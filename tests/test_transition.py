import allure
import pytest

from Locators.data import transition_data
from pages.transition_page import SearchQuestion


class TestTransition:
    @allure.title('Тест проверки выпадающих вопросов"')
    @pytest.mark.parametrize("question, answer, expected_text", transition_data)
    def test_transition_for_questions(self, driver, question, answer, expected_text):
        search_question = SearchQuestion(driver)
        search_question.find_question(question)
        element = search_question.drop_down_text(answer)
        assert element.text == expected_text
