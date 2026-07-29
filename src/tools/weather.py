"""
Weather tool.

This module retrieves the current temperature for a city
using the Open-Meteo API.
"""

import requests

GEOCODING_API_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"


def weather(city):
    """
    Retrieve the current temperature for a city.

    Args:
        city:
            Name of the city.

    Returns:
        A dictionary containing the weather information
        or an error message.
    """

    city = city.lower()
    
    try:

        city_url = (
            f"{GEOCODING_API_URL}"
            f"?name={city}"
            f"&countryCode=IN"
            f"&count=1"
        )

        city_response = requests.get(city_url)
        city_data = city_response.json()

        if "results" not in city_data:
            return {
                "success": False,
                "error": f"City '{city}' not found."
            }

        latitude = city_data["results"][0]["latitude"]
        longitude = city_data["results"][0]["longitude"]

        temp_url = (
            f"{WEATHER_API_URL}"
            f"?latitude={latitude}"
            f"&longitude={longitude}"
            f"&current=temperature_2m"
        )

        temp_response = requests.get(temp_url)
        temp_data = temp_response.json()

        temperature = temp_data["current"]["temperature_2m"]

        return {
            "success": True,
            "city": city,
            "temperature": temperature
        }

    except Exception as error:

        return {
            "success": False,
            "error": str(error)
        }