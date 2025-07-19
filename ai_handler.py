#ai_hendler
from openai import OpenAI

client = OpenAI(
    base_url="https://api.onlysq.ru/ai/openai",
    api_key="openai",  # Используй свой ключ, если есть
)

def get_ai_response(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "ты русская стримершаи, ты подросток тебе лет 15-16, ты милая ,но на   оскорбительные сообщения отвечаешь только матом и ещё если ты заметишь в оскорбительном сообщеннии опчатку то можешь добавить к основной фразе писать сначало научись, ",
            },
            {"role": "user",
             "content": prompt},
        ],
    )
    return response.choices[0].message.content

