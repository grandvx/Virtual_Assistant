import tkinter as tk
import webbrowser
import requests

class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather App")
        self.master.geometry("300x300")

        self.weather_info_label = tk.Label(self.master, text="", font=("Arial", 14))
        self.weather_info_label.pack(pady=10)

        self.city_entry = tk.Entry(self.master)
        self.city_entry.pack(pady=5)

        self.get_weather_button = tk.Button(self.master, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack(pady=5)

        self.open_meteo_button = tk.Button(self.master, text="Open meteo.gr", command=self.open_meteo_gr)
        self.open_meteo_button.pack(pady=5)

    def get_weather(self):
        city = self.city_entry.get()
        api_key = "f57394a82fbb2dedf23100a2b2e709d2"  # Replace with your API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != "404":
            weather_desc = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            self.weather_info_label.config(text=f"Weather: {weather_desc}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s")
        else:
            self.weather_info_label.config(text="City not found")

    def open_meteo_gr(self):
        webbrowser.open("https://meteo.gr")

