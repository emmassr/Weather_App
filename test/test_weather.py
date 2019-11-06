from lib.weather import Weather
time_stamp = 1572970803
weather = Weather()

def test_gets_forecast_when_given_location():
    latitude = "51.50722"
    longitude = "-0.1275"
    assert weather.get_forecast(time_stamp,latitude,longitude) == "Partly Cloudy"

def test_gets_forecast_when_given_different_location():
    latitude = "52.48142"
    longitude = "-1.89983"
    assert weather.get_forecast(time_stamp,latitude,longitude) == "Mostly Cloudy"

def test_gets_longitude_latitude_from_city_name():
    city_name = "Birmingham"
    assert weather.get_latitude_and_longitude(city_name) == [-1.9,52.48333]

def test_gets_weather_summary_from_city_name():
    city_name_1 = "Birmingham"
    city_name_2 = "London"
    assert weather.get_weather_summary(time_stamp,city_name_1) == "Mostly Cloudy"
    assert weather.get_weather_summary(time_stamp,city_name_2) == "Partly Cloudy"
