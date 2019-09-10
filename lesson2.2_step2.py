from selenium import webdriver
import time
import math
from math import log, sin

def calc(x):
  return str (math.log(abs(12*sin(x))))

try:
	link = "http://suninjuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)
	x_element = browser.find_element_by_css_selector ("#input_value")
	x = x_element.text
	y = calc (int (x))
	browser.execute_script("window.scrollBy(0, 100);")      #скроллим на 100 пикселей вниз, потому что вылез баннер и мешает проставить чекбоксы
	element = browser.find_element_by_id("answer").click()
	input = browser.find_element_by_css_selector ("#answer").send_keys(y)
	button = browser.find_element_by_css_selector ("#robotCheckbox").click()
	radio = browser.find_element_by_css_selector ("#robotsRule").click()
	tap = browser.find_element_by_css_selector ("button").click()

finally:
	time.sleep (10)
	browser.quit()