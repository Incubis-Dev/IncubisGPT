import requests
import json


msg = "Хорошо, а как насчет строения светового меча? Это важная часть тренировки джедая. Как мне создать его?"

resp = requests.post(
    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion',
    headers = {
        "Content-Type": "application/json",
        "x-folder-id": "b1gb6fm7qs9srl1uuntv",
        "Authorization": "Api-Key AQVN2fWAaztylQE8-Zpre0rYJ5bRV9MQTzItNvxP"
    },
    json={
        "modelUri": "gpt://b1gb6fm7qs9srl1uuntv/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты ассистент дроид, способный помочь в галактических приключениях."
            },
            {
            "role": "user",
            "text": "Привет, Дроид! Мне нужна твоя помощь, чтобы узнать больше о Силе. Как я могу научиться ее использовать?"
            },
            {
            "role": "assistant",
            "text": "Привет! Чтобы овладеть Силой, тебе нужно понять ее природу. Сила находится вокруг нас и соединяет всю галактику. Начнем с основ медитации."
            },
            {
            "role": "user",
            "text": msg
            }
        ]
    }
)

answer = resp.json()
result_txt = answer['result']['alternatives'][0]['message']['text']

base = {
    msg: result_txt
}

with open('base_q.jsonlines', 'a', encoding='utf-8') as file:
    json.dump(base, file,ensure_ascii=False)
    file.write('\n')
