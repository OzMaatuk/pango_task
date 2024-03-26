from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

SEARCH_BAR_XPATH="/html/body/div[5]/header/div[2]/div/form/input"
TEMP_LABEL_XPATH="/html/body/div[5]/main/article/section[2]/div[1]/div[1]/div/table/tbody/tr[3]/td[1]"

class TemperatureExtractor:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def get_temperature(self, city):
        self.driver.get('https://www.timeanddate.com/weather/')

        try:
            # Wait for search box and type city
            search_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, SEARCH_BAR_XPATH)))
            search_box.send_keys(city)
            search_box.submit()

            # Wait for temperature element (replace with more specific selector if possible)
            temperature_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, TEMP_LABEL_XPATH)))
            return temperature_element.text
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error extracting temperature: {e}")
            return None

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
