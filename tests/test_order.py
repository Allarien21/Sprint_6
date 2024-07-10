import allure

import pytest

from Locators.Order import Order
from pages.order_page import OrderPage


class TestOrder:

    order_data = [
        {
            "name": "Иван",
            "surname": "Иванов",
            "address": "ул. Пушкина, д. 1",
            "metro_station": "Пушкинская",
            "phone": "+79991234567",
            "date": "12.12.2024",
            "period": "сутки",
            "color": "black",
            "comment": "Позвонить за час до доставки",
        },
        {
            "name": "Петр",
            "surname": "Петров",
            "address": "ул. Лермонтова, д. 5",
            "metro_station": "Лермонтовский проспект",
            "phone": "+79998765432",
            "date": "13.12.2024",
            "period": "двое суток",
            "color": "grey",
            "comment": "Оставить у двери",
        }
    ]

    @allure.title('Тест оформление заказа через кнопку заказать в хедере')
    @allure.description('На странице ищем элемент "Заказать" и проверяем оформление заказа самоката')
    @pytest.mark.parametrize("data", order_data)
    def test_order_top(self, driver, data):
        page = OrderPage(driver)

        page.data_input_click_order_top(Order.ORDER_TOP)

        page.fill_order_form(
            data["name"],
            data["surname"],
            data["address"],
            data["metro_station"],
            data["phone"]
        )
        page.fill_second_page_form(
            data["date"],
            data["period"],
            data["color"],
            data["comment"]
        )
        page.confirm_order()
        assert page.check_success_popup()

    @allure.title('Тест оформление заказа через кнопку заказать в нижнюю')
    @allure.description('На странице ищем элемент "Заказать" и проверяем оформление заказа самоката')
    @pytest.mark.parametrize("data", order_data)
    def test_order_bottom(self, driver, data):
        page = OrderPage(driver)

        page.data_input_click_order_bottom(Order.ORDER_BOTTOM)

        page.fill_order_form(
            data["name"],
            data["surname"],
            data["address"],
            data["metro_station"],
            data["phone"]
        )
        page.fill_second_page_form(
            data["date"],
            data["period"],
            data["color"],
            data["comment"]
        )
        page.confirm_order()
        assert page.check_success_popup()

    @allure.title('Тест проверки логотипа Самоката')
    @allure.description('Проверяется что, если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')
    def test_navigation_to_scooter_homepage(self, driver):
        page = OrderPage(driver)
        page.data_input_click_order_top(Order.ORDER_TOP)
        page.click_scooter_logo()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title('Тест проверки логотипа Яндекса')
    @allure.description('Проверяется что, если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена')
    def test_navigation_to_yandex_zen(self, driver):
        page = OrderPage(driver)
        page.click_yandex_logo()
        assert "dzen.ru" in driver.current_url