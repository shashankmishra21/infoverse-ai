import prisma from "../../config/prisma";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";

const JWT_SECRET = process.env.JWT_SECRET;

const generateCompanyCode = () => {
    return "INFV-" + Math.random().toString(36).substring(2, 8).toUpperCase();
};

//REGISTERR
export const registerUser = async (name: string, email: string, password: string, companyInput: string) => {
    const existingUser = await prisma.user.findFirst({ where: { email } });
    if (existingUser) throw new Error("Email already registered");

    const hashedPassword = await bcrypt.hash(password, 10);

    let company = await prisma.company.findUnique({
        where: { code: companyInput }
    });

    let role: "ADMIN" | "USER";

    if (company) {
        role = "USER";
    }
    else {
        const companyCode = generateCompanyCode();

        company = await prisma.company.create({
            data: {
                name: companyInput,
                code: companyCode,
            },
        });
        role = "ADMIN";
    }

    const user = await prisma.user.create({
        data: {
            name,
            email,
            password: hashedPassword,
            companyId: company.id,
            role,
        }
    });
    return { user, company }
}


//LOGIN
export const loginUser = async (email: string, password: string) => {
    const user = await prisma.user.findUnique({ where: { email } });
    if (!user) throw new Error("User not found");

    const isPasswordValid = await bcrypt.compare(password, user.password);
    if (!isPasswordValid) throw new Error("Invalid Credentials");

    const token = jwt.sign(
        {
            userId: user.id,
            company: user.companyId,
            role: user.role,
        },
        JWT_SECRET as string,
        { expiresIn: "7d" }
    );

    return { user, token };
}