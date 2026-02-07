import { Request, Response } from "express";
import { saveChat } from "./chat.services";
import { askAI } from "./rag.service";

export const askQuestion = async (req: Request, res: Response) => {
  try {
    const { question } = req.body;
    const user = (req as any).user;
    if (!user) {
      return res.status(401).json({ error: "Unauthorized" });
    }

    if (!question) {
      return res.status(400).json({ error: "Question is required" });
    }

    const answer = await askAI(user.userId, question);
await saveChat(user.userId, user.companyId, question, answer);

    return res.json({ answer });
  } catch (error) {
    console.error("RAG Error:", error);
    return res.status(500).json({ error: "Failed to process AI request" });
  }
};