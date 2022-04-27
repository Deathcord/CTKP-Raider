import requests
import asyncio
import sys
import requests
import time
import colorama
from colorama import Fore, Style
import threading
import os

with open("tokens.txt") as f:
        tokens = f.read().split("\n")

def Setup():
    os.system('cls')
    print(Fore.CYAN + 'CTKP-Raider Beta' + Fore.RESET)
    print(Fore.CYAN + '\n\n     1 >>' + Fore.RESET + ' 入室 (招待コード)' + Fore.RESET)

def Start():
        command = list(input('\n\n   >> ').split(' '))
        if command[0] == "1":
                invite = command[1]
                threading.Thread(target=Join(invite)).start()

headers = {
	"x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjkzLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTMuMCIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAwODA0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
        "x-context-properties": "eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjQyNDQ0NzAyMzc2NTUyMDM4NiIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI2MDI3MDU3MzIzMzYzNTMyOTAiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9",
	"sec-fetch-dest": "empty",
	"x-debug-options": "bugReporterEnabled",
	"sec-fetch-mode": "cors",
	"sec-fetch-site": "same-origin",
	"accept": "*/*",
	"accept-language": "en-GB",
	"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.16 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
	"TE": "trailers"
}

headers2 = {
    "accept": "*/*",
    "authority": "discord.com",
    "method": "POST",
    "path": "/api/v9/auth/register",
    "scheme": "https",
    "origin": "discord.com",
    "referer": "discord.com/register",
    "x-debug-options": "bugReporterEnabled",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-Type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0OTY3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin"
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
        for token in tokens:
                headers["authorization"] = token
                headers["x-fingerprint"] = getfingerprint()
                response = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers, cookies=getcookie())
                print(response.status_code)
                time.sleep(2)
                Setup()
                Start()

Setup()
Start()
