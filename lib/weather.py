import requests
import os


class Weather(object):
    """docstring for Numbers."""

    def get_forecast(self, latitude, longitude):
        darksky_response = requests.get(f"https://api.darksky.net/forecast/{os.environ['DARK_SKY_API_KEY']}/{latitude},{longitude}?exclude=[minutely,hourly,daily,alerts,flags]")
        return darksky_response.json()["currently"]["summary"]


    def get_latitude_and_longitude(self, city_name):
        mapbox_response = requests.get(f"https://api.mapbox.com/geocoding/v5/mapbox.places/{city_name}.json?access_token={os.environ['MAPBOX_API_KEY']}")
        return mapbox_response.json()["features"][0]["center"]
