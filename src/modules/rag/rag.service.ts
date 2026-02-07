import axios from "axios";
import { getRecentChats } from "./chat.services";

const RETRIEVAL_URL = process.env.RETRIEVAL_URL || "http://localhost:8002";

export const askAI = async (userId: string, question: string): Promise<string> => {
  try {
    // Fetch recent chat memory
    const recentChats = await getRecentChats(userId);

    const historyText = recentChats
      .map((c: any) => `User: ${c.question}\nAssistant: ${c.answer}`)
      .join("\n\n");

    // Send memory + question to retrieval
    const response = await axios.post(`${RETRIEVAL_URL}/ask`, {
      query: `${historyText}\n\nUser Question: ${question}`,
    });

    return response.data.answer || "No response from RAG";
  } catch (error: any) {
    console.error("RAG Service Error:", error?.response?.data || error.message);
    throw new Error("Failed to connect to RAG pipeline");
  }
};