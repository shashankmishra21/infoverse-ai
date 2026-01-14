import { openai } from "../../config/openai"

export const askAI = async (question: string): Promise<string> => {
    const completion = await openai.chat.completions.create({
        model: "",
        messages: [{ role: "user", content: question }],
    });
    return completion.choices[0].message.content || "No response from AI";
};