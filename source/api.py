"""The program creates a an object that is used to access the OpenAI's API."""
import openai
import json
import requests
import os

class OpenAI:
    """The class creates an object that is used to access the OpenAI's API."""
    def __init__(self, api_key : str, model="davinci") -> None:
        """The constructor initializes the object with the API key and the model."""
        self.__api_key = api_key
        self.model = model
        openai.api_key = self.__api_key
        openai.Engine.list()
        self.max_tokens: int = 100
        self.temperature: float = 0.5
        self.n: int = 1
        self.prompt: str = "Testing the OpenAI API."

    def generate_text(self) -> str:
        """The method generates text based on the prompt."""
        response = openai.Completion.create(
            engine = self.model,
            prompt = self.prompt,
            max_tokens = self.max_tokens,
            temperature = self.temperature,
            n = self.n,
            stop = None,
        )

        if response.choices:
            return response.choices[0].text
        else:
            return "No response from the API."

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
        self.api_key = api_key
    
    def set_prompt(self, prompt:str) -> None:
        """The method sets the prompt."""
        self.prompt = prompt

if __name__ == "__main__":
    # The program creates an object that is used to access the OpenAI's API.
    key = os.environ.get("OPENAI_API_KEY")
    AI : OpenAI = OpenAI(api_key = key)

    # The program generates text based on the prompt.
    prompt = "What is the binary representation of 10?"
    print(AI.generate_text(prompt))