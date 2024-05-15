from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.headless = False
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
website = r"https://practicetestautomation.com/practice-test-login/"
driver.get(website)
sleep(2)


username = driver.find_element(By.ID, "username")
username.send_keys('student')
sleep(1)

password = driver.find_element(By.ID, "password")
password.send_keys('Password123')
sleep(1)


btn = driver.find_element(By.ID, "submit")
btn.click()
sleep(20)


driver.quit()
