import json
import requests
import  pyttsx3
import time
import os

search="what do you know about bubt"
# Define the endpoint
endpoint = "https://api.openai.com/v1/completions"

# Define the headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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",
}

# Define the data
data = {
    "model": "text-davinci-003",
    "prompt": search,
    "temperature": 0,
    "max_tokens": 1024,
}

# Send the request
response = requests.post(endpoint, json=data, headers=headers)
#print(response.json())
result = response.json()["choices"][0]["text"]


# Print the result
print(result)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  #change index to change voices
engine.setProperty('rate', 150)
engine.say(result)
engine.runAndWait()