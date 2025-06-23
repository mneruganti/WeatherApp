from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# Load API key from .env file
load_dotenv()

def get_current_weather(city="West Windsor"):
    
    # The URL can be found on the weather app docs.
    # We use os.getenv('API_KEY') to grab the key from your env folder
    # &q stands for queries and grabs the given city parameter
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    
    # This actually fetches the data from the url and converts it to JSON data
    weather_data = requests.get(request_url).json()
    
    # return this data
    return weather_data


if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***\n")
    
    city = input("\n Please Enter a City Name: ")
    
    weather_data = get_current_weather(city)
    
    print("\n")
    pprint(weather_data)
