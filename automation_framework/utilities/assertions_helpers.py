class AssertionHelper:
    VALID_KEYS = {
        "coord": {"lon": None, "lat": None},
        "weather": {"id": None, "main": None, "description": None, "icon": None},
        "base": None,
        "main": {
            "temp": None,
            "feels_like": None,
            "temp_min": None,
            "temp_max": None,
            "pressure": None,
            "humidity": None,
        },
        "visibility": None,
        "wind": {"speed": None, "deg": None},
        "rain": {"1h": None},
        "clouds": {"all": None},
        "dt": None,
        "sys": {
            "country": None,
            "sunrise": None,
            "sunset": None,
        },
        "timezone": None,
        "id": None,
        "name": None,
        "cod": None,
    }

    @staticmethod
    def assert_keys(response):
        AssertionHelper._assert_keys(AssertionHelper.VALID_KEYS, response)

    @staticmethod
    def _assert_keys(valid_keys, response):
        for key in response:
            if isinstance(response[key], dict):
                AssertionHelper._assert_keys(response[key], valid_keys[key])
            else:
                if not key in valid_keys:
                    raise AssertionError(f"{key} is not exist in response", key)


# Usage:
# response = {
#     "coord": {"lon": -0.1257, "lat": 51.5085},
#     "weather": [
#         {"id": 500, "main": "Rain", "description": "light rain", "icon": "10d"}
#     ],
#     "base": "stations",
#     "main": {
#         "temp": 11.01,
#         "feels_like": 10.33,
#         "temp_min": 9.6,
#         "temp_max": 12.06,
#         "pressure": 984,
#         "humidity": 83,
#     },
#     "visibility": 10000,
#     "wind": {"speed": 3.09, "deg": 90},
#     "rain": {"1h": 0.95},
#     "clouds": {"all": 75},
#     "dt": 1711470264,
#     "sys": {
#         "type": 2,
#         "id": 2075535,
#         "country": "GB",
#         "sunrise": 1711432120,
#         "sunset": 1711477397,
#     },
#     "timezone": 0,
#     "id": 2643743,
#     "name": "London",
#     "cod": 200,
# }  # Your actual API response
# AssertionHelper.assert_keys(response)
