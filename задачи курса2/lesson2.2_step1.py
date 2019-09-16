
from selenium import webdriver
import time
import math

def calc(x,y):
  return str(int(x)+int(y))

try:
	link = "http://suninjuly.github.io/selects1.html"
	browser = webdriver.Chrome()
	browser.get(link)
	x_element = browser.find_element_by_css_selector ("#num1")
	x = x_element.text
	y_element = browser.find_element_by_css_selector ("#num2")
	y = y_element.text
	z = calc (x,y)
	element = browser.find_element_by_id("dropdown").click()             #нажимаем на выпадающий список
	browser.find_element_by_css_selector("[value='" + z + "']").click()  #ищем значение, равное посчитанному ранее
	
	
	tap = browser.find_element_by_css_selector ("button").click()

finally:
	time.sleep (10)
	browser.quit()
