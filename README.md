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
그래서 구글 플레이 스토어에서 사용자들이 작성한 리뷰를 가져올 수 있도록 구현하였습니다.

이전에 작성한 naver cafe에 작성된 게시글을 가져오는 것과는 또 다른 재미(?)가 있었습니다. 
로그인이 없었기 떄문에 접근 하는 것 자체는 쉬웠으나, 과도한 크롤링에 IP 자체를 차단해버리면 어쩌지 하는 두려움도 있었습니다. 
어찌됐든 시간 간격을 잘 설정해서 그런 일은 없었으니 다행이지요.
그러나 리뷰 페이지는 쉬운 대상은 아니었습니다. selenium으로 페이지를 계속 스크롤 해야 하는데, 스크롤 하는 기법을 몰라서 찾아보고
다시 적용해보고, 에러가 발생하면 다시 또 찾아보고... 반복의 연속이었습니다.
더군다나 selenium으로 실행한 chrome browser는 일정 페이지를 로딩하면 한계가 있는 것 처럼 보였습니다. 
그래서 리뷰는 수만개가 달려있어도 막상 가져올 수 있는 건 3000개 조금 넘은 숫자입니다. 
다행히도 3000개가 넘는 리뷰도 1년 넘는 기간 동안 달린 리뷰라서 가치가 있다고 생각합니다.
이 밖에도 특정 리뷰는 쓰레드처럼 달리는 경우도 있어서 서비스 제공자가 답변한 날짜와 사용자가 작성한 날짜 간격이 이상하게 잡히기도 했습니다.

어찌됐든 원하는 소기 목적은 달성하였고, 각 서비스에 달린 리뷰 파일을 가지고 분석을 진행 할 예정입니다. 때마침 Kakao에서 만든 Khaiii도 잘 작동하고 있으니
리뷰 분석을 할 때 좀 더 ~~스트레스 덜 받고~~ 즐겁게 할 수 있을 것 같습니다.

항상 혼자 코드를 작성하다 보니 많이 외롭고...쉽지 않지만 그래도 언젠가 이 시간이 밑거름이 될 거라고 생각합니다.

~~동기랑 같이 해보고 싶은 것 중 하나였는데...아쉽다..이젠 못 하겠네~~

:keyboard: 설치 방법
-------------
기본적으로 Git이 설치되있다고 가정하고 아래의 코드를 터미널에서 실행해주세요.
```
git clone https://github.com/timetobye/google_playstore_review_scraping.git
``` 

**selenium용 driver download**
- selenium을 사용하려면 driver가 필요합니다.
- chrome web driver를 사용하였습니다.
- 자신의 chrome browser version에 맞는 것을 다운 받아주세요.
- [chrome web driver 다운로드 페이지](http://chromedriver.chromium.org/downloads)
- vesion
  - ~ 2019.09.24 : 75.0.3770.140
  - 2019.09.26 ~ : 77.0.3865.40(current)
- 참고로 사용했던 driver가 repo에 함께 있습니다. 

### library
```
pip install -r requirements.txt
```

### 주의 사항
- library 설치 시 오류가 발생할 경우 에러 메시지로 검색하여 대응해주시기 바랍니다.


:desktop_computer: 사용 방법
-----------------------------
사용하기 위해서는 아래 예시와 같이 원하는 App의 리뷰 페이지 링크가 필요합니다.

**example url**
- **socar** : https://play.google.com/store/apps/details?id=socar.Socar&hl=ko
- **zigzag** : https://play.google.com/store/apps/details?id=com.croquis.zigzag&hl=ko
- **final fantasy brave exvius** : https://play.google.com/store/apps/details?id=com.square_enix.android_googleplay.FFBEWW&hl=ko


:robot: example run code
```bash
python3 review_manager.py
```

:building_construction: 상세 설명

1. 실행을 하게 되면 앱의 이름과 App의 리뷰 페이지 링크를 입력 해달라는 메시지가 뜹니다.
2. 입력해주세요. 입력 후App 리뷰 페이지 링크로 이동합니다.
3. 잠시 후 App 리뷰 모두 보기로 자동으로 이동합니다.
4. 기본 default 보기가 유용순으로 되어 있는데, 최신순으로 자동으로 변환해 줍니다.
5. 그 뒤로는 스크롤을 내리면서 더보기를 자동으로 클릭합니다.
6. 일정 단계가 지나면 리뷰 페이지를 csv를 폴더내에 저장하고 종료 됩니다. 


### notice
각 단계 별로 일정 시간이 설정 되어 있습니다.
- 스크롤을 한 뒤 페이지가 로딩 되는 시간이 필요하기 때문에 시간 간격 설정은 필수입니다.
- 1회 더보기를 누른 후 다음 더보기를 누르기까지 약 160개의 리뷰가 추가로 로딩됩니다.
  - 그래서 더보기는 20회로 설정해두었습니다.
  

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
- user_simple_comment : 리뷰 내용
- user_specific_comment : 리뷰 상세
  - 간혹 리뷰가 길어서 user_simple_comment에서 다 못 가져오는 경우가 있습니다.
  - 이를 위해 리뷰 상세 소스도 가져옵니다.
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
  |  |-review_manager.py                             #main 실행 코드
  |  |-requirements.txt                              #library 항목
  |-README.md                                        #README.md
```


:memo: To-Do list
------------------
- [X] 더 많은 리뷰를 가져올 수 있도록 방법 찾기
  - 2019.12.21 기준 6천개 이상 가져올 수 있음
- [ ] user_simple_commen, user_specific_comment 를 하나로 합쳐서 csv로 저장하는 코드 구현
- [ ] 현재 App 당 20분 정도 걸리는데 시간 단축해보기
  - 셀레니움 속도상 어려울 듯
- [ ] 진행 중 일때 출력되는 메시지 업데이트
- [ ] try-except를 활용한 에러 대응

:man_technologist: Contact
```
github : https://github.com/timetobye
```

:bookmark: 참고 페이지
-------------
작성 예정(많아요....너무 많아요..ㅠ)
