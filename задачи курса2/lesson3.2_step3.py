from selenium import webdriver
import time
import unittest

class Test(unittest.TestCase):
	def test1(self):
		try: 
			link = "http://suninjuly.github.io/registration1.html"
			browser = webdriver.Chrome()
			browser.get(link)
			input = browser.find_element_by_xpath ("//input[@class='form-control first' and @required]").send_keys("Ivan")
			input = browser.find_element_by_xpath ("//input[@class='form-control second' and @required]").send_keys("Petrov")
			input = browser.find_element_by_xpath ("//input[@class='form-control third' and @required]").send_keys("email")    	
			button = browser.find_element_by_css_selector("button.btn")
			button.click()   
			time.sleep(1)
			welcome_text_elt = browser.find_element_by_tag_name("h1")  
			welcome_text = welcome_text_elt.text    
			assert "Congratulations! You have successfully registered!" == welcome_text
		finally:
			time.sleep(10)
			browser.quit()
			
	def test2(self):
		try: 
			link = "http://suninjuly.github.io/registration2.html"
			browser = webdriver.Chrome()
			browser.get(link)
			input = browser.find_element_by_xpath ("//input[@class='form-control first' and @required]").send_keys("Ivan")
			input = browser.find_element_by_xpath ("//input[@class='form-control second' and @required]").send_keys("Petrov")
			input = browser.find_element_by_xpath ("//input[@class='form-control third' and @required]").send_keys("email")    	
			button = browser.find_element_by_css_selector("button.btn")
			button.click()   
			time.sleep(1)
			welcome_text_elt = browser.find_element_by_tag_name("h1")  
			welcome_text = welcome_text_elt.text    
			assert "Congratulations! You have successfully registered!" == welcome_text
			
		finally:
			time.sleep(10)
			browser.quit()
		
if __name__ == "__main__":
    unittest.main()
