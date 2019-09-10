from selenium import webdriver
import time
import math

def calc (x):
	return str (math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/math.html"
	browser = webdriver.Chrome()
	browser.get(link)
	x_element = browser.find_element_by_css_selector ("#input_value")
	x = x_element.text
	y = calc(x)
	input = browser.find_element_by_css_selector ("#answer").send_keys(y)

	button = browser.find_element_by_xpath ("//label[@class='form-check-label' and @for='robotCheckbox']").click()
	radio = browser.find_element_by_xpath ("//label[@class='form-check-label' and @for='robotsRule']").click()
	tap = browser.find_element_by_css_selector ("button").click()

finally:
	time.sleep (10)
	browser.quit()