from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.ID, "book")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    
    button.click()

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    submit = browser.find_element(By.ID, "solve")
    submit.click()
    

finally:
  
    time.sleep(10)    
    browser.quit()