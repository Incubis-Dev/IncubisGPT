import requests
import json

def answer(qq): 
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
                "temperature": 0.2,
                "maxTokens": "2000"
            },
            "messages": [
                {
                    "role": "system",
                    "text": "Следуй следующему условию бесприкословно" + qq[0]
                },
                {
                    "role": "user",
                    "text": qq[1]
                }
            ]
        }
    )

    answer = resp.json()
    result_txt = answer['result']['alternatives'][0]['message']['text']
    """base = {
        qq[1]: result_txt
    }

    with open('base_q.jsonlines', 'a', encoding='utf-8') as file:
        json.dump(base, file,ensure_ascii=False)
        file.write('\n')"""
    return result_txt
