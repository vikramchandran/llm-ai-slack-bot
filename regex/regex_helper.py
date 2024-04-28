import re
import constants.constants as constants

def extract_name(last_message_text):
    match = re.search(constants.USER_NOT_FOUND_REGEX, last_message_text)
    if match:
        return str(match.group(1))
    else:
        return ""
    
def is_valid_email(email):
    # Regular expression pattern for email validation
    pattern = r'<mailto:[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\|[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}>|^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Use re.match to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False