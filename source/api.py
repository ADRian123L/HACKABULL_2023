"""The program creates a an object that is used to access the OpenAI's API."""
import openai
import json
import requests
import os
import asyncio
import aiohttp

class OpenAI:
    """The class creates an object that is used to access the OpenAI's API."""
    # The class attributes are used to store the API key and the model.
    

    def __init__(self, api_key : str, model="davinci", temperature: float = 0.5, max_tokens: int = 100, prompt: str = "") -> None:
        """The constructor initializes the object with the API key and the model."""
        self.__api_key = api_key
        self.model = model
        openai.api_key = self.api_key
        openai.Engine.list()
        self.cache = {}
        self.temperature: float = temperature
        self.max_tokens: int = max_tokens
        self.prompt: str = prompt

    def get_model(self) -> str:
        """The method returns the model."""
        return self.model
    
    def get_api_key(self) -> str:
        """The method returns the API key."""
        return self.api_key
    
    def set_model(self, model : str) -> None:
        """The method sets the model."""
        self.model = model
    
    def set_api_key(self, api_key : str) -> None:
        """The method sets the API key."""
        self.__api_key = api_key
    
    def get_temperature(self) -> float:
        """The method returns the temperature."""
        return self.temperature
    
    def set_max_tokens(self, max_tokens : int) -> None:
        """The method sets the max_tokens."""
        self.max_tokens = max_tokens
    
    def get_max_tokens(self) -> int:
        """The method returns the max_tokens."""
        return self.max_tokens
    
    def temperature(self, temperature : float = 0.5) -> None:
        """The method sets the temperature."""
        self.temperature = temperature

    async def generate_text(self) -> str:
        """The method generates text based on the prompt."""
        if prompt in self.cache:
            return self.cache[prompt]
        
        async with aiohttp.ClientSession() as session:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.__api_key}"
            }
            data = {
                "model": self.model,
                "prompt": prompt,
                "max_tokens": self.max_tokens,
                "temperature": self.temperature,
                "top_p": 1,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "n": n
            }
            async with session.post("https://api.openai.com/v1/engines/davinci/completions", headers = headers, json = data) as response:
                response = await response.json()
                if response["choices"]:
                    self.cache[prompt] = response["choices"][0]["text"]
                    return response["choices"][0]["text"]
                else:
                    return "No response from the API."
    

            


if __name__ == "__main__":
    # The program creates an object that is used to access the OpenAI's API.
    pass