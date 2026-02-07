import { Router } from "express";
import { askQuestion } from "./rag.controller";
import { authenticate } from "../../middlewares/auth.middleware";

const router = Router();

router.post("/ask", authenticate, askQuestion);

export default router;