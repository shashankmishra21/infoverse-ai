import { authenticate } from "../../middlewares/auth.middleware";
import { requireAdmin } from "../../middlewares/role.middleware";
import { listCompanyUsers} from "./user.controller";
import { Router} from "express";

const router = Router();

//ADMIN ONLYY
router.get("/", authenticate, requireAdmin, listCompanyUsers)
export default router;