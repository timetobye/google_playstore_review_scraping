import time
import random
from selenium.webdriver.common.keys import Keys


class SetDefaultWebPage:
    def __init__(self, driver):
        self.chrome_driver = driver

    def access_parsing_web_page(self, access_page_url):
        self.chrome_driver.get(access_page_url)
        time.sleep(random.randint(4, 9))

        self._click_more_review_button()
        self._select_toggle_button()
        self._click_recent_button()

        return self.chrome_driver

    def _click_more_review_button(self):
        more_review_string_xpath = f'//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]' \
                                   f'/div/div/main/div/div[1]/div[6]/div/span/span'
        self.chrome_driver.find_element_by_xpath(more_review_string_xpath).click()
        time.sleep(3)

    def _select_toggle_button(self):
        select_toggle_string_xpath = f'//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/div/div/main/' \
                                     f'div/div[1]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div[3]/span'
        self.chrome_driver.find_element_by_xpath(select_toggle_string_xpath).click()
        time.sleep(3)

    def _click_recent_button(self):
        click_recent_button_xpath = f'//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/div/div/main/' \
                                    f'div/div[1]/div[2]/c-wiz/div[1]/div/div[2]/div[1]/span'

        self.chrome_driver.find_element_by_xpath(click_recent_button_xpath).click()
        time.sleep(3)

    def get_current_web_page_last_height(self):
        self.chrome_driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        last_height = self.chrome_driver.execute_script("return document.body.scrollHeight")

        return last_height
