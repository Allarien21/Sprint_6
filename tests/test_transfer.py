import allure

from Locators.order_locator import Order
from pages.transfer_page import TransferPage


class TestTransfer:
    @allure.title('Тест проверки логотипа Самоката')
    @allure.description('Проверяется что, если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')
    def test_navigation_to_scooter_homepage(self, driver):
        page = TransferPage(driver)
        page.data_input_click_order(Order.ORDER_TOP)
        page.click_scooter_logo()
        assert page.get_current_url() == "https://qa-scooter.praktikum-services.ru/"


    @allure.title('Тест проверки логотипа Яндекса')
    @allure.description('Проверяется что, если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена')
    def test_navigation_to_yandex_zen(self, driver):
        page = TransferPage(driver)
        page.click_yandex_logo()
        assert "dzen.ru" in page.get_current_url()