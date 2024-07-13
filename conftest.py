import pytest
from selenium import webdriver
from constants import Constants


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.get(Constants.URL)
    browser.maximize_window()
    yield browser
    browser.quit()