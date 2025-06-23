from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

# THis line is what makes it a Flask app
app = Flask(__name__)

# Routes

# This is the home route
@app.route('/')
@app.route('/index')

# The route has to return something
def index():
    return render_template('index.html')

# This is the route for actually displaying the weather
@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    weather_data = get_current_weather(city)

    
    # The information to create this template can be accessed by seeing what JSON object is returned
    # by the get_current_weather() function
    # The variables being rendered in the template will be used in the weather.html template
    return render_template(
        "weather.html",
        title = weather_data["name"],
        status = weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)