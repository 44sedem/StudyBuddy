import httpx
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

async def call_llm(prompt: str, max_tokens: int = 1000, temperature: float = 0.3) -> str:
    """
    Async LLM call — swap provider here without touching feature code.
    Supports OpenAI-compatible APIs.
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
            json={
                "model": "gpt-4o-mini",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": max_tokens,
                "temperature": temperature,
            },
            timeout=30.0
        )
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
