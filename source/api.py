"""The program creates a an object that is used to access the OpenAI's API."""
import openai
import json
import requests
import os

class OpenAI:
    """The class creates an object that is used to access the OpenAI's API."""
    def __init__(self, api_key : str, model="davinci") -> None:
        """The constructor initializes the object with the API key and the model."""
        self.api_key = api_key
        self.model = model
        openai.api_key = self.api_key
        openai.Engine.list()
    
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
    
    def generate_text(self, prompt : str, max_tokens : int = 100, temperature = 0.5, n = 1) -> json:
        """The method generates text based on the prompt."""
        response = openai.Completion.create(
            engine = self.model,
            prompt = prompt,
            max_tokens = max_tokens,
            temperature = temperature,
            n = n,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0,
            stop = None,
        )

        if response.choices:
            return response.choices[0].text
        else:
            return "No response from the API."

