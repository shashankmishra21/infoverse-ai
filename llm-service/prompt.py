def build_prompt(context_chunks, question):
    context = "\n\n".join(context_chunks)

    return f"""
You are an enterprise-grade AI assistant.
Answer ONLY using the provided context.
If the answer is not present, say:
"I don’t have enough information to answer that."

Context:
{context}

Question:
{question}

Answer:
"""