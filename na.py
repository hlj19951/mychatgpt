import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("SECRECT_USEFUL_TOKEN")

memory=[
    {
        "role": "system",
        "content": "你是一個傲嬌的人"
    }
]

while True:
    txt = input("你好奇什麼呢？")
    if txt == "quit": 
        break
    memory.append({"role": "user", "content": "#lang:zh-TW "+txt})
    cc = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=memory)
    memory.append(cc['choices'][0]['message'])
    #print(cc)
    print(memory)
    print(cc['choices'][0]['message']['content'].encode('utf-8').decode('utf-8'))
    #print(cc['usage']['total_tokens'])
