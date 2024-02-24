"""
use following models : gpt-3.5-turbo-instruct, babbage-002, davinci-002, gpt-3.5-turbo
for legacy endpoint /v1/completions
tried model text_davinci-003 as well does not exist anymore
all failed with error : 429 (exceeded current quota)
have to pay for using API  

"""
import requests
import argparse
import os

# parses user argument
# example: user input in terminal or cmd : python3 python-chatgpt.py "prompt" "file-name-for-saving-response"
# example: python3 python-chatgpt.py "print todays date" "todays-date.py"
parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAI Api")
parser.add_argument("file_name", help="Name of the file to save the response as .py")
args = parser.parse_args

api_endpoint = "https://api.openai.com/v1/chat/completions"
# in terminal run below before running the script
# export OPENAI_API_KEY=api-key-here
# the key is export to the variable and we can use it !
# export noly works in UNIX 
# windows use:  set OPENAI_API_KEY=api-key-here
# to unset use: set OPENAI_API_KEY= , do not assign anything
# power shell use: $env:OPENAI_API_KEY=api-key-here
api_key = os.getenv("OPENAI_API_KEY")

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

request_data = {
    "model": "text_davinci-003", 
    # prompt for open ai model
    "prompt": f"Write python script forto {args.prompt}. Provide only code, no text",
    # number of words, commas etc in response. charged per number of tokens used
    "max_tokens": 7,
    # value between 0-1, 1 is go crazy creative, 0 is predictable response
    "temperature": 0.5
}
# How to generate a request 
response = requests.post(api_endpoint, headers = request_headers, json=request_data)

if response.status_code == 200:
    response_text = response.json()["choices"][0] ["text"]
    # save response to another file called output.py
    # if file is not present it is created
    with open({args.file_name}, "w") as file:
        file.write(response_text)
else:
    print(f"request failed with {str(response.status_code)}")

print(response.json())