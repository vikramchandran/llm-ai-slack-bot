from llm_core.llm_processors import grammar_terms_chain
import json
from regex.regex_helper import is_valid_email



class SlackLLMClient:
    def __init__(self, file_data, file_id):
        self.file_data = file_data
        self.file_id = file_id
        self.isEmail = is_valid_email(file_data)

    def __fetch_grammar_details(self):
        term, run_id = grammar_terms_chain(
            u_msg=self.file_data,
            file_id=self.file_id,
        )
        return term 
    
    def get_user_identifier(self):
        person_term = self.__fetch_grammar_details()
        term_json = person_term.json()
        term_dict = json.loads(term_json)
        user_object = term_dict['persons'][0]
        if self.isEmail:
            return user_object["email_address"]
        else:
            return user_object["first_name"]