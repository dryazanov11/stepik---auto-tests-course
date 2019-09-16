import time
import math
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
	
	
@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test1 (browser, number):
	link = f"https://stepik.org/lesson/{number}/step/1"
	browser.get(link)
	answer = str (math.log(int(time.time())))
	input = browser.find_element_by_css_selector ("[class = 'textarea ember-text-area ember-view']").send_keys(answer)
	tap = browser.find_element_by_xpath ("//button").click()
	time.sleep(1)
	# text = browser.find_element_by_css_selector (".smart-hints_hint").text
	# assert ask == "Correct!", "is not correct!"
	
	
	
	
	#ДОЛЖНО РАБОТАТЬ, НО ПОЧЕМУ-ТО ВЫДАЕТ ОШИБКУ selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":".smart-hints_hint"}

