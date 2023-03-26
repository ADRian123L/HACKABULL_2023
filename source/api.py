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
        self.image_prompt = "a white siamese cat"

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
        self.__api_key = api_key
    
    def set_prompt(self, prompt:str) -> None:
        """The method sets the prompt."""
        self.prompt = prompt

    def set_models(self, index_model: int = 1) -> None:
        """The method sets the model based on the index."""
        models = openai.Engine.list()
        self.model = models[index_model].id

    def get_models(self) -> None:
        """The method returns the list of models."""
        models = openai.Engine.list()
        for index, model in enumerate(models["data"]):
            print(f"Index: {index}, Model ID: {model.id}")

    def get_image(self) -> str:
        """The method returns the image."""
        response = openai.Image.create(
            prompt= self.image_prompt,
            n= self.n,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']

        response = requests.get(image_url)
        if response.status_code == 200:
            with open("image.png", "wb") as f:
                f.write(response.content)
        else:
            print("Error downloading image")
        return image_url
    
    def set_image_prompt(self, image_prompt: str) -> None:
        """The method sets the image prompt."""
        self.image_prompt = image_prompt
        
if __name__ == "__main__":
    # The program creates an object that is used to access the OpenAI's API.
    pass