from bs4 import BeautifulSoup


def get_star_rate(user_info_soup):
    review_star_rate_info = user_info_soup.find('div', role='img')

    string_review_star_rate = str(review_star_rate_info).split("=")
    star_rate_list = string_review_star_rate[1].split(' ')

    star_rate = int(star_rate_list[3][0])

    return star_rate


def get_date(user_info_soup):
    date_list = []

    review_comment_date_list = user_info_soup.find_all('span', class_='p2TkOb')

    length_date_list = len(review_comment_date_list)

    if length_date_list == 2:
        for i, review_comment_date in enumerate(review_comment_date_list):
            comment_date = review_comment_date.get_text()
            date_list.append(comment_date)

        review_date = date_list[0]
        answer_date = date_list[1]

        return review_date, answer_date

    else:
        for i, review_comment_date in enumerate(review_comment_date_list):
            comment_date = review_comment_date.get_text()
            date_list.append(comment_date)

        date_list.append('no_answer')

        review_date = date_list[0]
        answer_date = date_list[1]

        return review_date, answer_date


def get_name(user_info_soup):
    review_name_list = user_info_soup.find_all('span', class_='X43Kjb')
    review_user_name = review_name_list[0].get_text()

    return review_user_name


def get_simple_comment(user_info_soup):
    simple_comment_list = user_info_soup.find_all('span', jsname='bN97Pc')
    simple_comment = simple_comment_list[0].get_text()

    return simple_comment


def get_specific_comment(user_info_soup):
    specific_comment_list = user_info_soup.find_all('span', jsname='fbQN7e')
    specific_comment = specific_comment_list[0].get_text()

    return specific_comment


def get_comment(user_info_soup):

    specific_comment = get_specific_comment(user_info_soup)

    if specific_comment:

        return specific_comment
    else:
        simple_comment = get_simple_comment(user_info_soup)

        return simple_comment


def get_answer_check(user_info_soup):
    answer_list = user_info_soup.find_all('div', class_='LVQB0b')

    if answer_list:
        answer_to_user = "answer"

        return answer_to_user

    else:
        answer_to_user = 'no_answer'

        return answer_to_user


class GetReviewComment:
    def __init__(self):
        pass

    def get_user_review(self, users_web_page_info):

        user_review_dict = {}

        for i, user_info in enumerate(users_web_page_info):
            string_user_info = str(user_info)
            user_info_soup = BeautifulSoup(string_user_info, 'html.parser')

            star_rate = get_star_rate(user_info_soup)
            review_date, answer_date = get_date(user_info_soup)
            name = get_name(user_info_soup)
            # simple_comment = get_simple_comment(user_info_soup)
            # comment_all = get_specific_comment(user_info_soup)
            comment = get_comment(user_info_soup)
            answer_check = get_answer_check(user_info_soup)

            if i not in user_review_dict:
                user_review_dict[i] = {
                    'user_name': name,
                    'user_app_rating': star_rate,
                    'user_review_date': review_date,
                    'company_comment_date': answer_date,
                    'comment' : comment,
                    # 'user_simple_comment': simple_comment,
                    # 'user_specific_comment': comment_all,
                    'company_answer_check': answer_check
                }

        return user_review_dict
