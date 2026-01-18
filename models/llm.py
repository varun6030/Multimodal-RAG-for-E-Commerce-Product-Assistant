import ollama

def generate_answer(query, context):
    prompt = f"""
You are a shopping assistant.

Context:
{context}

Question:
{query}

Answer clearly and concisely.
"""
    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]
