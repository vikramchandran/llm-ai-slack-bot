import os
import re
from typing import Type
from pydantic import BaseModel

def camel_to_snake(name):
    """
    Convert a camel case string to snake case.
    """
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

class PromptManager:
    def __init__(self):
        self.package_dir = os.path.dirname(os.path.abspath(__file__))
        self.prompts_dir = os.path.join(self.package_dir, "prompts")
        self.prompts = {}
        self._load_prompts()

    def _load_prompts(self) -> None:
        """
        Load all prompts from the prompts directory and store them in the self.prompts dictionary.
        The key will be the model name in snake case and the value will be the prompt text.
        e.g. {"when_term_model": "System prompt for the when term as string"}
        """
        for file_name in os.listdir(self.prompts_dir):
            if file_name.endswith(".text"):
                base_name = file_name[:-len('_prompt.text')] + "_model"
                with open(os.path.join(self.prompts_dir, file_name), 'r') as file:
                    self.prompts[base_name] = file.read()

    def get_prompt(self, model: Type[BaseModel]) -> str:
        """
        Get the prompt for the provided Pydantic model class.

        Args:
            model (Type[BaseModel]): The Pydantic model class to get the prompt for.

        Returns:
            str: The prompt text for the model.
        """
        model_name = camel_to_snake(model.__name__)
        if model_name not in self.prompts:
            raise FileNotFoundError(f"No prompt found for model {model.__name__}")
        return self.prompts[model_name]
