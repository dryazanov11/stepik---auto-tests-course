from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
from math import log, sin

def calc(x):
  return str (math.log(abs(12*sin(x))))

try:
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser = webdriver.Chrome()
	browser.get(link)
	button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
	button = browser.find_element_by_css_selector ("#book").click()
	x_element = browser.find_element_by_css_selector ("#input_value")
	x = x_element.text
	y = calc(int (x))
	input = browser.find_element_by_css_selector ("#answer").send_keys(y)
	tap = browser.find_element_by_css_selector ("#solve").click()



finally:
	time.sleep (10)
	browser.quit()