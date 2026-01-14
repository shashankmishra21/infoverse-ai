import { healthCheck } from "./health.controller";
import { Router } from "express";

const router = Router();

router.get("/", healthCheck)

export default router;