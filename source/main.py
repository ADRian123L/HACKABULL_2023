from api import OpenAI
import os

# The program creates an object that is used to access the OpenAI's API.
key = os.environ.get("OPENAI_API_KEY")
AI : OpenAI = OpenAI(api_key = key)
