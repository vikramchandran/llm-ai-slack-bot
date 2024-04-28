import constants.constants as constants

class ResponseFormatter:
    def __init__(self, response):
        self.response = response

    def __generate_valid_response(self):
        first_name = self.response['first_name']
        last_name = self.response['last_name']
        email_address = self.response['email_address']
        role_value_1 = self.response['arbitrary_details'][0]['value']
        role_value_2 = self.response['arbitrary_details'][1]['value']

        # Constructing the string
        result_string = f"A meeting is scheduled with {first_name} {last_name} with email {email_address} for the role {role_value_1} {role_value_2}"
        return result_string
    
    def get_response(self, user):
        if self.response == constants.FILE_NOT_FOUND:
            return self.response
        elif self.response == constants.USER_DUPLICATE:
            return "There exists multiple candidates with name %s. Please provide candidate's email address instead in this thread"%user
        elif self.response == constants.USER_NOT_EXIST:
            return "There exists no availability data for %s. Please validate spelling and respond with verified candidate's name in this thread"%user
        else:
            return self.__generate_valid_response()