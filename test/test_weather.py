from lib.weather import Weather
def test_gets_forecast_when_given_location():
    weather = Weather()
    assert weather.get_forecast("51.528308","-0.3817826") == "Cloudy"

def test_gets_forecast_when_given_different_location():
    weather = Weather()
    assert weather.get_forecast("52.48142","-1.89983") == "Sunny"

def test_gets_longitude_latitude_from_city_name():
    weather = Weather()
    assert weather.get_latitude_and_longitude("Birmingham") == [-1.9,52.48333]
