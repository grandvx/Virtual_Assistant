import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3
import time
import speech_recognition as sr
import random
import threading
import pywhatkit
import datetime
import wikipedia
from wikipedia.exceptions import PageError
import pyjokes
import requests
import webbrowser
import smtplib


class AnimatedGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x600')

        # Create frames for the animation and buttons
        self.animation_frame = tk.Frame(self.master)
        self.button_frame = tk.Frame(self.master, bg='black')

        # Load images for the animation
        self.images = []
        for i in range(1, 335):
            image_path = f'D://recordings/InteractionHumanAndMachine/New folder/new_name_{i}.png'
            image = Image.open(image_path).convert('RGBA')
            self.images.append(ImageTk.PhotoImage(image))

        # Create a label to display the animation
        self.animation_label = tk.Label(self.animation_frame, image=self.images[0], bg='black')
        self.animation_label.pack()

        # Create buttons
        self.button1 = tk.Button(self.button_frame, text='Button 1', command=self.button1_function)
        self.button2 = tk.Button(self.button_frame, text='Button 2', command=self.button2_function)
        self.button3 = tk.Button(self.button_frame, text='Button 3', command=self.button3_function)
        self.button4 = tk.Button(self.button_frame, text='Button 4', command=self.button4_function)
        self.button5 = tk.Button(self.button_frame, text='Button 5', command=self.button5_function)
        self.button6 = tk.Button(self.button_frame, text='Button 6', command=self.button6_function)

        # Pack buttons
        self.button1.pack(side='left', padx=10, pady=0)
        self.button2.pack(side='left', padx=10, pady=0)
        self.button3.pack(side='left', padx=10, pady=0)
        self.button4.pack(side='left', padx=10, pady=0)
        self.button5.pack(side='left', padx=10, pady=0)
        self.button6.pack(side='left', padx=10, pady=0)

        # Pack frames
        self.button_frame.pack(side='bottom', fill='x')
        self.animation_frame.pack(fill='both', expand=True)
       
        # Start animation
        self.current_image = 0
        self.animate()

    def animate(self):
        self.animation_label.config(image=self.images[self.current_image])
        self.current_image = (self.current_image + 1) % len(self.images)
        self.master.after(20, self.animate)

    def button1_function(self):
        print('Button 1 was pressed!')

    def button2_function(self):
        print('Button 2 was pressed!')

    def button3_function(self):
        print('Button 3 was pressed!')

    def button4_function(self):
        print('Button 4 was pressed!')

    def button5_function(self):
        print('Button 5 was pressed!')

    def button6_function(self):
        print('Button 6 was pressed!')




#Variables-----------------------------------------------------------
r = sr.Recognizer()
keywords = [("pixel", 1e-20), ("Hey pixel", 1e-20), ] # Αρχικοποιούμε τις λέξης με τις οποίες θα μας ακούει
source = sr.Microphone() # Το μικρόφωνο που θα χρησιμοποιούμε
#Funtcions-----------------------------------------------------------
def Speak(text):
    rate = 150 #Ελέγχει την ταχύτητα που μιλάει ο personal assistant
    engine = pyttsx3.init() #Αρχικοποιεί την μηχανή για να μιλάει
    voices = engine.getProperty('voices') #ορίζει την ιδιότητες για την ομιλία
    engine.setProperty('voice', voices[1].id) # 0 για αντρική φωνή , 1 για γυναικεία
    engine.setProperty('rate', rate) # Προσαρμόζει την ταχύτητα της ομιλίας
    engine.say(text) # Λέει στην Python να μιλήσει τα περιεχόμενα του text
    engine.runAndWait() #Περιμένει να τελιώσει το πρόγραμμα την ομιλία και μετά συνεχίζει το πρόγραμμα

def send_email(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.

def callback(recognizer, audio):
    try:
        speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=keywords)
        print(speech_as_text)
        if "Pixel" in speech_as_text or "hey Pixel":
            Speak("Yes sir?")
            recognize_main()
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")

def start_recognizer():
    print("Waiting for a keyword...")
    r.listen_in_background(source, callback)
    time.sleep(1000000)

def recognize_main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        data = data.lower()
        print("You said: " + data)
        if "how are you" in data:
            Speak("I am Fine")
        elif "hello" in data:
            Speak("Hi there")
        elif 'play' in data:
            song = data.replace('play', '')
            Speak('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in data:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('Current time is ' + time)
            Speak('Current time is ' + time)
        elif 'who is' in data:
            person = data.replace('who is', '').strip()  # Replace 'who is' and strip extra spaces
            try:
                info = wikipedia.summary(person, sentences=2)
                print(info)
                Speak(info)
            except wikipedia.exceptions.PageError:
                print(f"Sorry, I couldn't find information about {person}.")
                Speak(f"Sorry, I couldn't find information about {person}.")
        elif 'joke' in data:
            Speak(pyjokes.get_joke()) 
            print(pyjokes.get_joke())
        elif "where is" in data:
            ind = data.lower().split().index("is")
            location = data.split()[ind + 1:]
            url = "https://www.google.com/maps/place/" + "".join(location)
            Speak =("This is where" + str(location) + " is.")
            webbrowser.open(url)
        elif 'bye-bye' in data:
            Speak("Goodbye!")
            stop_event.set()  # Set the stop event to stop the voice recognition loop
        elif 'weather' in data:
        # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
            api_key = 'f57394a82fbb2dedf23100a2b2e709d2'

        # Get the city name from user input (e.g., "What's the weather in Paris?")
            city = data.split('weather in ')[-1]

        # Define the URL for the weather API
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        # Make a GET request to the weather API
            response = requests.get(url)

            if response.status_code == 200:
                weather_data = response.json()
                # Extract relevant weather information from the API response
                main_weather = weather_data['weather'][0]['main']
                description = weather_data['weather'][0]['description']
                temperature = weather_data['main']['temp']
                temperature = round(temperature - 273.15, 2)  # Convert temperature to Celsius

                weather_message = f"The weather in {city} is {main_weather} ({description}) with a temperature of {temperature}°C."
                print(weather_message)
                Speak(weather_message)
            else:
                print("Could not fetch weather data. Please try again later.")
                Speak("Could not fetch weather data. Please try again later.")
        else:
            Speak("I'm sorry sir, I did not understand your request")
    except sr.UnknownValueError:
        print("Pixel did not understand your request")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def gui_thread():
    root = tk.Tk()
    app = AnimatedGUI(root)
    root.mainloop()

# Create a thread for voice recognition
def voice_recognition_thread():
    while not stop_event.is_set():  # Check if the stop event is not set
        start_recognizer()

# Create a threading.Event to signal when to stop the voice recognition
stop_event = threading.Event()

gui_thread = threading.Thread(target=gui_thread)
voice_recognition_thread = threading.Thread(target=voice_recognition_thread)

gui_thread.start()
voice_recognition_thread.start()

#gui_thread.join()
#voice_recognition_thread.join()