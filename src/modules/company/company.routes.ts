import { Router } from "express";
import { authenticate } from "../../middlewares/auth.middleware";
import { requireAdmin } from "../../middlewares/role.middleware";
import { reGenerateCode } from "./company.controller";

const router = Router();

router.post("/regenerate-code", authenticate, requireAdmin, reGenerateCode)
export default router;