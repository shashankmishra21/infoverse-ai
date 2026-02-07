import prisma from "../../config/prisma";

 // Save a chat message (Q/A pair)
export const saveChat = async (
  userId: string,
  companyId: string,
  question: string,
  answer: string
) => {
  return (prisma as any).chat.create({
    data: {
      userId,
      companyId,
      question,
      answer,
    },
  });
};
 //Get recent chats for conversational memory

export const getRecentChats = async (userId: string) => {
  return (prisma as any).chat.findMany({
    where: { userId },
    orderBy: { createdAt: "desc" },
    take: 5, // memory window (last 5 chats)
  });
};