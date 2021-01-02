<p align="center">
<img src="./img/support.png" width="20%" height="20%" alt="mainimg"></img>
</p>

디스코드 봇 예제 및 가이드
===

디스코드 봇 예제 및 가이드입니다      

유용한 링크
---
[YJU가 제작한 디스코드 봇 소스코드](https://github.com/yju0808/discordbot_example/blob/master/discordbot.py)   
[처음부터 잘 정리된 블로그 글](https://m.blog.naver.com/6116949/221901926848)   
[다양한 기능 구현을 볼 수 있는 블로그](https://blue-coding.tistory.com/15?category=755355)   
[discord.py 소스코드](https://github.com/Rapptz/discord.py)   
[discord.py API 공식문서](https://discordpy.readthedocs.io/en/latest/api.html)  

<br/>


봇 제작 시작하기
---
[해당 링크](https://m.blog.naver.com/6116949/221901926848)에 나와있는 대로 진행하시면 됩니다
대체적으로 잘 설명되어 있으나 
```
일단, Discord 봇을 만들기 위해서는 Discord 라이브러리를 다운로드 받아서 사용하도록 선언해야합니다. 
사용하시는 IDE 따라서 pip를 이용하여 설치하시면 됩니다. 
특히, venv 환경을 사용하시는 경우에 조심하시기 바랍니다.
```
이 부분은 [cmd](https://editorizer.tistory.com/200)를 열고
```
pip install discord
```
를 입력하시면 되고요

<br/>

링크 내용을 다 하신 후에 디스코드 봇을 서버에 초대하는 방법은
```
https://discordapp.com/oauth2/authorize?client_id=봇의클라이언트아이디&scope=bot   
```
에서 "봇의클라이언트아이디" 를 교체해주시고 접속하시면 초대가 가능합니다.


<br/>

기능 구현을 위한 가이드
---
YJU가 사용한 모듈   
[모듈이란?](https://wikidocs.net/29)   
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
|requests|네이버 api 이용(번역)|[Python requests 모듈 간단 정리](https://dgkim5360.tistory.com/entry/python-requests)|
|json|api 결과값 사용(번역)|[[파이썬] json 모듈로 JSON 데이터 다루기](https://www.daleseo.com/python-json/)|
|random|랜덤선택(가위바위보)|[랜덤(random) 모듈](https://wikidocs.net/79)|
|selenium|웹 크롤링(유튜브)|[<문과의 파이썬>셀레니움(selenium)](https://brunch.co.kr/@jk-lab/18)|
|bs4|웹 크롤링(유튜브)|[사이트 정보 추출하기 - beautifulsoup 사용법](https://wikidocs.net/85739)|
|re|정규표현식(알파벳 검색)|[점프 투 파이썬 07장 정규표현식](https://wikidocs.net/1669)|
