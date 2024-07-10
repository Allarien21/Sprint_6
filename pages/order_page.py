import allure

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Locators.Main import Main
from Locators.Order import Order
from pages.main_page import MaimPage


class OrderPage(MaimPage):
    @allure.step('Нажимаем на копку  {locator}')
    def data_input_click_order_top(self, locator):
        self.find_element_located(locator).click()

    @allure.step('Нажимаем на копку  {locator}')
    def data_input_click_order_bottom(self, locator, time=20):
        button = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.find_element_clickable(locator).click()

    @allure.step('Шаги заполнения первой страницы заказа')
    def fill_order_form(self, name, surname, address, metro_station, phone):
        self.find_element_located(Order.NAME).send_keys(name)
        self.find_element_located(Order.SURNAME).send_keys(surname)
        self.find_element_located(Order.ADDRESS).send_keys(address)

        metro_field = self.find_element_located(Order.METRO_STATION)
        metro_field.click()
        metro_field.send_keys(metro_station)

        metro_option_locator = (By.XPATH, f"//div[@class='select-search__select']//*[contains(text(), '{metro_station}')]")
        self.find_element_located(metro_option_locator).click()

        self.find_element_located(Order.PHONE).send_keys(phone)
        self.find_element_located(Order.NEXT_BUTTON).click()

    @allure.step('Шаги заполнения второй страницы заказа')
    def fill_second_page_form(self, date, period, color, comment):
        date_field = self.find_element_located(Order.DATE_FIELD)
        date_field.click()
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)
        self.find_element_located(Order.RENT_PERIOD).click()
        period_option = f"//div[@class='Dropdown-menu']/div[text()='{period}']"
        self.find_element_located((By.XPATH, period_option)).click()
        color_locator = Order.COLOR_SCOOTER_1 if color == "black" else Order.COLOR_SCOOTER_2
        self.find_element_located(color_locator).click()
        self.find_element_located(Order.COMMENTS).send_keys(comment)

    @allure.step('Шаги подтверждения заказа')
    def confirm_order(self):
        self.find_element_located(Order.CONFIRM_BUTTON).click()
        self.find_element_located(Order.CONFIRM_YES).click()

    @allure.step('Всплывающее окно успешного оформления заказа')
    def check_success_popup(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((Order.SUCCESS_POPUP)))

    @allure.step('Нажатие на логотип Самоката')
    def click_scooter_logo(self):
        self.find_element_located(Main.SCOOTER_LOLO).click()

    @allure.step('Нажатие на логотип Яндекса')
    def click_yandex_logo(self):
        self.find_element_located(Main.YA_LOLO).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_contains("dzen.ru"))

