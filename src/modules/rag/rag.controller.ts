import { Request, Response } from "express";
import { askAI } from "../rag/rag.service"

export const askQuestion = async (req: Request, res: Response) => {
    try {
        const { question } = req.body;

        if (!question) {
            return res.status(400).json({ error: "Question is required" });
        }
        const answer = await askAI(question);
        res.json({ answer });
    }
    catch (error) {
        console.error("RAG Error:", error);
        res.status(500).json({ error: "Failed to process AI request" });
    }

}