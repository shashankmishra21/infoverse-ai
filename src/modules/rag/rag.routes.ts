import { Router } from "express";
import { askQuestion } from "./rag.controller";

const router = Router();

router.post("/ask", askQuestion);

export default router;