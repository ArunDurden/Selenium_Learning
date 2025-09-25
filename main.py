from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

chrome_service = Service(r"C:\Users\arunp\Python_Projects\Selenium_Learning\chromedriver-win64\chromedriver.exe")

"""In the below line, it is important to provide the chrome_service as an argument to the service."""
driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
driver.get("https://demoqa.com/login")
""" demoqa.com used above is a website made for learning web automation in fact it's a website to get
selenium certification, so create a user account there, it will be useful."""

wait = WebDriverWait(driver, 10)
username_text_box = wait.until(EC.visibility_of_element_located((By.ID, 'userName')))
password_text_box = wait.until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

username_text_box.send_keys("ArunDurden")
password_text_box.send_keys("Batsy004!")
"""You may think why I haven't used wait.until() for clicking the login button too.
The thing is sometimes google may pop an advertisement that hides the login button, in that case, we'll get an error.
So, we're using execute_script method - this method takes JavaScript code & an UI object. Basically executes a JavaScript
code and makes increases a chance of an element getting clicked.

Read the Selenium docs"""
driver.execute_script("arguments[0].click()", login_button)

if input("Enter 'yes' to quit the driver: ") == 'yes':
	driver.quit()