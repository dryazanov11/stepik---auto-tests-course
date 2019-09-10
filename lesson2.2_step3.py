from selenium import webdriver
import time
import os

try:
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)
	input = browser.find_element_by_css_selector ("[name='firstname']").send_keys("firstname")
	input = browser.find_element_by_css_selector ("[name='lastname']").send_keys("lastname")
	input = browser.find_element_by_css_selector ("[name='email']").send_keys("email")
	current_dir = os.path.abspath(os.path.dirname("C:/Users/dryazanov/selenium_course/file.txt"))        #загружаем файл с компа
	file_path = os.path.join(current_dir, 'file.txt')  
	input = browser.find_element_by_css_selector("#file").send_keys(file_path)     #вставояем файл
	tap = browser.find_element_by_css_selector ("button").click()
	

finally:
	time.sleep (10)
	browser.quit()