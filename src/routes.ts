import { Express } from "express";
import healthRoutes from "./modules/health/health.routes";
import ragRoutes from "./modules/rag/rag.routes";

export const registerRoutes = (app: Express) => {
    app.use("/health", healthRoutes);
    app.use("/api/rag", ragRoutes);
};