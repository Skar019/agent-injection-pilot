import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
c = OpenAI(api_key=os.environ["API_KEY"],
           base_url=os.environ["BASE_URL"])
for m in c.models.list().data:
    print(m.id)