import { Request, Response } from "express";
import { registerUser, loginUser } from "./auth.service";

//Register
export const register = async (req: Request, res: Response) => {
    try {
        const { name, email, password, company } = req.body;

        if (!name || !email || !password || !company) {
            return res.status(400).json({ error: "All fields required" });
        }

        const result = await registerUser(name, email, password, company);

        const { password: _, ...safeUser } = result.user;

        res.status(201).json({
            message:
                result.user.role === "ADMIN" ? "Company created. You are ADMIN." : "Joined company successfully.",
            company: {
                name: result.company.name,
                code: result.company.code,
            },
            user: safeUser,
        });
    } catch (err: any) {
        res.status(400).json({ error: err.message });
    }
}

// Login
export const login = async (req: Request, res: Response) => {
    try {
        const { email, password } = req.body;
        const data = await loginUser(email, password);
        res.json(data);
    } catch (err: any) {
        res.status(401).json({ error: err.message })
    }
}
