import platform
import time 
from tqdm import tqdm 
import os 
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError 
from slack_print import SlackPrint

host_system = platform.uname()

print(f"Analyzing system internals")

for i in tqdm(host_system):
    time.sleep(1)

with open("sysinfo.txt", "w") as text_file: 
    text_file.write(f"System: {host_system.system}\n")
    text_file.write(f"Node Name: {host_system.node}\n") 
    text_file.write(f"Release: {host_system.release}\n")
    text_file.write(f"Version: {host_system.version}\n")
    text_file.write(f"Machine: {host_system.machine}\n")
    text_file.write(f"Processor: {host_system.processor}\n")

# Run SLACK_BOT_TOKEN python3 <script_name.py>
client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])


try: 
    filepath="./sysinfo.txt"
    #response = client.files_upload(channel="#test", file=filepath)
    sp=SlackPrint('SLACK_TOKEN', '#test') # Enter the slack token here 
    sp.upload('sysinfo.txt')
except SlackApiError as e: 
    assert e.response["ok"] is False
    assert e.response["error"] 
    print(f"got an error: {e.response['error']}")