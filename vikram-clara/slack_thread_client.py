from regex.regex_helper import extract_name
from llm_core.llm_core import get_llm_response


class SlackThreadClient:
    def __init__(self, client, slack_channel, thread_ts, message_text, inclusive = True, limit=1):
        self.client = client
        self.channel = slack_channel
        self.thread_ts = thread_ts
        self.message_text = message_text
        self.inclusive = inclusive
        self.limit = limit
        self.last_message_text, self.last_message_ts, self.last_message_is_bot = self.__get_latest_message_attributes()
        self.last_message_name = self.__get_latest_message_name()


    def __get_conversation_history(self):
        return self.client.conversations_history(channel=self.channel, latest=self.thread_ts, inclusive=self.inclusive, limit=self.limit)
    
    def __get_latest_message(self):
        return self.__get_conversation_history()["messages"][0]
    
    def __get_latest_message_attributes(self):
        latest_message = self.__get_latest_message()
        return [latest_message["text"], latest_message["ts"], latest_message.get("bot_id")]
    
    def __get_latest_message_name(self):
        return extract_name(self.last_message_text)

    def __send_user_unavailable_message(self):
        self.client.chat_postMessage(
            channel=self.channel,
            text="Unavailable to find availability data for %s. Please update user availability"%self.last_message_name,
            thread_ts=self.last_message_ts,
        )

    def __send_response_in_thread(self, response):   
        self.client.chat_postMessage(
            channel=self.channel,
            text=response,
            thread_ts=self.last_message_ts,
        )

    def __schedule_user_message(self):
        self.__send_response_in_thread("Scheduling meeting...")
        response = get_llm_response(self.message_text)
        self.__send_response_in_thread(response)
    
    def handle_incoming_message(self):
        if self.last_message_name == self.message_text:
            self.__send_user_unavailable_message()
        else:
            self.__schedule_user_message()

    
