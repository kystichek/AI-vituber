from openai import OpenAI

client = OpenAI(
    base_url="https://api.onlysq.ru/ai/openai",
    api_key="openai",  # Используй свой ключ, если есть
)

def get_ai_response(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content

