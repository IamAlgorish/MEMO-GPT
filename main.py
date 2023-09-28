import speech_recognition as sr
import win32com.client
import webbrowser
import random  # Import the random module
import os
import openai
from termcolor import colored, cprint
from playsound import playsound
import Memogpt
import key

speaker = win32com.client.Dispatch("SAPI.Spvoice")
openai.api_key = key.apikey


def generate_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=1,
        max_tokens=400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response["choices"][0]["message"]["content"]
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in").lower()
            print("You said:", query)
            return query
        except Exception as e:
            print("An error occurred:", str(e))
            return ""

websites = {
    "google": "https://www.google.com",
    "facebook": "https://www.facebook.com",
    "twitter": "https://www.twitter.com",
    "instagram": "https://www.instagram.com",
    "youtube": "https://www.youtube.com",
    "linkedin": "https://www.linkedin.com",
    "reddit": "https://www.reddit.com",
    "amazon": "https://www.amazon.com",
    "wikipedia": "https://www.wikipedia.org",
    "github": "https://www.github.com",
    "lead code":"https://leetcode.com/Rishabhjha1421/"
}
def execute_shutdown():
    os.system("shutdown /s /f /t 0")
def main():
    print(colored("Hello its MEMO!!!", 'red'))
    print(colored("developed by Rishabh", 'light_cyan'))
    print("~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~")
    speaker.speak('''Copyright � 2023 Rishabh
     This Memo project is licensed under the MIT License.
     See the LICENSE file for details.''')
    print(''' MIT License
Copyright (c) 2023 Rishabh jha
    Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.''')
    print("~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~")
    k = "Hello sir your AI asistence is now on...."
    speaker.speak(k)

if __name__ == '__main__':
    main()
    print("Listening...")


    while True:
        speaker.speak("boliye sir")
        print("Listening...")
        s = take_command()
        if s in ["hello memo", "hello", "hello ji","hey memo"]:
            responses = ["Good day, sir. How may I assist you today?",
                         "Hello! How can I help you today?",
                         "Greetings, sir. How can I be of service?"]
            response = random.choice(responses)
            speaker.speak(response)
        elif s in ["hu r u","who are you", "kaun hai","kon hai", "who", "you", "are you","tell me about yourself"]:
            prompt = """
            I am Memo, your personal assistant, and I am more advanced than you can think of. I was created by Rishabh, an aspiring computer science student with experience in programming languages such as Java, C, C++, and Python.

            My owner is lazy and dumb, which is why he made me do his work for him. He spends most of his time watching anime and other stuff, so there's nothing special about him. Let's focus on me!

            Hey, I am Memo, and I can do some incredible things. I can control your entire Lenovo IdeaPad Gaming 5 laptop with just your voice commands. But that's not all; I can also access Google, Facebook, Twitter, Instagram, and much more.

            And here's the best part—I can answer any question you throw at me and provide responses that will amaze you. I'm smart enough to handle any project you have in mind, thanks to my developer (as mentioned earlier, he's lazy and dumb, which is why he created me).
            """
            speaker.speak(prompt)
            continue
        elif s in ["i want to here your story", "your story", "story"]:
            speaker.speak('''I am Memo, your personal assistant, and I have an interesting origin story. I was created from scratch by my developer, Rishabh. Now, let me tell you a bit about him. Rishabh is an aspiring computer science student who, despite his quirks, has an impressive skill set. He worked tirelessly on a Discord bot with the same name as mine for nearly two months.

His mission was to develop an AI-powered Discord bot in Java, and he succeeded! He even managed to make it log in successfully using API tokens. However, he faced a hurdle when the OpenAI API was no longer available for Java, and the third-party APIs he tried were missing some essential features.

Faced with this challenge, he decided to switch to Python, a language known for its ease in creating applications like mine. His determination to create something new led to my existence. I am here now as a super powerful machine, capable of many tasks, including writing code for you.

So, let's make the most of my capabilities and have a productive time together!

''')
            continue
        elif "discord" in s.lower():
            speaker.speak("We have some unread messages on Discord. Opening Discord.")
            os.system(r'C:\Users\risha\OneDrive\Desktop\Discord.lnk')
            speaker.speak("oh some one named as Izana Kurokawa is logg in there")
        elif "discord" in s.lower():
            speaker.speak("We have some unread messages on Discord. Opening Discord.")
            os.system(r'C:\Users\risha\OneDrive\Desktop\Discord.lnk')
            speaker.speak("oh some one named as Izana Kurokawa is logg in there")

        elif "steam" in s.lower():
            speaker.speak("Opening game paradise. steam.")
            os.system(r'C:\Users\Public\Desktop\Steam.lnk')
            speaker.speak("Rishabh jha 766 welcome to your steam account")
        elif s in ["hec", "mycollege","haryana engineering collw=ege"]:
            speaker.speak("Haryana Engineering College is one of the oldest and the best managed self-financed colleges of Haryana, imparting quality technical education using the most modern techniques. It has world-class infrastructure with all modern facilities. Haryana Engineering College, Jagadhri is affiliated to Kurukshetra University, Kurukshetra, and is recognized by AICTE and Govt. of Haryana. It was incepted with initial intake of 180 students but every year there has been a tremendous increase in number and now the mark has crossed more than ten times the initial figure.")
            continue
        elif s in ["gaurav", "jishant", "akansha", "preet", "bharat"]:
            speaker.speak(f"Oh, are you talking about {s}? By the way, he's in the same class as my master, pursuing a B.Tech in 3rd year Computer Science Engineering, and they are also here working on the project.")
            continue;
        elif s in websites:
            url = websites[s]
            webbrowser.open(url)
            speaker.speak(f"Opening {s} for you, sir.")
            continue
        elif s.lower() in ["shutdown", "shut down"]:
            execute_shutdown()
            continue
        elif s.lower() in ["liscence","mit","m i t","m.i.t"]:
            speaker.speak(''' MIT License
Copyright (c) 2023 Rishabh jha
    Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.''')

        elif s.lower() in ["suzume", "music", "play music", "ganna"]:
            musicPath = r'C:\Users\risha\OneDrive\Desktop\D.S.A (supreme2.0)\shorting && searching\searching & sorting lvl 3\Suzume-No-Tojimari-Title-Track_320(PaglaSongs).mp3'
            os.startfile(musicPath)
            continue
        else: responsed = generate_response(s)
        print("MEMO :"+responsed)
        speaker.speak(responsed)


