import allure
from Locators.Transition import Transition
from pages.transition_page import SearchQuestion


class TestTransition:
    @allure.title('Тест проверки выпадающего вопроса "Сколько это стоит? И как оплатить?"')
    @allure.description('Ищем элемент  с вопросом на странице, и проверяем выпажающий тест')
    def test_transition_for_questions_1(self,driver):
        search_question = SearchQuestion(driver)
        search_question.find_question(Transition.QUESTION_ONE)
        element = search_question.drop_down_text(Transition.ANSWER_ONE)
        assert element.text == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    @allure.title('Тест проверки выпадающего вопроса "Хочу сразу несколько самокатов! Так можно?"')
    @allure.description('Ищем элемент  с вопросом на странице, и проверяем выпажающий тест')
    def test_transition_for_questions_2(self,driver):
        search_question = SearchQuestion(driver)
        search_question.find_question(Transition.QUESTION_TWO)
        element = search_question.drop_down_text(Transition.ANSWER_TWO)
        assert element.text == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

    @allure.title('Тест проверки выпадающего вопроса "Как рассчитывается время аренды?"')
    @allure.description('Ищем элемент  с вопросом на странице, и проверяем выпажающий тест')
    def test_transition_for_questions_3(self,driver):
        search_question = SearchQuestion(driver)
        search_question.find_question(Transition.QUESTION_THREE)
        element = search_question.drop_down_text(Transition.ANSWER_THREE)
        assert element.text == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    @allure.title('Тест проверки выпадающего вопроса "Можно ли заказать самокат прямо на сегодня?"')
    @allure.description('Ищем элемент  с вопросом на странице, и проверяем выпажающий тест')
    def test_transition_for_questions_4(self,driver):
        search_question = SearchQuestion(driver)
        search_question.find_question(Transition.QUESTION_FOUR)
        element = search_question.drop_down_text(Transition.ANSWER_FOUR)
        assert element.text == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    @allure.title('Тест проверки выпадающего вопроса "Можно ли продлить заказ или вернуть самокат раньше?"')
    @allure.description('Ищем элемент  с вопросом на странице, и проверяем выпажающий тест')
    def test_transition_for_questions_5(self,driver):
        search_question = SearchQuestion(driver)
        search_question.find_question(Transition.QUESTION_FIVE)
        element = search_question.drop_down_text(Transition.ANSWER_FIVE)
        assert element.text == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

    @allure.title('Тест проверки выпадающего вопроса "Вы привозите зарядку вместе с самокатом?"')
    @allure.description('Ищем элемент  с вопросом на странице, и проверяем выпажающий тест')
    def test_transition_for_questions_6(self,driver):
        search_question = SearchQuestion(driver)
        search_question.find_question(Transition.QUESTION_SIX)
        element = search_question.drop_down_text(Transition.ANSWER_SIX)
        assert element.text == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    @allure.title('Тест проверки выпадающего вопроса "Можно ли отменить заказ?"')
    @allure.description('Ищем элемент  с вопросом на странице, и проверяем выпажающий тест')
    def test_transition_for_questions_7(self,driver):
        search_question = SearchQuestion(driver)
        search_question.find_question(Transition.QUESTION_SEVEN)
        element = search_question.drop_down_text(Transition.ANSWER_SEVEN)
        assert element.text == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    @allure.title('Тест проверки выпадающего вопроса "Я живу за МКАДом, привезёте?"')
    @allure.description('Ищем элемент  с вопросом на странице, и проверяем выпажающий тест')
    def test_transition_for_questions_8(self,driver):
        search_question = SearchQuestion(driver)
        search_question.find_question(Transition.QUESTION_EIGHT)
        element = search_question.drop_down_text(Transition.ANSWER_EIGHT)
        assert element.text == "Да, обязательно. Всем самокатов! И Москве, и Московской области."

