google_playstore_review_scraping
---------------------
![alt text](https://img.shields.io/badge/Python-3.7-red.svg)
![alt text](https://img.shields.io/badge/selenium-Chrome%20driver-brightgreen.svg)
![alt text](https://img.shields.io/badge/googleplaystore-Appreview-yellowgreen.svg)
![alt text](https://img.shields.io/badge/results-csv-blue.svg)
![alt text](https://img.shields.io/badge/data-web-orange.svg)


> Google Playstore에서 App의 review를 가져와서 csv로 저장합니다.

:spiral_notepad: Introduction
----------------------------

사용자의 목소리를 듣는 것은 서비스 제공을 하는 사람들의 최우선 업무 중 하나입니다. 직장을 다닌다면 회사에서 등록된 API를 이용해서
사용자가 작성한 리뷰를 가져 올 수 있지만, 그렇지 않을 경우는 수작업으로 확인을 해야 합니다. 
이제 막 시작한 서비스 App이라면 확인하는 것이 오래 걸리지 않겠지만, 상대적으로 더 많은 이용자가 있는 App이라면 그것도 쉽지 않습니다. 
무엇보다 우리는 리뷰만 확인 하는 것이 아니라, 이것 저것 요것 ~~말도 안되는 것~~ 도 다 하기 때문에 시간도 부족하죠. 
그래서 구글 플레이 스토어에서 사용자들이 작성한 리뷰를 자동으로 가져올 수 있도록 구현하였습니다.

:keyboard: 설치 방법
-------------
기본적으로 Git이 설치되있다고 가정하고 아래의 코드를 터미널에서 실행해주세요.
```
git clone https://github.com/timetobye/google_playstore_review_scraping.git
``` 

**selenium용 driver download**
- selenium을 사용하려면 driver가 필요하며, chrome web driver를 사용하였습니다.
- 자신의 chrome browser version에 맞는 것을 다운 받아주세요. 최신 사용을 권장합니다.
- [chrome web driver 다운로드 페이지](http://chromedriver.chromium.org/downloads)
- vesion history
  - 2020.08.21 ~ : 84.x
  - ~~2020.04.05 ~ : 80.x~~
  - ~~2020.01.12 ~ : 79.x~~
  - ~~2019.12.25 ~ : 78.0.3904.105~~
  - ~~2019.09.24 : 75.0.3770.140~~
  - ~~2019.09.26 ~ : 77.0.3865.40(current)~~ 

### library
라이브러리 설치
```
pip install -r requirements.txt
```

:desktop_computer: 사용 방법
-----------------------------
사용하기 위해서는 아래 예시와 같이 원하는 App의 리뷰 페이지 링크가 필요합니다.

**example url**
- **socar** : https://play.google.com/store/apps/details?id=socar.Socar&hl=ko
- **zigzag** : https://play.google.com/store/apps/details?id=com.croquis.zigzag&hl=ko
- **final fantasy brave exvius** : https://play.google.com/store/apps/details?id=com.square_enix.android_googleplay.FFBEWW&hl=ko

:robot: example run code
```bash
python3 playstore_review_scraping.py
```

:building_construction: 상세 설명

1. 실행을 하게 되면 앱의 이름(영어로 입력해주세요)과 App의 리뷰 페이지 링크를 입력
2. 화면 전환 진행 - 관심에서 최신으로 자동 변경 후 스크래핑 시작
3. 일정 시간이 지나면 리뷰 페이지를 csv를 폴더내에 저장하고 종료 됩니다. 


### notice
각 단계 별로 일정 시간이 설정 되어 있습니다.
- 스크롤을 한 뒤 페이지가 로딩 되는 시간이 필요하기 때문에 시간 간격 설정을 해두었습니다.
- 1회 더보기를 누른 후 다음 더보기를 누르기까지 약 160개의 리뷰가 추가로 로딩됩니다.
  

:notebook_with_decorative_cover: example result
-------------------------------------
실행 후 csv로 저장합니다. 저장 되는 항목은 아래와 같습니다.

```python3
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
```

- user_name : 사용자의 닉네임
  - Google 사용자라는 경우가 있는데, 탈퇴하거나 이용하지 않은 회원인 것 같습니다. 의외로 많습니다.
- user_app_rating : 별점
- user_review_date : 리뷰 작성 날짜
- company_comment_date : 서비스 제공자가 답변 작성한 날짜
- comment : 리뷰 내용
- company_answer_check : 서비스 제공자 답변 여부


#### example
![alt text](https://github.com/timetobye/google_playstore_review_scraping/blob/master/review_sample_image_1.gif)

:open_file_folder: Directory structure
------------
``` bash
  |-google_playstore_review_code                     #google_playstore_review folder
  |  |-review_run_web_driver.py                      #web driver 실행
  |  |-review_set_default_web_page.py                #리뷰 페이지 설정
  |  |-review_get_specific_web_page.py               #페이지 정보 조회
  |  |-review_get_review_comment.py                  #조회된 페이지를 바탕으로 자료 추출
  |-README.md                                        #README.md
  |-playstore_review_scraping.py                     #main 실행 코드
  |-chromedriver                                     #chromedriver
  |-requirements.txt                                 #library 항목
```

:memo: To-Do list
------------------
- [X] 더 많은 리뷰를 가져올 수 있도록 방법 찾기
  - 2019.12.21 기준 6천개 이상 가져올 수 있음
- [X] user_simple_commen, user_specific_comment 를 하나로 합쳐서 csv로 저장하는 코드 구현
  - comment 라는 값 하나로 합쳐서 구현
- [ ] 진행 중 일때 출력되는 메시지 업데이트
- [ ] try-except를 활용한 에러 대응

:man_technologist: Contact
```
github : https://github.com/timetobye
```

:bookmark: 참고 페이지
-------------
작성 예정(많아요....너무 많아요..ㅠ)
