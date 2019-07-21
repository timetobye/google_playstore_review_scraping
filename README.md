naver_cafe_board_scraping
---------------------
![alt text](https://img.shields.io/badge/Python-3.7-red.svg)
![alt text](https://img.shields.io/badge/selenium-Chrome%20driver-brightgreen.svg)
![alt text](https://img.shields.io/badge/googleplaystore-Appreview-yellowgreen.svg)
![alt text](https://img.shields.io/badge/results-csv-blue.svg)
![alt text](https://img.shields.io/badge/data-web-orange.svg)


> Google Playstore에서 App의 review commnet를 가져와서 csv로 저장합니다.

:spiral_notepad: Introduction
----------------------------

사용자의 목소리를 듣는 것은 서비스 제공을 하는 사람들의 최우선 업무 중 하나입니다. 직장을 다닌다면 회사에서 등록된 API를 이용해서
사용자가 작성한 리뷰를 가져 올 수 있지만, 그렇지 않을 경우는 수작업으로 확인을 해야 합니다. 
이제 막 시작한 서비스 App이라면 확인하는 것이 오래 걸리지 않겠지만, 상대적으로 더 많은 이용자가 있는 App이라면 그것도 쉽지 않습니다. 
무엇보다 우리는 리뷰만 확인 하는 것이 아니라, 이것 저것 요것 ~~말도 안되는 것~~ 도 다 하기 때문에 시간도 부족하죠. 
그래서 하나 구글 플레이 스토어에서 사용자들이 작성한 리뷰를 가져올 수 있도록 구현하였습니다.

이전에 작성한 naver cafe에 작성된 게시글을 가져오는 것과는 또 다른 재미(?)가 있었습니다. 
로그인이 없었기 떄문에 접근 하는 것 자체는 쉬웠으나, 과도한 크롤링에 IP 자체를 차단해버리면 어쩌지 하는 두려움도 있었습니다. 
어찌됐든 시간 간격을 잘 설정해서 그런 일은 없었으니 다행이지요.
그러나 리뷰 페이지는 쉬운 대상은 아니었습니다. Selenium으로 페이지를 계속 스크롤 해야 하는데, 스크롤 하는 기법을 몰라서 찾아보고
다시 적용해보고, 에러가 발생하면 다시 또 찾아보고... 반복의 연속이었습니다.
더군다나 selenium으로 실행한 chrome browser는 일정 페이지를 로딩하면 한계가 있는 것 처럼 보였습니다. 
그래서 리뷰는 수만개가 달려있어도 막상 가져올 수 있는 건 3000개 조금 넘은 숫자입니다. 
다행히도 3000개가 넘는 리뷰도 1년 넘는 기간 동안 달린 리뷰라서 가치가 있다고 생각합니다.
이 밖에도 특정 리뷰는 쓰레드처럼 달리는 경우도 있어서 서비스 제공자가 답변한 날짜와 사용자가 작성한 날짜 간격이 이상하게 잡히기도 했습니다.

어찌됐든 원하는 소기 목적은 달성하였고, 각 서비스에 달린 리뷰 파일을 가지고 분석을 진행 할 예정입니다. 때마침 Kakao에서 만든 Khaiii도 잘 작동하고 있으니
리뷰 분석을 할 때 좀 더 ~~스트레스 덜 받고~~ 즐겁게 할 수 있을 것 같습니다.

항상 혼자 코드를 작성하다 보니 많이 외롭고...쉽지 않지만 그래도 언젠가 이 시간이 밑거름이 될 거라고 생각합니다.