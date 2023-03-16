import pyautogui
import requests
# url="https://e655638aa411eb60c0.gradio.live/"
url=input("Enter gf url: ")
def blender_bot(text):
    global url
    response = requests.post(f"{url}run/predict", json={
        "data": [
            text,
        ]
    }).json()

    data = response["data"][0]
    return data

import requests
from time import sleep
  
#
output_lang={
    1:"en",
    2:"hi",
    3:"bn"
} 
from googletrans import Translator

# Create a Translator object
translator = Translator()
def trans(text, id):
    # Translate a sentence from English to Spanish
    result = translator.translate(text,  dest=output_lang[id])
    # Print the translated text
    return result.text

  
import speech_recognition as sr
r = sr.Recognizer()

def get_speech_duration(sentence):
    # Speech rate in characters per second
    speech_rate = 12
    # Calculate the number of characters in the sentence
    num_chars = len(str(sentence))
    # Calculate the estimated duration in seconds
    duration = num_chars / speech_rate
    return duration


dict_lnag={  1: "en-In",
                2: "hi-IN",
                3: "bn-IN",}
print("Enter your input language:")
print("1. English\n2. Hindi\n3. Bengali")
input_lang=int(input("Enter your choice: "))
print("\n")
print("Enter your output language:")
print("1. English\n2. Hindi\n3. Bengali")
out_lang=int(input("Enter your choice: "))

while(1):	

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        print("Recognizing Now .... ")
    try:
        text = r.recognize_google(audio,language=dict_lnag[input_lang])
        #write a text file  
        bot_reply=blender_bot(trans(text,1))
        gf=trans(bot_reply,out_lang)
        print ("you said: " + text)
        print(bot_reply)
        print(gf)
        if len(gf)>=1:
            with open("demo.txt", "w", encoding="utf-8") as file:
                file.write(gf)

            
            reload_button = pyautogui.locateOnScreen("./reload.png",confidence=0.9)
            send_button_x, send_button_y = pyautogui.center(reload_button)
            pyautogui.click(send_button_x, send_button_y)

            read_button = pyautogui.locateOnScreen("./aloud.png",confidence=0.9)
            send_button_x, send_button_y = pyautogui.center(read_button)
            pyautogui.click(send_button_x, send_button_y)
            # pyautogui.click(529,76)
            sleep_time=get_speech_duration(gf)
            sleep(sleep_time)
         

    except Exception as e:
        print("Sorry could not recognize your voice")
        print(e)
        continue
                    
       