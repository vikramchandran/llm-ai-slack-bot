from llm_core.slack_llm_client import SlackLLMClient
from availability.availability_fetcher import AvailabilityFetcher
from response.response_formatter import ResponseFormatter
from file_reader.file_reader import FileReader
import constants.constants as constants

def get_llm_response(input_data):
    file_reader = FileReader(input_data)
    file_data, file_id = file_reader.get_content_and_file_id()
    
    slack_llm_client = SlackLLMClient(file_data, file_id)
    user_identifier = slack_llm_client.get_user_identifier()

    availability_class = AvailabilityFetcher(user_identifier)
    user_data = availability_class.get_user_information()

    response_formatter = ResponseFormatter(user_data)
    return response_formatter.get_response(user_identifier)


if __name__ == "__main__":
    filename = constants.INPUT_FILE
    text_string = "Schedule a meeting with John for EST"
    get_llm_response(text_string, False)

    # main(filename, True)
   
