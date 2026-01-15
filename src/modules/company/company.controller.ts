import { AuthRequest } from "../../middlewares/auth.middleware";
import { Response } from "express";
import { reGenerateCompanyCode } from "./company.service";

export const reGenerateCode = async (req: AuthRequest, res: Response) => {

    try {
        const companyId = req.user!.companyId;

        

        if (!companyId) {
            return res.status(400).json({ error: "Company ID missing from token" });
        }
        const company = await reGenerateCompanyCode(companyId);
        res.json({
            message: "Company code regenerated successfully",
            company,
        })
    } catch (err: any) {
        res.status(400).json({ error: err.message })
    }
};