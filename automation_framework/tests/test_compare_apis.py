import pytest
from automation_framework.utilities.api_helpers import ApiHelper
from automation_framework.utilities.db_helpers import DatabaseHelper
from automation_framework.utilities.selenium_helpers import TemperatureExtractor
import json, random

@pytest.fixture(scope="module")
def api():
    return ApiHelper()

@pytest.fixture(scope="module")
def db():
    return DatabaseHelper()

@pytest.fixture(scope="module")
def add_column(db):
    return DatabaseHelper.add_column(db,"other")

@pytest.fixture(scope="module")
def output_file():
    return open("report.txt", 'w')

@pytest.fixture(scope="module")
def temperature_extractor():
    return TemperatureExtractor()




# - Execute a comparative temperature analysis for a minimum of 100 cities using data from both (https://www.timeanddate.com/weather/) and the [OpenWeatherMap API](https://openweathermap.org/current).
countries_list=random.sample(json.load(open('city.list.300.json', 'r', encoding='latin1')), 10)
print(countries_list)

@pytest.mark.parametrize("city", countries_list)
def test_compare_apis(city, api, db, add_column, output_file, temperature_extractor):
    # - Identify a relevant API to acquire city names for testing.
    # Wanted to use the 'openweathermap.org/geo/1.0/direct' API, but it was useless.

    res = ApiHelper.get_current_weather_celsius(api, city)
    assert(res.status_code == 200)
    data=res.json()    
    temp=data['main']['temp']
    feels=data['main']['feels_like']

    DatabaseHelper.insert_weather_data(db, city, temp, feels)

    # - Employ Selenium to extract temperature data from the specified website.
    temperature = temperature_extractor.get_temperature(city)
    temperature = temperature[:-3]

    # - Ensure continuity by utilizing the same database from previous questions.   
    DatabaseHelper.update_weather_data(db, city, 'other', temperature)

    # - generate report highlighting cities with temperature differences.
    if (temp != temperature):
        output_file.write(f"For city {city}, OpenWeatherMap was: {temp}, while timeanddate was {temperature}\n")
