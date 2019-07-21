import time
import random
from bs4 import BeautifulSoup


class GetSpecificWebPage:
    def __init__(self, driver):
        self.chrome_driver = driver

    def get_the_specific_web_page_info(self, web_page_last_height):
        more_button_click_count = 0
        # limit_count_review_source = 1000
        more_button_click_string_xpath = f'//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/' \
                                         f'div/div[1]/div/div/div[1]/div[2]/div[2]/div/span/span'

        while True:
            # Scroll down to bottom
            self.chrome_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page, but...how to set the proper sleep time?
            time.sleep(random.randint(3, 5))

            # Calculate new scroll height and compare with last scroll height
            web_page_new_height = self.chrome_driver.execute_script("return document.body.scrollHeight")
            print(f'web_page_new_height is : {web_page_new_height}, last_height : {web_page_last_height}')

            time.sleep(random.randint(2, 4))

            if web_page_new_height == web_page_last_height:

                if more_button_click_count == 20:  # To-do change value 3 to 50
                    page_source_html = self.chrome_driver.page_source
                    page_source_soup = BeautifulSoup(page_source_html, 'html.parser')
                    review_source_list = page_source_soup.find_all('div', class_="d15Mdf bAhLNe")

                    count_review_source = len(review_source_list)
                    print(f'count_review_source : {count_review_source}')

                    return review_source_list

                try:
                    more_button_click_count += 1
                    print(f'more_click_count : {more_button_click_count}')
                    self.chrome_driver.find_element_by_xpath(more_button_click_string_xpath).click()
                    time.sleep(random.randint(2, 5))

                except Exception as e:
                    print(e)
                    continue
            else:
                web_page_last_height = web_page_new_height