from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')  # Load secret key from environment variable

# Load API key from environment variable
API_KEY = os.getenv('API_KEY')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

cities = ['Miami', 'Orlando', 'Tampa', 'Jacksonville', 'Tallahassee']

def get_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def celsius_to_fahrenheit(celsius):
    return round(celsius * 9/5 + 32, 1)

def generate_humorous_text(temp_f, description):
    humor_text = ""
    if temp_f <= 32:
        humor_text += "Brrr! It's freezing! "
    elif 32 < temp_f <= 60:
        humor_text += "Chilly, isn't it? "
    elif 60 < temp_f <= 80:
        humor_text += "Nice and comfy weather! "
    else:
        humor_text += "It's hot! Get your sunscreen! "

    if "rain" in description:
        humor_text += "Don't forget your umbrella."
    elif "snow" in description:
        humor_text += "Snowball fight, anyone?"
    elif "clear" in description:
        humor_text += "Perfect day for a picnic."
    elif "cloud" in description:
        humor_text += "Cloudy skies, but still a good day."

    return humor_text

@app.route('/')
def index():
    weather_data = []
    for city in cities:
        data = get_weather_data(city)
        if data.get('cod') == 200:
            temp_f = celsius_to_fahrenheit(data['main']['temp'])
            description = data['weather'][0]['description']
            weather = {
                'city': city,
                'temperature': temp_f,
                'description': description,
                'icon': data['weather'][0]['icon'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'country': data['sys']['country'],
                'humor_text': generate_humorous_text(temp_f, description)
            }
            weather_data.append(weather)
        else:
            flash(f"City '{city}' not found. Error: {data.get('message', 'Unknown error')}", 'danger')
            cities.remove(city)
    return render_template('index.html', weather_data=weather_data)

@app.route('/add', methods=['POST'])
def add_city():
    city = request.form.get('city')
    if city and city not in cities:
        cities.append(city)
    return redirect(url_for('index'))

@app.route('/remove/<city>')
def remove_city(city):
    if city in cities:
        cities.remove(city)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
