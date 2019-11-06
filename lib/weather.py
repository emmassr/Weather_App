import requests
import os


class Weather(object):

    def get_weather_summary(self, time_stamp, city_name):
        #[longitude, latitude] = [-1.9,52.48333]
        [longitude, latitude] = self.get_latitude_and_longitude(city_name)
        forecast_summary = self.get_forecast(time_stamp,latitude,longitude)
        return forecast_summary

    def get_forecast(self, time_stamp, latitude, longitude):
        darksky_response = requests.get(f"https://api.darksky.net/forecast/{os.environ['DARK_SKY_API_KEY']}/{latitude},{longitude},{time_stamp}?exclude=[minutely,hourly,daily,alerts,flags]")
        return darksky_response.json()["currently"]["summary"]


    def get_latitude_and_longitude(self, city_name):
        mapbox_response = requests.get(f"https://api.mapbox.com/geocoding/v5/mapbox.places/{city_name}.json?access_token={os.environ['MAPBOX_API_KEY']}")
        return mapbox_response.json()["features"][0]["center"]
