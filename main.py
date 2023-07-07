import datetime
import os
import smtplib
import subprocess
import webbrowser
import time
import pyjokes
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import wikipedia
from googletrans import Translator

# from nltk.sentiment import SentimentIntensityAnalyzer
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer

# with open("data.yaml") as f:
#     data = yaml.load(f, Loader=yaml.FullLoader)

# Use the data in the file.


# initialize recognizer
listener = sr.Recognizer()
# initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    # tokens = nltk.word_tokenize(text)
    print(text)
    engine.say(text)
    engine.runAndWait()


# use the microphone as the source for audio
# def take_command():
#     try:
#         with sr.Microphone() as source:
#             print("Listening...")
#             listener.adjust_for_ambient_noise(source)
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             print(command)
#         return command.lower()
#
#     except sr.UnknownValueError:
#         return ""
#
#     except sr.RequestError:
#         return ""

def take_command():
    """Returns a string of the user's command."""

    # Get the user's input.
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = listener.listen(source)
            command = listener.recognize_google(audio, language='en')
            command = command.lower()
            # if 'rivi' in command:
            #     command = command.replace('alexa', '')
            return command
    except Exception as e:
        print(e)
        print("I didn't understand that. Please try again.")
        return None


def greet():
    """Greets the user and asks how they can help.

  Returns:
    A string containing the greeting.
  """

    # Get the current time.
    now = datetime.datetime.now()

    hour = now.hour

    if 6 <= hour < 12:
        talk("Hey ! Good morning! Thanks for Using Me, Iam a voice bot Rivi by NEXTs")
    elif 12 <= hour < 18:
        talk(" Hey ! Good afternoon! Thanks for Using Me, Iam a voice bot Rivi by NEXTs")
    else:
        talk("Hey ! Good Morning! Thanks for Using Me, Iam a voice bot 'Rivi' by NEXTs")


#
# def process_text(text):
#     # Tokenize the text into individual words
#     tokens = word_tokenize(text)
#
#     # Remove stopwords from the text
#     stop_words = set(stopwords.words('english'))
#     filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
#
#     # Lemmatize the filtered tokens
#     lemmatizer = WordNetLemmatizer()
#     lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
#
#     # Return the processed text as a string
#     return ' '.join(lemmatized_tokens)


# def analyze_sentiment(text):
#     sia = SentimentIntensityAnalyzer()
#     sentiment_scores = sia.polarity_scores(text)
#     return sentiment_scores
#

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('prakash72716@gmail.com', ' password here')
    server.sendmail('prakash72716@gmail.com', to, content)
    server.close()


def run_rivi():
    # Greet the user.
    greet()
    while True:
        # get user input
        user_input = input("You: ").lower()
        # user_input = input("You: ").lower() and take_command()
        # processed_input = process_text(user_input)
        # sentiment_scores = analyze_sentiment(processed_input)

        # if "change my name to" in user_input:
        #     user_input = user_input.replace("change my name to", "")
        #     talk(user_input)

        if 'hi' or 'hello' or 'hey' in user_input:
            print('Hey Nice to see you ,what can i do')

        elif 'write a c program' in user_input:
            print('Sorry Thats your Fate')

        elif "change name" in user_input:
            print("What would you like to call me, Sir ")
            user_input = input[talk("Thanks for naming me")]

        elif "is your name" in user_input:
            print("My friends call me rivi")

        # If the user says "play", play a song.
        elif "play" in user_input:
            song = input(talk("What song would you like to play?\n"))
            pywhatkit.playonyt(song)

        elif 'time' in user_input:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('Current time is ' + time)

        # elif 'what is love' or 'what about love' or 'who is your love' in user_input:
        #     talk("It is 7th sense that destroy all other senses")

        elif "are you" in user_input:
            print("I am your virtual assistant created by NEXTs")

        elif "i have exam today" or 'about exams' in user_input:
            talk('Rest in peace bro')

        elif 'reason for you' or 'why are you here' in user_input:
            talk("I was created as a Minor project by company NEXTs ")

        elif 'date' in user_input:
            date = datetime.date.today().strftime('%B %d, %Y')
            talk('Today is ' + date)

        elif "camera" in user_input or "take a photo" in user_input:
            ec.capture(0, "rivi Cam-1", "img.jpg")

        # elif 'wikipedia' or 'what is' or 'who is' in user_input:
        #     query = user_input.replace('wikipedia', '')
        #     info = wikipedia.summary(query, 2)
        #     talk(info)

        elif 'search' in user_input:
            query = user_input.replace('search', '')
            pywhatkit.search(query)
            print('Here are the search results for ' + query)

        elif 'open brave' in user_input:
            talk('Opening brave...')
            path = r"C:\Users\PRAKASH R\Downloads\BraveBrowserSetup-BRV011"
            os.startfile(path)

        elif 'open edge' in user_input:
            talk('Opening edge...')
            path = r"C:\Users\PRAKASH R\Downloads\BraveBrowserSetup-BRV011"
            os.startfile(path)

        elif 'open google' in user_input:
            talk('Opening google...')
            webbrowser.open_new_tab("www.google.com")
        elif 'joke' in user_input:
            talk(pyjokes.get_joke())

        elif 'not a joke' in user_input:
            talk('hey I have anther one for you...')
            talk(pyjokes.get_joke())

        # If the user says "who the heck is", look up a person on Wikipedia.
        elif user_input.startswith("who the heck is"):
            person = user_input.replace("who the heck is", "")
            info = wikipedia.summary(person, 1)
            print(info)

        elif 'shutdown' in user_input:
            talk('Shutting down')
            os.system('shutdown /s /t 1')

        elif 'restart' in user_input:
            talk('Restarting')
            os.system('shutdown /r /t 1')

        elif 'log off' in user_input:
            talk('Logging off')
            subprocess.call(["shutdown", "/l"])

        elif 'stop listening' in user_input:
            print(talk('Goodbye!'))
            return False

        elif 'send a mail' in user_input:
            try:
                talk("What should I say?")
                content = user_input
                talk("whome should i send")
                to = input()
                sendEmail(to, content)
                talk("Email has been sent !")
            except Exception as e:
                print(e)
                talk("I am not able to send this email")

        elif "who are you" in user_input or "define yourself" in user_input:
            print("Hello, I am Rivi. Your Assistant. I am here to make your life easier. You can command me to "
                  "perform various tasks such as asking questions or opening applications etcetera")
            talk("Hello, I am Rivi. Your Assistant. I am here to make your life easier. You can command me to "
                 "perform various tasks such as asking questions or opening applications etcetera")

        elif "made you" in user_input or "created you" in user_input:
            talk("I was created by Mr.Prakash")

        elif "your name" in user_input:
            talk("My name is Assistant")

        elif "who am i" in user_input:
            talk("You must probably be a human")

        elif "why do you exist" in user_input or "why did you come to this word" in user_input:
            talk("It is a secret")

        elif "how are you" in user_input:
            talk("I am awesome, Thank you")
            talk("\nHow are you?")

        elif "fine" in user_input or "good" in user_input:
            talk("It's good to know that your fine")

        # elif 'hi' or 'hey' or 'rivi' in user_input:
        #     talk('Hey Good to see you ! How are you man')

        elif "weather" in user_input:

            # get API key from OpenWeatherMap

            api_key = "your_api_key_here"

            # set the OpenWeatherMap API endpoint

            api_endpoint = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

            # get the city name from user input

            city_name = user_input.split(" ")[-1]

            # send a GET request to the OpenWeatherMap API endpoint for the specified city

            response = requests.get(api_endpoint.format(city_name, api_key))

            # if the response status code is OK, parse the response and get the weather information

            if response.status_code == 200:

                data = response.json()

                weather_description = data['weather'][0]['description']

                temperature = round(float(data['main']['temp']) - 273.15, 2)

                feels_like = round(float(data['main']['feels_like']) - 273.15, 2)

                humidity = data['main']['humidity']

                wind_speed = data['wind']['speed']

                talk(
                    f"Currently in {city_name} the temperature is {temperature} degrees Celsius, feels like {feels_like} "

                    f"degrees Celsius, the humidity is {humidity} percent, and the wind speed is {wind_speed} meters per second. "

                    f"The weather description is {weather_description}")

            else:

                talk(f"Sorry, I couldn't find weather information for {city_name}")

        elif "translate" in user_input:

            # get the text to translate and the target language from user input

            text_to_translate = user_input.split(" ")[-2]

            target_language = user_input.split(" ")[-1]

            # initialize the Translator object

            translator = Translator()

            # translate the text to the target language

            translation = translator.translate(text_to_translate, dest=target_language)

            # speak the translation

            talk(f"The translation of {text_to_translate} to {target_language} is {translation.text}")

        elif "analyze sentiment" in user_input:

            # get the text to analyze sentiment from user input

            text_to_analyze = user_input.split(" ")[-1]

            # analyze the sentiment of the text

            sentiment_scores = analyze_sentiment(text_to_analyze)

            # print the sentiment scores

            print(f"Positive: {sentiment_scores['pos']}, Negative: {sentiment_scores['neg']}, "

                  f"Neutral: {sentiment_scores['neu']}, Compound: {sentiment_scores['compound']}")

            # speak the sentiment scores

            talk(f"The sentiment scores of {text_to_analyze} are as follows: "

                 f"Positive: {sentiment_scores['pos']}, Negative: {sentiment_scores['neg']}, "

                 f"Neutral: {sentiment_scores['neu']}, Compound: {sentiment_scores['compound']}")

        elif 'news' in user_input:

            # NewsAPI

            url = "https://newsapi.org/v2/top-headlines"

            params = {
                "country": "in",
                "apiKey": "07d6ce5dedd74bdbae26cf1d2bceff00"
            }

            response = requests.get(url, params=params)

            articles = response.json()["articles"]

            news_titles = "Here are the latest news headlines: "

            for article in articles:
                news_titles += article["title"] + ". "
            talk(news_titles)

        elif 'stock' in user_input:
            # Alpha Vantage
            url = "https://www.alphavantage.co/query"
            params = {
                "function": "TIME_SERIES_DAILY_ADJUSTED",
                "symbol": "AAPL",
                "apikey": "DFA8FR2GEI41W2AM"
            }
            response = requests.get(url, params=params)
            data = response.json()["Time Series (Daily)"]
            latest_data = list(data.items())[0][1]
            print(f"Open: {latest_data['1. open']}")
            print(f"High: {latest_data['2. high']}")
            print(f"Low: {latest_data['3. low']}")
            print(f"Close: {latest_data['4. close']}")

        # elif 'exit' or 'goodbye' or 'bye' or 'quit' in user_input:
        #     # If the user wants to exit, thank them and exit the program.
        #     print("Thank you for using Rivi! I hope you have a great day.")
        #     exit()
        elif 'exit' or 'bye' or 'goodbye' in user_input:
            print('Ok sir    Goodbye, take care')
            exit()

        else:
            talk("Sorry, I don't understand what you're asking for ?")


while True:
    try:
        run_rivi()
    except KeyboardInterrupt:
        print('\nProgram interrupted by user. Continuing...')
        talk('Is there anything else I can help you with?')

if __name__ == "__main__":
    run_rivi()
