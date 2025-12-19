import requests
import json
import os

import user

url = "https://api.siliconflow.cn/v1/chat/completions"
models = ["deepseek-ai/DeepSeek-R1-0528-Qwen3-8B"]
roles = ["user", "assistant", "system"]


def post_chat_completions(content: str):
    if not os.path.exists("APIKey.json"):
        user.make_empty_apikey_file()

    with open("APIKey.json", "r") as f:
        data = json.load(f)
        apikey = data.get("APIKey")

    payload = {
        "model": models[0],
        "messages": [
            {
                "role": roles[0],
                "content": content
            }
        ],
        "stream": False,
        "max_tokens": 4096,
        "enable_thinking": False,
        "thinking_budget": 4096,
        "min_p": 0.05,
        "stop": None,
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.5,
        "n": 1,
        "response_format": { "type": "text" },
    }
    headers = {
        "Authorization": f"Bearer {apikey}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()

if __name__ == "__main__":
    if not user.check_apikey_valid():
        user.write_apikey(input("请输入APIKey: "))
    print(post_chat_completions("介绍一下阿森纳"))