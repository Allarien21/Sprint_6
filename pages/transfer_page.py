import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Locators.main_locator import Main
from pages.base_page import BasePage

class Transfer(BasePage):
    @allure.step('Нажимаем на копку  {locator}')
    def data_input_click_order(self, locator):
        self.find_element_located(locator).click()
    @allure.step('Нажатие на логотип Самоката')
    def click_scooter_logo(self):
        self.find_element_located(Main.SCOOTER_LOLO).click()


    @allure.step('Нажатие на логотип Яндекса')
    def click_yandex_logo(self):
        self.find_element_located(Main.YA_LOLO).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_contains("dzen.ru"))

    def get_current_url(self):
        return self.driver.current_url