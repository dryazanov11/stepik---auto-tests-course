from selenium import webdriver
import time
import math

def calc (x):
	return str (math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)
	x_element = browser.find_element_by_css_selector ("#treasure")
	x1_element = x_element.get_attribute ("valuex")
	
	y = calc(x1_element)
	input = browser.find_element_by_css_selector ("#answer").send_keys(y)

	button = browser.find_element_by_css_selector ("#robotCheckbox").click()
	radio = browser.find_element_by_css_selector ("#robotsRule").click()
	tap = browser.find_element_by_css_selector ("button").click()

finally:
	time.sleep (10)
	browser.quit()