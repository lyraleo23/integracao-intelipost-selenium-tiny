import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def start_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    actions = ActionChains(driver)

    return driver

def open_page(driver, url):
    driver.get(url)
    time.sleep(2)

