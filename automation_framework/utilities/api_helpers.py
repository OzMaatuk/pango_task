import requests
from configparser import ConfigParser


class ApiHelper:
    configur = ConfigParser()
    configur.read('automation_framework\\config\\config.ini') 
    API_KEY=configur.get('API', 'API_KEY')
    BASE_URL=configur.get('API', 'BASE_URL')

    def get_weather(self, url):
        print(url)
        response = requests.get(url)
        print(response)
        return response

    def get_current_weather(self, city):
        url = f"{self.BASE_URL}?q={city}&appid={self.API_KEY}"
        return self.get_weather(url)

    def get_current_weather_celsius(self, city):
        url = f"{self.BASE_URL}?q={city}&appid={self.API_KEY}&units=metric"
        return self.get_weather(url)

    def get_current_weather_by_id(self, city_id):
        url = f"{self.BASE_URL}?id={city_id}&appid={self.API_KEY}"
        return self.get_weather(url)