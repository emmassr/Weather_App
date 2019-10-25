from lib.weather import Weather
def test_gets_forecast_when_given_location():
    weather = Weather()
    assert weather.get_forecast("London") == "Cloudy"
