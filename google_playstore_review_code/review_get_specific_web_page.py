import time
import random
from bs4 import BeautifulSoup


class GetSpecificWebPage:
    def __init__(self, driver):
        self.chrome_driver = driver

    def get_the_specific_web_page_info(self, web_page_last_height, button_click_count=70):
        more_button_click_count = 0
        # limit_count_review_source = 1000
        more_button_click_string_xpath = f'//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/' \
                                         f'div/div/main/div/div[1]/div[2]/div[2]/div/span/span'
        repeat_check = 0  # 무한로딩 방지용으로 설정해둠

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
                if more_button_click_count == 100:  # To-do : find a best value..
                    # page_source_html = self.chrome_driver.page_source
                    page_source_soup = BeautifulSoup(self.chrome_driver.page_source, 'html.parser')
                    review_source_list = page_source_soup.find_all('div', class_="d15Mdf bAhLNe")

                    count_review_source = len(review_source_list)
                    print(f'count_review_source : {count_review_source}')

                    return review_source_list

                try:
                    self.chrome_driver.find_element_by_xpath(more_button_click_string_xpath).click()
                    more_button_click_count += 1
                    print(f'more_click_count : {more_button_click_count}')
                    time.sleep(random.randint(2, 5))

                    repeat_check = 0

                except Exception as e:
                    repeat_check += 1
                    print(f'repeat_check : {repeat_check}')
                    if repeat_check >= 5:
                        page_source_soup = BeautifulSoup(self.chrome_driver.page_source, 'html.parser')
                        review_source_list = page_source_soup.find_all('div', class_="d15Mdf bAhLNe")

                        count_review_source = len(review_source_list)
                        print(f'count_review_source : {count_review_source}')

                        return review_source_list

                    print(e)
                    continue
            else:
                web_page_last_height = web_page_new_height
