## Large Language Models: Recruiting Agent Slack Bot

Welcome to the AI Recruiter Slack Bot! This project aims to revolutionize the recruitment process for software engineers in the AI business by harnessing the power of Artificial Intelligence (AI) and Language Models (LLMs). Our Slack bot provides recruiters with intelligent scheduling assistance and streamlined communication within Slack channels, making it easier than ever to find and hire top talent

### Introduction to AI Recruiting:
In today's competitive tech landscape, finding and hiring top talent is essential for companies looking to stay ahead. Traditional recruiting methods often fall short in identifying and engaging with qualified candidates in this specialized field.


### Solution:
This project aims to create a versatile Slack bot tailored for recruiters, utilizing Python and Language Models (LLMs) to streamline recruiting processes within Slack channels. The bot facilitates seamless interaction with Open AI's API endpoints, providing users with scheduling assistance and intelligent responses powered by LLMs and Slack's Bolt API. 

### Setup Instructions:

1. Clone the repository to your local machine.


```
git clone <repository-url>
```

2. Navigate to the project directory.
```
cd <project-directory>
```
3. Install project dependencies using pip.

```
python3 -m pip install -r requirements.txt
```

4. Follow the setup instructions outlined in the [Slack API Quickstart Tutorial](https://api.slack.com/start/quickstart) to create a new Slack app and add the setup the relevant scopes + permissions. The following bot token scopes must be granted:
    1. app_mentions:read
    2. channels:history
    3. chat:write
    4. commands
    5. groups:history
    6. im:history
    7. reactions:read

5. Setup [ngrok](https://ngrok.com/download) to tunnel Slack's API requests to your localhost

6. Configure slash commands in the Slack app to point to your ngrok forwarding port 

6. Add the Slack app to your desired Slack channel(s) where recruiting activities will take place.

7. Utilize the /help-schedule command to leverage the benefits of LLMs in your day-to-day recruiting

### Usage:

After successfully adding the Slack app to your channel, users can interact with the bot using the following commands:

1. /help-schedule: Initiates interaction with the bot for scheduling assistance.
2. DM the Slack bot within a Slack thread for further scheduling assistance
### Features:

Scheduling Assistance: Users can request scheduling assistance by using the /help-schedule command. The bot interacts with an in-built LLM, which accesses Open API endpoints to provide intelligent scheduling recommendations.

### Contributing:
Contributions to this project are welcomed! Whether it's fixing bugs, adding features, or improving documentation, feel free to submit pull requests.

### Feedback and Support:
For any questions, feedback, or support regarding this project, please contact vikramchandran98@gmail.com.

### License:
This project is licensed under the MIT License.

### Acknowledgments:

Special thanks to the Slack API documentation and the OpenAI team for their invaluable resources and support.


### Disclaimer:
This project utilizes language models powered by OpenAI. Please review the terms of use and privacy policy of OpenAI before using this application.

### About the Author:
This project was developed by Vikram Chandran. Connect with me on [LinkedIn](https://www.linkedin.com/in/vikramchandran/) for more information about this project and other initiatives.
