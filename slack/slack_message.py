import os 
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError 

client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])

try: 
    response = client.chat_postMessage(channel="#test", text="SUP!")
    #assert response["message"]["text"] == "Hello World!"
except SlackApiError as e: 
    assert e.response["ok"] is False
    assert e.response["error"] 
    print(f"got an error: {e.response['error']}")