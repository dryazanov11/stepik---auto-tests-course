from selenium import webdriver
import time
import math

def test_input_text(expected_result, actual_result):
    if expected_result != actual_result:
        return f"expected {expected_result}, got {actual_result}"
    


expected_result = 8
actual_result = 11
print (test_input_text(expected_result, actual_result))