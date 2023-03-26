from api import OpenAI
import openai
import os

import openai

# Set your API key
key = os.getenv("OPENAI_API_KEY")
AI: OpenAI = OpenAI(api_key = key)
AI.set_prompt("Testing the OpenAI API, can you tell something about AI?")
models = openai.Engine.list()
data = models["data"]
idt = data[0].id
print(idt)
