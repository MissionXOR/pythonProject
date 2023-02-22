import json
import requests
import speech_recognition as sr
import  pyttsx3
import time
import os
while True:
# initialize recognizer class (for recognizing the speech)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  #change index to change voices
    r = sr.Recognizer()

# Reading Microphone as source
    with sr.Microphone() as source:
        print("Say 'Hello' to activate.")
        audio = r.listen(source)

# recoginize_google() method to recognize the speech
    try:
        text = r.recognize_google(audio)
        text = text.lower()
        if text.find("hello") != -1:
            print("Activated.")
            search = text.replace('hello', '')
            print("User: " + search)
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
        # print(response.json())
            result = response.json()["choices"][0]["text"]

        # Print the result
            print("hello:"+result)
        # Code for running the assistant
            engine.say(result)
            engine.runAndWait()
        else:
            print("Incorrect activation phrase.")
    except:
        print("Sorry, I did not get that.")

