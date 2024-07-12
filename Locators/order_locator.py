from selenium.webdriver.common.by import By

class Order:
    ORDER_TOP = (By.XPATH,'//button[@class="Button_Button__ra12g"]') # Верхняя кнопка Заказа
    ORDER_BOTTOM = (By.XPATH,'(//button[contains(@class,"Button_Button")])[3]') # Нижняя кнопка Заказа
    NAME = (By.XPATH,'//input[@placeholder="* Имя"]') # Поле ввода имени
    SURNAME = (By.XPATH,'//input[@placeholder="* Фамилия"]') # Поле ввода фамилии
    ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')  # Поле ввода адреса
    METRO_STATION = (By.XPATH, '//input[@ class ="select-search__input"]')  # Поле выбора станции метро
    PHONE = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')  # Поле ввода телефона
    NEXT_BUTTON = (By.XPATH, '//button[contains(@class,"Button_Middle__1CSJM")]') # Кнопка далее

    DATE_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]') # Поле ввода даты
    RENT_PERIOD = (By.XPATH, '//div[@class="Dropdown-placeholder"]') # Поле выбора срока аренды

    COLOR_SCOOTER_1 = (By.ID, 'black') # Поле выбора цвета самоката
    COLOR_SCOOTER_2 = (By.ID, 'grey')  # Поле выбора цвета самоката

    COMMENTS = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')  # Поле ввода комментария для курьера
    CONFIRM_BUTTON = (By.XPATH,'(//button[contains(@class,"Button_Button")])[4]') # Нижняя кнопка Заказа
    CONFIRM_YES = (By.XPATH,'//button[contains(text(),"Да")]') # Кнопка подтверждения
    SUCCESS_POPUP = (By.XPATH,'//div[@class= "Order_ModalHeader__3FDaJ"]') # Заказ оформлен

    @staticmethod
    def metro_option_locator(metro_station):
        return (By.XPATH, f"//div[@class='select-search__select']//*[contains(text(), '{metro_station}')]")

    @staticmethod
    def period_option_locator(period):
        return (By.XPATH, f"//div[@class='Dropdown-menu']/div[text()='{period}']")