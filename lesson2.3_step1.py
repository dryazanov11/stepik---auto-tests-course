from selenium import webdriver
import time
import math
from math import log, sin

def calc(x):
  return str (math.log(abs(12*sin(x))))

try:
	link = "http://suninjuly.github.io/alert_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)
	tap = browser.find_element_by_css_selector ("button").click()
	confirm = browser.switch_to.alert                                #открывается модальное окно
	confirm.accept()                                                 #и мы выбираем "Да"
	x_element = browser.find_element_by_css_selector ("#input_value")
	x = x_element.text
	y = calc(int (x))
	input = browser.find_element_by_css_selector ("#answer").send_keys(y)
	tap = browser.find_element_by_css_selector ("button").click()

finally:
	time.sleep (10)
	browser.quit()