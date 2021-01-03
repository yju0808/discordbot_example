#필요한 모듈을 import 한다
import discord
import requests
import json
import random
from selenium import webdriver
import bs4
import re

#보여주면 안되는 데이터를 파일에서 불러온다
secret_file = open("discordbot\secret.txt","r")
secret = secret_file.read().split("\n")
secret_file.close()

#디스코드 봇 토큰
token = secret[0]
#네이버 api ID
client_id = secret[1]
#네이버 api 비밀번호
client_secret = secret[2]

#번역을 위한 함수 번역 소스 언어, 번역 목적 언어, 번역하려는 말을 매개변수로 받는다
def translate(source,target,text):
    #네이버 api URL
    URL = 'https://openapi.naver.com/v1/papago/n2mt'

    #api 요청을 위한 헤더와 변수를 작성한다
    headers = {'X-Naver-Client-Id': client_id,
            'X-Naver-Client-Secret': client_secret}
    data = {'source': source, 'target': target, 'text': text}

    #네이버 api에 요청을 보내고 받아온다
    response = json.loads(requests.post(URL, headers=headers, data=data).text)

    #번역된 결과를 리턴한다
    return response["message"]["result"]["translatedText"]


class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        game = discord.Game("!명령어를 입력하세요")
        #온라인, 게임중으로 설정한다
        await client.change_presence(status=discord.Status.online,activity=game)

    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):
        #channel 변수에 메시지가 전송된 채널을 담는다
        channel = message.channel

        #포괄적인 예외처리
        try:
            #봇이 보낸거면 대답하지 않는다
            if message.author.bot:
                return None

            #!명령어가 입력되었을 때
            if message.content == "!명령어":
                #embed 객체를 생성한다
                embed = discord.Embed(
                    title="안녕하세요", description="명령어를 소개합니다", colour=0x5CD1E5)
                #add_field 메서드를 이용해 데이터를 채운다
                embed.add_field(name="!제작가이드", value="디스코드 봇 제작 가이드 링크를 보내드려요", inline=False)
                embed.add_field(name="!말해", value="채팅을 보내드려요", inline=False)
                embed.add_field(name="!임베드", value="임베드를 보내드려요", inline=False)
                embed.add_field(name="!가위바위보 가위/바위/보", value="저랑 가위바위보를 합니다!", inline=False)
                embed.add_field(name="!번역영한 번역할말", value="영-->한 번역을 해드려요", inline=False)
                embed.add_field(name="!번역한영 번역할말", value="한-->영 번역을 해드려요", inline=False)
                embed.add_field(name="!유튜브검색 검색어", value="유튜브에서 검색어를 검색해드려요", inline=False)
                embed.add_field(name="!이미지검색 검색어", value="이미지를 검색해드려요", inline=False)
                embed.add_field(name="!계산기 수식", value="수식을 계산해드려요", inline=False)

                #채널에 embed를 보낸다
                await channel.send(embed=embed)
                return None

            #!제작가이드 가 입력되었을 때
            if message.content == "!제작가이드":
                #embed 객체를 생성한다
                embed = discord.Embed(
                    title="디스코드 봇 제작 가이드", description="https://github.com/yju0808/discordbot_example", colour=0x5CD1E5)

                #채널에 embed를 보낸다
                await channel.send(embed=embed)
                return None

            #!말해가 입력되었을 때
            if message.content == "!말해":
                #채널에 메시지를 보낸다
                await channel.send(content="안녕하세요!!")

            #!임베드가 입력되었을때
            if message.content == "!임베드":
                #embed 객체를 생성한다
                embed = discord.Embed(
                    title="안녕하세요", description="", colour=0x5CD1E5)
                embed.add_field(name="이것이 임베드랍니다", value="ㅎㅎ", inline=False)
                #채널에 embed를 보낸다
                await channel.send(embed=embed)
                return None

            #!가위바위보가 입력되었을 때
            if message.content.startswith("!가위바위보"):
                #유저의 선택을 가져온다
                user_pick = message.content.split()[1]
                #가위바위보중 랜덤으로 하나를 선택한다(봇의 선택)
                bot_pick = random.choice(["가위","바위","보"])


                #유저의 선택이 가위,바위,보 중 하나가 아닐경우 메시지를 보내고 끝낸다
                if user_pick != "가위" and user_pick != "보" and user_pick != "바위":
                    await channel.send(content="제대로된 입력이 아닙니다!! 가위/바위/보 중 선택하세요")

                    return None
                #비겼을 경우
                if user_pick == bot_pick:
                    result = "비겼습니다!!"
                #유저가 이겼을 경우
                elif user_pick == "가위" and bot_pick == "보" or user_pick == "바위" and bot_pick == "가위" or user_pick == "보" and bot_pick == "바위":
                    result = "이기셨네요!!"
                #봇이 이겼을 경우
                else:
                    result = "제가 이겼네요 ㅎㅎ"
                #embed 객체 생성
                embed = discord.Embed(
                    title="가위바위보 결과", description="당신의 선택 : {}\n제 선택 : {}\n\n{}".format(user_pick,bot_pick,result), colour=0x5CD1E5)

                #채널에 emebed를 보낸다
                await channel.send(embed=embed)
                return None

            #!번역한영이 입력되었을 때
            if message.content.startswith("!번역한영"):
                #유저가 번역하고자하는 메시지를 가져오고 translate함수에 넘긴다
                msg = translate("ko","en",message.content[5:])
                #embed객체 생성
                embed = discord.Embed(colour=0x5CD1E5)
                embed.add_field(name="번역결과", value=msg, inline=False)
                #채널에 embed를 보낸다
                await channel.send(embed=embed)
                return None

            #!번역영한이 입력되었을 때
            if message.content.startswith("!번역영한"):
                #유저가 번역하고자하는 메시지를 가져오고 translate함수에 넘긴다
                msg = translate("en","ko",message.content[5:])
                #embed객체 생성
                embed = discord.Embed(colour=0x5CD1E5)
                embed.add_field(name="번역결과", value=msg, inline=False)
                #채널에 embed를 보낸다
                await channel.send(embed=embed)
                return None

            #!유튜브검색이 입력되었을 때
            if message.content.startswith("!유튜브검색"):
                #시간이 꽤 걸리기 때문에 일단 검색중... 메시지를 보낸다
                searching_message =  await channel.send(content='검색중...')
                #웹 크롤링을 위한 크롬드라이버 셋팅
                chromedriver_dir = "discordbot\chromedriver.exe"
                options = webdriver.ChromeOptions()
                options.add_argument("headless")
                #driver 객체를 생성한다
                driver = webdriver.Chrome(chromedriver_dir,chrome_options=options)
                driver.get('https://www.youtube.com/results?search_query=' + message.content[6:])
                #beautifulsoup를 이용해 html 소스를 구한뒤 크롤링한다
                html = bs4.BeautifulSoup(driver.page_source, 'html.parser')
                result = html.find('a', {'id': 'video-title'})
                #embed 객체 생성
                embed = discord.Embed(title="검색결과", description='{}에 대한 검색 결과입니다'.format(message.content[6:]),colour=0xFF0000)
                #보냈던 검색중... 메시지를 삭제한다
                await searching_message.delete()
                #채널에 embed를 보낸다
                await channel.send(embed=embed)
                #채널에 검색결과를 보낸다
                await channel.send(content='https://www.youtube.com' + result.get("href"))
                return None

            #!이미지검색이 입력되었을 때
            if message.content.startswith("!이미지검색"):
                #네이버 api 요청 URL
                URL = 'https://openapi.naver.com/v1/search/image?query={}&display=1'.format(message.content[6:])
                #요청을 위한 헤더 설정
                headers = {'X-Naver-Client-Id': client_id,
                            'X-Naver-Client-Secret': client_secret}
                #요청한 결과에서 이미지파일 링크만 가져온다
                image = json.loads(requests.get(URL,headers=headers).text)['items'][0]['link']
                #embed 객체를 생성하고 set_image 메서드로 이미지를 설정해준다
                embed = discord.Embed(title="검색결과", description='{}에 대한 검색 결과입니다'.format(message.content[6:]),colour=0x5CD1E5)
                embed.set_image(url=image)
                #채널에 embed를 보낸다
                await channel.send(embed=embed)
                return None
                

            #!계산기가 입력되었을 때
            if message.content.startswith("!계산기"):
                #유저가 보낸 수식을 가져온다
                mathematical_expression = message.content[4:]

                #수식에 알파벳이 없는지 확인한다 (eval함수는 파이썬 표현식을 실행할 수 있는 함순데 위험한 표현식도 실행이 될 수 있으므로 영어로 된 코드입력 방지를 위해서 알파벳이 포함됬는지 확인한다)
                if re.search('[a-zA-Z]', mathematical_expression) == None:
                    #수식에 알파벳이 없을 경우에만 정상적으로 계산을 한다
                     embed = discord.Embed(title="계산결과", description=str(eval(mathematical_expression)),colour=0x5CD1E5)
                     await channel.send(embed=embed)
                     return None

                else:
                    #수식에 알파벳이 있을 경우엔 예외를 던진다(밖에서 예외처리를 해서 알아서 잡힐것이다.)
                    raise Exception
        #예외처리
        except Exception as e:
            print(e)
            #뭔가 에러가 났을 경우엔 이렇게 보낸다.
            await channel.send("뭔가 잘못 입력하신듯 합니다..")
            return None
            

#파일을 실행했을때 실행될 함수
if __name__ == "__main__":
    print("실행중")
    #client 객체를 생성한다
    client = chatbot()
    #run 메서드를 실행한다
    client.run(token)
