from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox(executable_path=r"C:/Users/jerom/Desktop/FireFoxDriver/geckodriver.exe")
driver.get("https://google.com/maps")

search = driver.find_element_by_id('searchboxinput')
search.send_keys('Kankanady')
search.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "S9kvJb"))
    )
    element.click()
finally:
    search.send_keys('scnsdcc')
