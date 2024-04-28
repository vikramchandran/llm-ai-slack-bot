from typing import Dict, Type, Optional

import instructor
from dotenv import load_dotenv
from openai import OpenAI
from llm_core.prompt_manager import PromptManager
from pydantic import BaseModel

from langsmith import traceable
from langsmith.wrappers import wrap_openai


SECRETS_FILE = "secrets.env"

class LLMClient:
    """General purpose Language Model (LLM) client that integrates with OpenAI services."""

    def __init__(self, trace=False) -> None:
        load_dotenv(SECRETS_FILE)
        self.prompts = PromptManager()
        self.openai = OpenAI()

        # If we want to trace with Langsmith, we wrap the client and then patch it.
        if trace:
            wrapped_client = wrap_openai(self.openai)
            self.openai_patched = instructor.patch(wrapped_client, mode=instructor.Mode.TOOLS)
        else:
            self.openai_patched = instructor.patch(self.openai)

    def get_openai_completion(
        self,
        user_message: str,
        model: str = "gpt-4",
        max_tokens: int = 4000,
        temperature: float = 0,
        seed: int = 123,
        max_retries: int = 1,
        response_model: Type[BaseModel] = None,
        system_message: str = None,
        langsmith_extra: Optional[Dict] = None,
    ) -> BaseModel:
        
        if not system_message:
            system_message = self.prompts.get_prompt(response_model)

        completion = self.openai_patched.chat.completions.create(
            model=model,
            response_model=response_model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message},
            ],
            max_tokens=max_tokens,
            temperature=temperature,
            seed=seed,
            max_retries=max_retries,
            **({"langsmith_extra": langsmith_extra} if langsmith_extra else {}),
        )
        return completion
    
    @traceable(name="OpenAI Completion")
    def get_and_trace_openai_completion(
        self,
        response_model: Type[BaseModel] = None,
        user_message: str = None,
        system_message: str = None,
        model: str = "gpt-4",
        max_tokens: int = 4000,
        temperature: float = 0,
        seed: int = 123,
        max_retries: int = 1,
        langsmith_extra: Optional[Dict] = None,
    ) -> BaseModel:
        
        traced_completion = self.get_openai_completion(
            response_model=response_model,
            system_message=system_message,
            user_message=user_message,
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            seed=seed,
            max_retries=max_retries,
            langsmith_extra=langsmith_extra,
        )
        return traced_completion

