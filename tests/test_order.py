import allure

import pytest

from Locators.order import Order
from pages.order_page import OrderPage
from Locators.data import order_data


class TestOrder:
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
