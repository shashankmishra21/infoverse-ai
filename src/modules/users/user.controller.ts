import { AuthRequest } from "../../middlewares/auth.middleware";
import { getCompanyUsers } from "./user.service";
import { Response } from "express";

export const listCompanyUsers = async (req: AuthRequest, res: Response) => {
    try {
        const companyId = req.user!.companyId;
        const users = await getCompanyUsers(companyId);
        res.json(users);
    } catch (err: any) {
        res.status(400).json({ error: err.message })
    }

}