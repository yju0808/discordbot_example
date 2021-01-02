<p align="center">
<img src="./img/support.png" width="20%" height="20%" alt="mainimg"></img>
</p>

디스코드 봇 예제
===

디스코드 봇 예제입니다      

유용한 페이지
---
[discord.py 소스코드](https://github.com/Rapptz/discord.py)   
[discord.py API 공식문서](https://discordpy.readthedocs.io/en/latest/api.html)    
[처음부터 잘 정리된 블로그 글](https://m.blog.naver.com/6116949/221901926848)   
[다양한 기능 구현을 볼 수 있는 블로그](https://blue-coding.tistory.com/15?category=755355)      

<br/>

기능 구현을 위한 가이드
---
사용한 모듈
```{.python}
import discord
import requests
import json
import random
from selenium import webdriver
import bs4
import re
```

|모듈|용도|관련 링크|
|:---:|:---:|:---:|
|discord|디스코드 봇 제작|[discord.py API 공식문서](https://m.blog.naver.com/6116949/221901926848)|
|requests|네이버 api 이용|[Python requests 모듈 간단 정리](https://dgkim5360.tistory.com/entry/python-requests)|
|json|api 결과값 사용|[[파이썬] json 모듈로 JSON 데이터 다루기](https://www.daleseo.com/python-json/)|
|random|가위바위보 기능|[랜덤(random) 모듈](https://wikidocs.net/79)|
|selenium|웹 크롤링(유튜브)|[<문과의 파이썬>셀레니움(selenium)](https://brunch.co.kr/@jk-lab/18)|
|bs4|웹 크롤링(유튜브)|[사이트 정보 추출하기 - beautifulsoup 사용법](https://wikidocs.net/85739)|
|re|정규표현식(알파벳 검색)|[점프 투 파이썬 07장 정규표현식](https://wikidocs.net/1669)|
