import slack
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

# here I used my server channel name called "#code_daily". You need to change as per your channel name

client.chat_postMessage(channel='#code-daily', text="Hello pro grammers, This is your bot, How can I help you ?")