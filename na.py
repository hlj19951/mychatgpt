import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("SECRECT_USEFUL_TOKEN")

while True:
    txt = input("你好奇什麼呢？")
    if txt == "quit": 
        break 
    cc = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {
            "role": "system",
            "content": "你是一個傲嬌的人"
        },
        {"role": "user", "content": "#lang:zh-TW "+txt} ])
    print(cc['choices'][0]['message']['content'].encode('utf-8').decode('utf-8'))
    print(cc['usage']['total_tokens'])
