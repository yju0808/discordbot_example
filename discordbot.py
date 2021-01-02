import discord
import requests
import json
import random
from selenium import webdriver
import bs4
import re

secret_file = open("discordbot\secret.txt","r")
secret = secret_file.read().split("\n")
secret_file.close()

token = secret[0]
client_id = secret[1]
client_secret = secret[2]

def translate(source,target,text):
    URL = 'https://openapi.naver.com/v1/papago/n2mt'

    headers = {'X-Naver-Client-Id': client_id,
            'X-Naver-Client-Secret': client_secret}
    data = {'source': source, 'target': target, 'text': text}

    response = json.loads(requests.post(URL, headers=headers, data=data).text)

    return response["message"]["result"]["translatedText"]


class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):

        game = discord.Game("!명령어를 입력하세요")
        await client.change_presence(status=discord.Status.online,activity=game)

    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):
        channel = message.channel

        try:
            if message.author.bot:
                return None

            if message.content == "!명령어":
                embed = discord.Embed(
                    title="안녕하세요", description="명령어를 소개합니다", colour=0x5CD1E5)
                embed.add_field(name="!말해", value="채팅을 보내드려요", inline=False)
                embed.add_field(name="!embed", value="embed를 보내드려요", inline=False)
                embed.add_field(name="!가위바위보 가위/바위/보", value="저랑 가위바위보를 합니다!", inline=False)
                embed.add_field(name="!번역영한 번역할말", value="영-->한 번역을 해드려요", inline=False)
                embed.add_field(name="!번역한영 번역할말", value="한-->영 번역을 해드려요", inline=False)
                embed.add_field(name="!유튜브검색 검색어", value="유튜브에서 검색어를 검색해드려요", inline=False)
                embed.add_field(name="!계산기 수식", value="수식을 계산해드려요", inline=False)

                await channel.send(embed=embed)
                return None


            if message.content == "!말해":
                await channel.send(content="안녕하세요!!")


            if message.content == "!embed":
                embed = discord.Embed(
                    title="안녕하세요", description="", colour=0x5CD1E5)
                embed.add_field(name="이것이 embed랍니다", value="ㅎㅎ", inline=False)

                await channel.send(embed=embed)
                return None


            if message.content.startswith("!가위바위보"):
                user_pick = message.content.split()[1]
                bot_pick = random.choice(["가위","바위","보"])


                #early exit
                if user_pick != "가위" and user_pick != "보" and user_pick != "바위":
                    await channel.send(content="제대로된 입력이 아닙니다!! 가위/바위/보 중 선택하세요")

                    return None
                
                if user_pick == bot_pick:
                    result = "비겼습니다!!"
                
                elif user_pick == "가위" and bot_pick == "보" or user_pick == "바위" and bot_pick == "가위" or user_pick == "보" and bot_pick == "바위":
                    result = "이기셨네요!!"
                
                else:
                    result = "제가 이겼네요 ㅎㅎ"

                embed = discord.Embed(
                    title="가위바위보 결과", description="당신의 선택 : {}\n제 선택 : {}\n\n{}".format(user_pick,bot_pick,result), colour=0x5CD1E5)


                await channel.send(embed=embed)
                return None


            if message.content.startswith("!번역한영"):
                msg = translate("ko","en",message.content[5:])

                embed = discord.Embed(colour=0x5CD1E5)
                embed.add_field(name="번역결과", value=msg, inline=False)

                await channel.send(embed=embed)
                return None


            if message.content.startswith("!번역영한"):
                msg = translate("en","ko",message.content[5:])

                embed = discord.Embed(colour=0x5CD1E5)
                embed.add_field(name="번역결과", value=msg, inline=False)

                await channel.send(embed=embed)
                return None


            if message.content.startswith("!유튜브검색"):

                searching_message =  await channel.send(content='검색중...')

                chromedriver_dir = "discordbot\chromedriver.exe"
                options = webdriver.ChromeOptions()
                options.add_argument("headless")

                driver = webdriver.Chrome(chromedriver_dir,chrome_options=options)
                driver.get('https://www.youtube.com/results?search_query=' + message.content[6:])

                html = bs4.BeautifulSoup(driver.page_source, 'html.parser')
                result = html.find('a', {'id': 'video-title'})

                embed = discord.Embed(title="검색결과", description='{}에 대한 검색 결과입니다'.format(message.content[6:]),colour=0xFF0000)

                await searching_message.delete()
                await channel.send(embed=embed)
                await channel.send(content='https://www.youtube.com' + result.get("href"))
                return None

            
            if message.content.startswith("!계산기"):

                mathematical_expression = message.content[4:]

                #safe eval을 위한 코드 입력 방지
                if re.search('[a-zA-Z]', mathematical_expression) == None:
                     embed = discord.Embed(title="계산결과", description=eval(mathematical_expression),colour=0x5CD1E5)
                     await channel.send(embed=embed)
                     return None

                else:
                    raise Exception





        except Exception as e:
            print(e)
            await channel.send("뭔가 잘못 입력하신듯 합니다..")
            return None
            






if __name__ == "__main__":
    print("실행중")
    client = chatbot()
    client.run(token)
