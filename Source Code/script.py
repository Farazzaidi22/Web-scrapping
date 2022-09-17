import time
from selenium import webdriver
from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException



def Search_And_Download_Files():
    chrome_executable = Service(executable_path='chromedriver.exe', log_path='NUL')

    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "E:\Freelance\XML Data handling\Source Code\data_files"}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=chrome_executable, chrome_options=options)

    driver.implicitly_wait(500)  # gives an implicit wait for 20 seconds

    driver.get('https://www.handelsregister.de/rp_web/erweitertesuche.xhtml')


    search_bar = driver.find_element(
        by=By.XPATH, value="//textarea[@id='form:schlagwoerter']").send_keys("faraz")


    find_button = driver.find_element(
        by=By.XPATH, value="//button[@id='form:btnSuche']")
    find_button.click()

    SI_data = driver.find_element(
        by=By.XPATH, value="//a[6]/span[contains(text(),'SI')]")

    try:
        SI_data.click()
        download_button = driver.find_element(
            by=By.XPATH, value="//button[@id='form:kostenpflichtigabrufen']")
        download_button.click()
    except WebDriverException:
        print("No element found")

    time.sleep(10)
