import pytest
from automation_framework.utilities.api_helpers import ApiHelper
from automation_framework.utilities.db_helpers import DatabaseHelper
from automation_framework.utilities.assertions_helpers import AssertionHelper

@pytest.fixture(scope="module")
def api():
    return ApiHelper()

@pytest.fixture(scope="module")
def db():
    return DatabaseHelper()


@pytest.mark.parametrize("city", [
                                    ("london"),
                                    ("tel aviv"),
                                    ("ness ziona")
                                ])
def test_get_current_weather(city, api, db):
    DatabaseHelper.create_tables(db)
    res = ApiHelper.get_current_weather_celsius(api, city)

    # - Validate Status Code.
    assert(res.status_code == 200)
    data=res.json()
    # print(data)
    AssertionHelper.assert_keys(data)

    # - Insert temperature and feels_like responses for each city into the database.
    temp=data['main']['temp']
    feels=data['main']['feels_like']

    DatabaseHelper.insert_weather_data(db, city, temp, feels)

    # - Verify that temperature and feels_like from the database are equal to the API response.
    tpl=DatabaseHelper.get_weather_data(db, city)
    assert(tpl[0]==city)
    assert(tpl[1]==temp)
    assert(tpl[2]==feels)


@pytest.mark.parametrize("city_id", [
                                    ("2643743"),
                                    ("833"),
                                    ("2960"),
                                    ("3245"),
                                    ("2643743"),
                                    ("833"),
                                    ("2643743"),
                                ])
def test_get_weather_data_avarage(city_id, api, db):
    DatabaseHelper.create_tables(db)
    res = ApiHelper.get_current_weather_by_id(api, city_id)
    data=res.json()
    # print(data)
    temp=data['main']['temp']
    feels=data['main']['feels_like']
    AssertionHelper.assert_keys(data)
    
    # - Create a new database column for the average temperature of each city.
    DatabaseHelper.add_column(db,"avg")

    # - Insert temperature and feels_like responses for each city into the database.
    tpl=DatabaseHelper.get_weather_data(db, city_id)
    if (tpl == None):
        DatabaseHelper.insert_weather_data(db, city_id, temp, feels)
        DatabaseHelper.update_weather_data(db, city_id, "avg", temp)
    else:
        DatabaseHelper.update_weather_data(db, city_id, "temperature", temp)
        new_avg = (tpl[1] + temp)/2
        DatabaseHelper.update_weather_data(db, city_id, "avg", new_avg)

    # - Assert that the data inserted into the database is equal to the API response.
    tpl=DatabaseHelper.get_weather_data(db, city_id)
    assert(tpl[0]==city_id)
    assert(tpl[1]==temp)
    assert(tpl[2]==feels)

    # - Print the city with the highest average temperature.
    max_avg=DatabaseHelper.get_max_by_col(db, "avg")
    print("max_avg: " + str(max_avg))