from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MaimPage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_located(self, locator, time=20):
        try:
            return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f'Not found {locator}')
        except Exception as e:
            raise Exception(f'Error finding element by {locator}: {str(e)}')

    def find_element_clickable(self, locator, time=20):
        try:
            return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f'Element not clickable: {locator}')
        except Exception as e:
            raise Exception(f'Error finding clickable element by {locator}: {str(e)}')
