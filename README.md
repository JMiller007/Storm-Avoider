# Storm-Avoider

Avoid Storms with this weather application. Never again have to run through the rain!

## About

Storm-Avoider is a fun and functional weather application that helps you check the current weather conditions and forecasts for your favorite cities. It uses the OpenWeatherMap API to fetch real-time weather data.

## Features

- **Real-time Weather Data**: Get up-to-date weather information for your selected cities.
- **Modern Dark Theme**: Stylish and easy on the eyes, perfect for night-time browsing.
- **Grid Layout**: View weather information in a neat grid format.
- **Pre-populated with Major Florida Cities**: Start with weather info for Miami, Orlando, Tampa, Jacksonville, and Tallahassee.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/JMiller007/Storm-Avoider.git
   cd Storm-Avoider
   ```

2. **Set Up a Virtual Environment**:

   - On macOS and Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv venv
     venv\\Scripts\\activate
     ```

3. **Install Dependencies**:

   ```bash
   pip install Flask requests python-dotenv
   ```

4. **Set Up Your API Key**:
   - Sign up on [OpenWeatherMap](https://openweathermap.org/) and get your API key.
   - Create a `.env` file in the root directory of the project and add your API key:
     ```
     SECRET_KEY=your_secret_key
     API_KEY=your_openweather_api_key
     ```

## Usage

1. **Run the Application**:

   ```bash
   python app.py
   ```

2. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:5000/` to start using Storm-Avoider.

3. **Add Cities**:
   - Use the form to add more cities to your weather dashboard.
   - Remove cities by clicking the "Remove" button next to each city's weather card.

## Technology Stack

- **Flask**: For the web framework.
- **Requests**: To handle API requests.
- **Bootstrap**: For modern UI elements.
- **Weather Icons**: For engaging weather icons.
- **Python-dotenv**: To manage environment variables.

## Have Fun!
