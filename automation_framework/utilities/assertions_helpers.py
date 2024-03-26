class AssertionHelper:
    VALID_KEYS = {
        'coord': ['lon', 'lat'],
        'weather': [{'id': None, 'main': None, 'description': None, 'icon': None}],
        'base': None,
        'main': ['temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity'],
        'visibility': None,
        'wind': ['speed', 'deg'],
        'rain': ['1h'],
        'clouds': ['all'],
        'dt': None,
        'sys': ['type', 'id', 'country', 'sunrise', 'sunset'],
        'timezone': None,
        'id': None,
        'name': None,
        'cod': None
    }

    @staticmethod
    def assert_keys(response):
        AssertionHelper._assert_keys(AssertionHelper.VALID_KEYS, response)

    @staticmethod
    def _assert_keys(valid_keys, response):
        for key, subkeys in valid_keys.items():
            if key not in response:
                raise AssertionError(f"Missing key in the response: {key}")
            if isinstance(subkeys, list):
                for subkey in subkeys:
                    if isinstance(subkey, dict):
                        AssertionHelper._assert_keys(subkey, response[key][0])
                    else:
                        if subkey not in response[key][0]:
                            raise AssertionError(f"Missing key in the response: {subkey}")
            elif isinstance(subkeys, dict):
                AssertionHelper._assert_keys(subkeys, response[key])

# Usage:
# response = {...}  # Your actual API response
# AssertionHelper.assert_keys(response)
