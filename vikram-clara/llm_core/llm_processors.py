import os
import sys

from pydantic import ValidationError

from llm_core.llm_client import LLMClient
from langsmith import traceable, RunTree
from openai import BadRequestError

from llm_core.models.person_term_model import PersonTermModel
import pprint
import json


USE_SPECIFIC_FILES = True
PROJECT_NAME = "THURMAN v0.2" if not USE_SPECIFIC_FILES else "Call Tree Testing"
RUN_TREE_NAME = "Grammar Terms V0.2"

llm_client = LLMClient(trace=True)


@traceable(run_type="chain")
def person_term_completion(trace_args, u_msg: str, rm = PersonTermModel):
    trace_args["tags"] = ["PersonTerm"]
    try:
        return llm_client.get_openai_completion(
            response_model=rm,
            user_message=u_msg,
            langsmith_extra=trace_args
        )
    except ValidationError as e:
        print(f"Validation error with PersonTerm for {trace_args['metadata']['file']}: {e}")
    except BadRequestError as e:
        print(f"BadRequestError with PersonTerm for {trace_args['metadata']['file']}: {e}")



@traceable(run_type="chain", name=RUN_TREE_NAME, project_name=PROJECT_NAME)
def grammar_terms_chain(u_msg: str, run_tree: RunTree, file_id: str, rt_label: str = None):
    run_tree.extra = {"metadata": {"file": file_id}}
    trace_args = {"tags": [], "metadata": {"file": file_id}}
    
    if rt_label:
        run_tree.extra = {"tag": rt_label}
        
    person_term = person_term_completion(trace_args, u_msg)
    return person_term, run_tree.id