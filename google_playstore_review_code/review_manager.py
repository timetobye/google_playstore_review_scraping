import pandas as pd
import time
from datetime import datetime
from timeit import default_timer
from review_run_web_driver import RunChromeWebDriver
from review_set_default_web_page import SetDefaultWebPage
from review_get_specific_web_page import GetSpecificWebPage
from review_get_review_comment_info import GetReviewComment


def run_driver():
    web_driver = RunChromeWebDriver()
    execute_chrome_web_driver = web_driver.run_chrome_web_driver()

    return execute_chrome_web_driver


def set_default_parsing_page(driver, access_url):
    set_default_web_page = SetDefaultWebPage(driver=driver)
    access_driver = set_default_web_page.access_parsing_web_page(access_url)

    # get web_page last height
    web_page_last_height = set_default_web_page.get_current_web_page_last_height()

    return access_driver, web_page_last_height


def get_specific_parsing_page_info(driver, web_page_last_height):
    specific_web_page = GetSpecificWebPage(driver)
    specific_users_web_page_info = specific_web_page.get_the_specific_web_page_info(web_page_last_height)

    return specific_users_web_page_info


def get_review_user_info(specific_users_web_page_info):
    user_review_information = GetReviewComment()
    user_reviews_result_dict = user_review_information.get_user_review(specific_users_web_page_info)

    return user_reviews_result_dict


def create_csv_file(user_reviews_result_dict, application_name):
    user_reviews_result_df = pd.DataFrame.from_dict(user_reviews_result_dict, orient='index')
    user_reviews_result_df = user_reviews_result_df[
        [
            'user_name',
            'user_app_rating',
            'user_review_date',
            'company_comment_date',
            'user_simple_comment',
            'user_specific_comment',
            'company_answer_check'
        ]
    ]

    user_reviews_result_df.sort_values(by='user_review_date', ascending=False)

    now_time = datetime.now()
    file_date = now_time.strftime('%Y%m%d_%H%M%S')
    file_name = f'{application_name}_app_user_reviews_{file_date}.csv'

    user_reviews_result_df.to_csv(file_name, index=False)

    print('끝났습니다.!!')


def main():
    """
    example url
    - azar : https://play.google.com/store/apps/details?id=com.azarlive.android&hl=ko
    - socar : https://play.google.com/store/apps/details?id=socar.Socar
    """
    # input access page url
    application_name = input('앱 이름을 입력해 주세요 ex) socar : ')
    access_page_url = input('원하는 앱 리뷰 페이지 주소를 복사해서 입력해주세요 : ')

    program_start_time = default_timer()
    run_chrome_web_driver = run_driver()
    set_chrome_web_driver, browser_page_last_height = set_default_parsing_page(
        driver=run_chrome_web_driver,
        access_url=access_page_url
    )

    time.sleep(5)

    specific_users_web_page_info = get_specific_parsing_page_info(
        set_chrome_web_driver, browser_page_last_height
    )

    time.sleep(3)

    user_review_result = get_review_user_info(specific_users_web_page_info)
    create_csv_file(user_review_result, application_name)

    program_end_time = default_timer()
    program_running_time = program_end_time - program_start_time
    print(program_running_time)


if __name__ == "__main__":
    main()
