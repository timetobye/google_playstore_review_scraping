import os
from selenium import webdriver


class RunChromeWebDriver:

    def __init__(self):
        pass

    def run_chrome_web_driver(self):
        chrome_web_driver_path = self.get_chrome_web_driver_path
        chrome_driver = webdriver.Chrome(chrome_web_driver_path)
        chrome_driver.implicitly_wait(3)

        return chrome_driver

    @property
    def get_chrome_web_driver_path(self):
        current_working_directory = os.getcwd()
        chrome_driver_file_name = '/chromedriver'
        chrome_web_driver_path = current_working_directory + chrome_driver_file_name

        return chrome_web_driver_path
