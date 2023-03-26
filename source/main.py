from api import OpenAI
import asyncio
import os

async def main():
    key = os.environ.get("OPENAI_API_KEY")
    AI: OpenAI = OpenAI(key)
    AI.set_prompt(prompt="What is the binary representation of 10?")
    response = await OpenAI.generate_text()
    print(response)

asyncio.run(main())

