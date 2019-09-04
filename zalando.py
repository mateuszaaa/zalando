import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
import time
import re
import sys
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

def isVisible(xpath, timeout=2):
    try:
        ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return True
    except TimeoutException:
        return False

def waitFor(xpath):
    for i in range(5):
        if isVisible(element_id):
            print("found")
            return
        else:
            print("not found")
    raise Exception("fatal error")


opts = Options()
# opts.add_argument("--headless")
opts.add_argument('--no-sandbox')
driver = webdriver.Chrome('/usr/bin/chromedriver', options=opts)
# options.setProxy(null);

driver.get("https://zalando-lounge.pl/#/login")

xpath_login = "//button[contains(text(),'Zarejestruj się teraz')]"

login = ui.WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, "form-email")))
login.send_keys("mateusz.cz.nowakowski@gmail.com")
password = ui.WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, "form-password")))
password.send_keys("4JUY6X76Vcc9GFM")
password.submit()

mens = "//li[contains(text(),'Mężczyźni')]";
ui.WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, mens))).click()

ui.WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, "campaigns-open")))
promotions = driver.find_elements_by_xpath("//div[@id='campaigns-open']//a")
print(promotions)
random.choice(promotions).click()

filters = "//a[contains(@class, 'tabs___link')]"
ui.WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, filters)))
driver.find_elements_by_xpath(filters)[1].click() #filtry



# filters = "//div[contains(@class, 'size___tabs')]//span[contains(text(), 'Górne częsci garderoby')"
categories = { 'Górne części garderoby': ["41", "L", "XL"], 'Spodnie' :["34", "34x34", "L"], 'Obuwie':["45","46"] }

for category in categories:
    filters = "//span[contains(text(), '{}')]".format(category)
    print(category)
    try:
        ui.WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, filters))).click()
        for f in categories[category]:
            try:
                ui.WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.NAME, f))).click()
                print("{} - success".format(f))
            except selenium.common.exceptions.TimeoutException:
                pass
            except selenium.common.exceptions.NoSuchElementException:
                pass
    except selenium.common.exceptions.NoSuchElementException:
        pass
    except selenium.common.exceptions.TimeoutException:
        print("not found")
        pass

        # filters = "//span[contains(text(), '{}')]".format(category)
        # ui.WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, filters)))

# print(len(driver.find_elements_by_xpath(filters)))

