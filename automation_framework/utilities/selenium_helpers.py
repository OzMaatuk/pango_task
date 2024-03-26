from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configparser import ConfigParser


class TemperatureExtractor:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        configur = ConfigParser()
        configur.read('automation_framework\\config\\config.ini') 
        BASE_URL=configur.get('API', 'BASE_URL')
        self.SEARCH_BAR_XPATH=configur.get('OTHER', 'SEARCH_BAR_XPATH')
        self.TEMP_LABEL_XPATH=configur.get('OTHER', 'TEMP_LABEL_XPATH')
        self.BASE_URL=configur.get('OTHER', 'BASE_URL')
        self.FIRST_ELEMENT_XPATH=configur.get('OTHER', 'FIRST_ELEMENT_XPATH')

    def get_temperature(self, city):
        self.driver.get(self.BASE_URL)

        # Wait for search box and type city
        search_box = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.SEARCH_BAR_XPATH)))
        search_box.send_keys(city)
        search_box.submit()
        
        search_first_element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.FIRST_ELEMENT_XPATH)))
        search_first_element.click()
        
        # Wait for temperature element (replace with more specific selector if possible)
        temperature_element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.TEMP_LABEL_XPATH)))
        print(temperature_element.text)
        return temperature_element.text

    def close(self):
        self.driver.quit()


# Usage:
# extractor = TemperatureExtractor()
# temperature = extractor.get_temperature('ness ziona')
# if temperature:
#     print(f"Temperature in Your City: {temperature}")
# else:
#     print("Temperature extraction failed.")
# extractor.close()
