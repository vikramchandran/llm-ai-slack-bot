import json 
import constants.constants as constants
from regex.regex_helper import is_valid_email
import os 

class AvailabilityFetcher:
    def __init__(self, input_filter):
        self.input_filter = input_filter

    def get_matching_persons(self, persons):
        if is_valid_email(self.input_filter):
            return [person for person in persons if person["email_address"] == self.input_filter]
        else:
            return [person for person in persons if person["first_name"] == self.input_filter]
    
    def get_user_information(self):
        try:
            current_dir = os.path.dirname(__file__)

            file_path = os.path.join(current_dir, "availability.txt")

            # Load data from the file
            with open(file_path, "r") as file:
                data = json.load(file)
            
            # Access the list of persons
            persons = data["persons"]
            
            # Filter persons by first name
            matching_persons = self.get_matching_persons(persons)
            
            if len(matching_persons) == 1:
                # If only one user found, return that user's information
                return matching_persons[0]
            elif len(matching_persons) > 1:
                # If multiple users found, return message about duplicate first name
                return constants.USER_DUPLICATE
            else:
                # If user not found
                return constants.USER_NOT_EXIST

        
        except FileNotFoundError:
            return constants.FILE_NOT_FOUND
