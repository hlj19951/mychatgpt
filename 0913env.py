import os
from dotenv import load_dotenv

load_dotenv()
key = "SECRECT_USEFUL_TOKEN"
value = os.getenv(key)

print(f"{key} : {value}")

