from selenium.webdriver.common.by import By

class Transition:
    QUESTION_ONE = (By.ID, 'accordion__heading-0') # Вопрос 1
    QUESTION_TWO = (By.ID, 'accordion__heading-1') # Вопрос 2
    QUESTION_THREE = (By.ID, 'accordion__heading-2') # Вопрос 3
    QUESTION_FOUR = (By.ID, 'accordion__heading-3') # Вопрос 4
    QUESTION_FIVE = (By.ID, 'accordion__heading-4') # Вопрос 5
    QUESTION_SIX = (By.ID, 'accordion__heading-5') # Вопрос 6
    QUESTION_SEVEN = (By.ID, 'accordion__heading-6') # Вопрос 7
    QUESTION_EIGHT = (By.ID, 'accordion__heading-7') # Вопрос 8

    ANSWER_ONE = (By.XPATH, '//div[@id="accordion__panel-0"]/p[contains(text(), "Сутки — 400 рублей.")]') # Ответ 1
    ANSWER_TWO = (By.XPATH, '//div[@id="accordion__panel-1"]/p[contains(text(), "Пока что у нас так")]') # Ответ 2
    ANSWER_THREE = (By.XPATH, '//div[@id="accordion__panel-2"]/p[contains(text(), "Допустим, вы оформляете заказ на 8 мая")]') # Ответ 3
    ANSWER_FOUR = (By.XPATH, '//div[@id="accordion__panel-3"]/p[contains(text(), "Только начиная с завтрашнего дня.")]') # Ответ 4
    ANSWER_FIVE = (By.XPATH, '//div[@id="accordion__panel-4"]/p[contains(text(), "Пока что нет!")]') # Ответ 5
    ANSWER_SIX = (By.XPATH, '//div[@id="accordion__panel-5"]/p[contains(text(), "Самокат приезжает к вам")]') # Ответ 6
    ANSWER_SEVEN = (By.XPATH, '//div[@id="accordion__panel-6"]/p[contains(text(), "Да, пока самокат не привезли")]') # Ответ 7
    ANSWER_EIGHT = (By.XPATH, '//div[@id="accordion__panel-7"]/p[contains(text(), "Да, обязательно")]') # Ответ 8
