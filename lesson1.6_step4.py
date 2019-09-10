﻿from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements_by_css_selector ("[type = text]")
    for element in elements:
       element.send_keys("Answer")

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()