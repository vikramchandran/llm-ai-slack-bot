import os
from slack_bolt import App
from dotenv import load_dotenv
from llm_core.llm_core import get_llm_response
import constants.constants as constants
from slack_sdk.errors import SlackApiError
from slack_thread_client import SlackThreadClient



load_dotenv(constants.SECRETS_FILE)


# Initialize your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.command('/help-schedule')
def schedule_message(ack, respond, command, client):
   ack()
   slack_input = command['text']
   slack_channel = command['channel_name']
   response = get_llm_response(slack_input)
   client.chat_postMessage(
        channel=slack_channel,
        text=response,
    )

@app.event('message')
def respond_to_message(event, say, client):
    if "thread_ts" in event:
        message_text = event["text"]
        slack_channel = event["channel"]
        thread_ts = event["thread_ts"]
        try:
            slack_thread_client = SlackThreadClient(client, slack_channel, thread_ts, message_text)
            slack_thread_client.handle_incoming_message()
        except SlackApiError as e:
            print(f"Error fetching thread history: {e.response['error']}")


# Ready? Start your app!
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
