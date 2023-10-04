#màu
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
#Library
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import requests
import base64, json, os, sys
from datetime import date
from datetime import datetime
from time import sleep,strftime
time = (datetime.now().strftime('%H:%M:%S'))
import socket
from pystyle import *
#====#
ip = requests.get('https://checkip.amazonaws.com').text.strip()
info = f'{red}[{trang}+{red}]'
#Check Key

#NORI-TOOL
#Nori Tool
day = (datetime.now().strftime('%d/%m/%Y'))
time = (datetime.now().strftime('%H:%M:%S'))
ip = requests.get('https://checkip.amazonaws.com').text.strip()
info = f'{red}[{trang}+{red}]'
hd = f'{red}[{trang}•_•{red}] {trang}=> {green}'
gachngang = f'{red}────────────────────────────────────────────────────────────────────────'

def banner():
 os.system("cls" if os.name == "nt" else "clear")
 banner = f'''{xduong}███╗  ██╗ █████╗ ██████╗ ██╗      ████████╗ █████╗  █████╗ ██╗
{xduong}████╗ ██║██╔══██╗██╔══██╗██║      ╚══██╔══╝██╔══██╗██╔══██╗██║
{xduong}██╔██╗██║██║  ██║██████╔╝██║█████╗   ██║   ██║  ██║██║  ██║██║
{xduong}██║╚████║██║  ██║██╔══██╗██║╚════╝   ██║   ██║  ██║██║  ██║██║
{xduong}██║ ╚███║╚█████╔╝██║  ██║██║         ██║   ╚█████╔╝╚█████╔╝███████╗
{xduong}╚═╝  ╚══╝ ╚════╝ ╚═╝  ╚═╝╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚══════╝
{red}────────────────────────────────────────────────────────────────────────
{info}{tim} Admin: Quang Đức
{info}{yellow} Zalo: 0364218196
{info}{xnhac} Box Zalo: https://zalo.me/g/ocazmg167
{info}{blue} Youtube:
{red}────────────────────────────────────────────────────────────────────────
{info}{luc} Chúc Bạn Dùng Tool Vui Vẻ
{info}{luc} IP Hiện Tại Của Bạn Là:{trang} {ip}
{info}{luc} Hôm Nay Là Ngày:{trang} {day}
{info}{luc} Bạn Vào Tool Lúc:{trang} {time}
{red}────────────────────────────────────────────────────────────────────────'''
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush()
  sleep(0.00125)
banner()
tool = f"""
{do}╔═════════════════════╗
{do}║  {vang}Tool Trao Đổi Sub  {do}║
{do}╚═════════════════════╝
{hd}Nhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTool TDS FB
{hd}Nhập Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mTool TDS Pro5
{hd}Nhập Số \033[1;31m[\033[1;33m3\033[1;31m] \033[1;32mTool TDS Tiktok
{red}────────────────────────────────────────────────────────────────────────
{do}╔══════════════════════╗
{do}║ {vang}Tool Tương Tác Chéo  {do}║
{do}╚══════════════════════╝
{hd}Nhập Số \033[1;31m[\033[1;33m4\033[1;31m] \033[1;32mTool TTC FB {trang}[Đang Update]
{hd}Nhập Số \033[1;31m[\033[1;33m5\033[1;31m] \033[1;32mTool TTC Pro5 {trang}[Đang Update]
{hd}Nhập Số \033[1;31m[\033[1;33m6\033[1;31m] \033[1;32mTool TTC Tiktok {trang}[Đang Update]
{red}────────────────────────────────────────────────────────────────────────
{do}╔═════════════════════╗
{do}║  {vang}  Tool TikTok      {do}║
{do}╚═════════════════════╝
{hd}Nhập Số \033[1;31m[\033[1;33m7\033[1;31m] \033[1;32mTool Buff View TikTok {trang}[Đang Update]
{hd}Nhập Số \033[1;31m[\033[1;33m8\033[1;31m] \033[1;32mTool Buff Tim TikTok {trang}[Đang Update]
{red}────────────────────────────────────────────────────────────────────────
{do}╔═════════════════════╗
{do}║     {vang}Tool Pro5       {do}║
{do}╚═════════════════════╝
{hd}Nhập Số \033[1;31m[\033[1;33m9\033[1;31m] \033[1;32mTool REG PRO5 + UP AVT
{hd}Nhập Số \033[1;31m[\033[1;33m10\033[1;31m] \033[1;32mTool Buff View Story Pro5 
{hd}Nhập Số \033[1;31m[\033[1;33m11\033[1;31m] \033[1;32mTool Buff Reaction Bằng Page Pro5 {trang}[Đang Update]
{hd}Nhập Số \033[1;31m[\033[1;33m12\033[1;31m] \033[1;32mTool Share Max Speed Bằng Token Pro5 {trang}[Đang Update]
{hd}Nhập Số \033[1;31m[\033[1;33m13\033[1;31m] \033[1;32mTool Buff Follow Bằng Page Pro5
{hd}Nhập Số \033[1;31m[\033[1;33m14\033[1;31m] \033[1;32mTool Buff Mem Group Bằng Page Pro5
{hd}Nhập Số \033[1;31m[\033[1;33m15\033[1;31m] \033[1;32mTool Chuyển Quyền Admin Page Pro5
{hd}Nhập Số \033[1;31m[\033[1;33m16\033[1;31m] \033[1;32mTool Buff Comment Pro5 {trang}[Đang Update]
{hd}Nhập Số \033[1;31m[\033[1;33m17\033[1;31m] \033[1;32mTool Kích Hoạt Pro5 {trang}[Đang Update]
{red}────────────────────────────────────────────────────────────────────────"""
#{do}╔══════════════════════════╗
#{do}║ {vang}Tool Công Cụ + Tiện Ích  {do}║
#{do}╚══════════════════════════╝

print(tool)
chon = input(f'{hd}{luc}Nhập Lựa Chọn: {vang}')

#TDS FB
if chon == '1':
 exec(requests.get('https://run.mocky.io/v3/d6779d25-6c38-46f7-ab4e-ef315510804e').text)
#TDS PRO5
if chon == '2':
 exec(requests.get('https://run.mocky.io/v3/d9703b27-b0aa-4a70-82fc-e88be6013c8d').text)
#TDS TIKTOK
if chon == '3':
 exec(requests.get('https://run.mocky.io/v3/207b5835-e1f8-4819-8304-e05305ffa328').text)
#TTC FB
if chon == '4':
 exec(requests.get('').text)
#TTC PRO5
if chon == '5':
 exec(requests.get('').text)
#TTC TIKTOK
if chon == '6':
 exec(requests.get('').text)
#BUFF VIEW TIKTOK
if chon == '7':
 exec(requests.get('').text)
#BUFF TIM TIKTOK
if chon == '8':
 exec(requests.get('').text)
#REG PRO5
if chon == '9':
 exec(requests.get('https://run.mocky.io/v3/b33ca81c-857f-40c3-b01e-1d428421ebd4').text)
#BUFF VIEW STORY PRO5
if chon == '10':
 exec(requests.get('https://run.mocky.io/v3/02e57ffa-bdd0-488d-9924-f726210a4181').text)
#BUFF CẢM XÚC PRO5
if chon == '11':
 exec(requests.get('').text)
#BUFF SHARE PRO5
if chon == '12':
 exec(requests.get('').text)
#BUFF FL PRO5
if chon == '13':
 exec(requests.get('https://run.mocky.io/v3/fbcc0689-30fb-45b5-9c12-210effae8e5d').text)
#BUFF MEM PRO5
if chon == '14':
 exec(requests.get('https://run.mocky.io/v3/a77b9ef9-5d02-42f6-81ed-7f129b263ae8').text)
#CHANGE PRO5
if chon == '15':
 exec(requests.get('https://run.mocky.io/v3/02515bfa-a765-4b74-afce-f5abd232655d').text)
#BUFF CMT
if chon == '16':
 exec(requests.get('').text)
#KÍCH PRO5
if chon == '17':
 exec(requests.get('').text)
