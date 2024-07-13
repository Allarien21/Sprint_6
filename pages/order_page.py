import allure

from selenium.webdriver import Keys

from Locators.order_locator import Order
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Нажимаем на копку  {locator}')
    def data_input_click_order_top(self, locator):
        self.find_element_located(locator).click()

    @allure.step('Нажимаем на копку  {locator}')
    def data_input_click_order_bottom(self, locator):
        self.scroll_to_view(locator)
        self.find_element_clickable(locator).click()

    @allure.step('Шаги заполнения первой страницы заказа')
    def fill_order_form(self, name, surname, address, metro_station, phone):
        self.find_element_located(Order.NAME).send_keys(name)
        self.find_element_located(Order.SURNAME).send_keys(surname)
        self.find_element_located(Order.ADDRESS).send_keys(address)

        metro_field = self.find_element_located(Order.METRO_STATION)
        metro_field.click()
        metro_field.send_keys(metro_station)
        metro_option_locator = Order.metro_option_locator(metro_station)
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
        period_option = Order.period_option_locator(period)
        self.find_element_located(period_option).click()

        color_locator = Order.COLOR_SCOOTER_1 if color == "black" else Order.COLOR_SCOOTER_2
        self.find_element_located(color_locator).click()
        self.find_element_located(Order.COMMENTS).send_keys(comment)

    @allure.step('Шаги подтверждения заказа')
    def confirm_order(self):
        self.find_element_located(Order.CONFIRM_BUTTON).click()
        self.find_element_located(Order.CONFIRM_YES).click()

    @allure.step('Всплывающее окно успешного оформления заказа')
    def check_success_popup(self):
        return self.presence_element_located(Order.SUCCESS_POPUP)

