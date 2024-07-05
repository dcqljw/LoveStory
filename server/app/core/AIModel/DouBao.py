import requests
import json
from config.SETTINGS import DOUBAO_URL, DOUBAO_KEY


def dou_bao_chat(input_data):
    data = {"messages": [{"role": "system",
                          "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
                         {"role": "user",
                          "content": input_data}],
            "model": "ep-20240628015517-knb5k", "frequency_penalty": None, "function_call": None, "functions": None,
            "logit_bias": None, "logprobs": None, "max_tokens": None, "presence_penalty": None, "stop": None,
            "stream": True, "stream_options": None, "temperature": None, "tools": None, "top_logprobs": None,
            "top_p": None}
    headers = {
        "Authorization": f"Bearer {DOUBAO_KEY}"
    }
    post = requests.post(DOUBAO_URL, json=data, headers=headers, stream=True)
    for i in post.iter_lines():
        decode = i.decode()
        data = decode[6:]
        if data != "[DONE]" and data.strip() != "":
            # print(data)
            dumps = json.loads(data)
            print(dumps['choices'][0]['delta']['content'], end="")
            text = dumps['choices'][0]['delta']['content']
            text = json.dumps({"text": text}, ensure_ascii=False)
            yield f"data: {text}\n"
