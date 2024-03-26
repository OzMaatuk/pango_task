import requests
from configparser import ConfigParser


class ApiHelper:
    configur = ConfigParser()
    configur.read('../config/config.ini') 
    API_KEY=configur.get('API', 'API_KEY')
    BASE_URL=configur.get('API', 'API_KEY')

    def get_current_weather(self, city):
        url = f"{self.BASE_URL}?q={city}&appid={self.API_KEY}"
        print(url)
        response = requests.get(url)
        print(response)
        return response

    def get_weather_data(self, city_id):
            url = f"{self.BASE_URL}?id={city_id}&appid={self.API_KEY}"
            print(url)
            response = requests.get(url)
            print(response)
            return response