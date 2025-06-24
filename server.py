from flask import Flask, render_template, request, redirect, url_for
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
@app.route('/weather', methods=["GET", "POST"])
def get_weather():
    
    if request.method == 'POST':
        city = request.form.get('city', '')
    
        # Check for empty strings/spaces
        if not city.strip():
            city = "Princeton Junction"
        return redirect(url_for('get_weather', city=city))
    
    city = request.args.get('city')
    # Check for empty strings/spaces
    if not city.strip():
        return redirect(url_for('index'))
    
    weather_data = get_current_weather(city)
    
    # City is not found by API data
    if weather_data['cod'] != 200:
        return render_template('city-not-found.html')
        


    
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