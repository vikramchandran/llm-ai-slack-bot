import os 
import constants.constants as constants
class FileReader:
    def __init__(self, input_data):
        self.input_data = input_data
    
    def __read_email(self, file_path: str) -> str:
        with open(file_path, "r") as file:
            return file.read()
        
    def __process_as_file(self):
        return ".txt" in self.input_data

    def get_content_and_file_id(self):
        if self.__process_as_file():
            email_str = self.__read_email(self.input_data)
            if "<html>" in email_str.lower():
                print(f"skipping {self.input_data} (html)")
                next
            elif len(email_str) > 1000:
                print(f"truncating {self.input_data}")
                email_str = email_str[:1000]
            file_id = os.path.basename(self.input_data)
            return email_str, file_id
        else:
            return self.input_data, constants.INPUT_FILE