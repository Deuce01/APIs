import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Replace with your OpenWeatherMap API Key
API_KEY = "your_openweather_api_key"

# Endpoint to fetch weather data
@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City name is required"}), 400

    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(weather_url)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch weather data"}), response.status_code

    weather_data = response.json()
    simplified_data = {
        "city": weather_data['name'],
        "temperature": weather_data['main']['temp'],
        "description": weather_data['weather'][0]['description'],
        "humidity": weather_data['main']['humidity'],
        "wind_speed": weather_data['wind']['speed']
    }
    return jsonify(simplified_data), 200

if __name__ == '__main__':
    app.run(debug=True)
