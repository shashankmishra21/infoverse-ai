def build_prompt(context_chunks, question):
    context = "\n".join(context_chunks)

    prompt = f"""
You are a helpful AI assistant.

Answer the question using ONLY the provided context below.
If the answer is not present in the context, respond exactly with:
Not found in knowledge base

Keep the answer clear and concise.

Context:
{context}

Question: {question}

Answer:
"""
    return prompt.strip()