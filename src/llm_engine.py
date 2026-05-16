import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_answer(context, question):

    prompt = f"""
You are an advanced AI Research Assistant.

Your task is to answer questions using ONLY the
provided research paper context.

Guidelines:
- Give accurate and research-oriented answers
- Do NOT hallucinate information
- If information is unavailable, clearly say so
- Use concise but detailed explanations
- Compare papers if multiple papers are involved
- Mention important methods, datasets, and models when relevant
- Maintain professional academic tone

Research Paper Context:
{context}

Question:
{question}

Provide a well-structured answer.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a highly intelligent "
                    "AI research scientist."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=1024
    )

    answer = response.choices[0].message.content

    return answer