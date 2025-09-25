from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_service = Service(r"C:\Users\arunp\Python_Projects\Selenium_Learning\chromedriver-win64\chromedriver.exe")

"""In the below line, it is important to provide the chrome_service as an argument to the service."""
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://demoqa.com/login")
""" demoqa.com used above is a website made for learning web automation in fact it's a website to get
selenium certification, so create a user account there, it will be useful."""


if input("Enter 'yes' to quit the driver: ") == 'yes':
	driver.quit()



