import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
ndp_tool="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
#Config
__SHOP__ = 'ĐANG CẬP NHẬT'
__ZALO__ = '0899623990'
__ADMIN__ = 'DINH LUC'
__FACEBOOK__ = 'ĐANG CẬP NHẬT'
__VERSION__ = '1.0'
def banner():
 banner = f"""
\033[1;95m ██████╗ ██╗███╗   ██╗██╗  ██╗    ██╗     ██╗   ██╗ ██████╗
\033[1;37m ██╔══██╗██║████╗  ██║██║  ██║    ██║     ██║   ██║██╔════╝
\033[1;95m ██║  ██║██║██╔██╗ ██║███████║    ██║     ██║   ██║██║     
\033[1;37m ██║  ██║██║██║╚██╗██║██╔══██║    ██║     ██║   ██║██║     
\033[1;95m ██████╔╝██║██║ ╚████║██║  ██║    ███████╗╚██████╔╝╚██████╗
\033[1;37m ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;33mTOOL  VIP 
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;35mADMIN: \033[1;36mDINH LUC
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;36mFB: \033[1;31mĐANG CẬP NHẬT
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mBOX SUPPORT: \033[1;37mĐANG CẬP NHẬT
\033[1;31m────────────────────────────────────────────────────────────
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)
# =======================[ NHẬP KEY ]=======================
os.system("cls" if os.name == "nt" else "clear")
banner()
import json,requests,time
from time import strftime
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTOOL TRAO ĐỔI SUB  \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1.1\033[1;31m] \033[1;32mTOOL TDS FACEBOOK \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1.2\033[1;31m] \033[1;32mTOOL TDS PRO5 \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1.3\033[1;31m] \033[1;32mTOOL TDS PRO5 VIP \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1.4\033[1;31m] \033[1;32mTOOL TDS TIKTOK \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1.5\033[1;31m] \033[1;32mTOOL TDS IG \033[1;31m[\033[1;33mOFF\033[1;31m] ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═══════════════════════╗")
print("\033[1;37m║  \033[1;33mTOOL TƯƠNG TÁC CHÉO  \033[1;37m║")
print("\033[1;37m╚═══════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m2.1\033[1;31m] \033[1;32mTOOL TTC FACEBOOK \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m2.2\033[1;31m] \033[1;32mTOOL TTC PRO5 \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m2.3\033[1;31m] \033[1;32mTOOL TTC TIKTOK \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTOOL TIỆN ÍCH      \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3.1\033[1;31m] \033[1;32mTOOL CHECK XU TRAO ĐỔI SUB \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3.2\033[1;31m] \033[1;32mTOOL CHECK XU TƯƠNG TÁC CHÉO \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3.3\033[1;31m] \033[1;32mTOOL SPAM TIN NHẮN TELEGRAM \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3.4\033[1;31m] \033[1;32mTOOL SPAM SMS VIP  \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3.5\033[1;31m] \033[1;32mTOOL ĐÀO PROXY  \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3.6\033[1;31m] \033[1;32mTOOL BUFF FOLLOW TIKTOK VIP \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3.7\033[1;31m] \033[1;32mTOOL GET ID FACEBOOK \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3.8\033[1;31m] \033[1;32mTOOL BẬT KHIÊN AVATAR FACEBOOK VIP \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║\033[1;33mTOOL PRO5 x FACEBOOK \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m4.1\033[1;31m] \033[1;32mTOOL REG PRO5 VIP \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m4.2\033[1;31m] \033[1;32mTOOL GET TOKEN PRO5 \033[1;31m[\033[1;33mOFF\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m4.3\033[1;31m] \033[1;32mTOOL BUFF FOLLOW BĂNG PRO5 \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m4.4\033[1;31m] \033[1;32mTOOL SHARE ẢO MAX VIP \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m4.5\033[1;31m] \033[1;32mTOOL BUFF STORY BẰNG PRO5 \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m4.6\033[1;31m] \033[1;32mTOOL THẢ BÌNH LUẬN DẠO FACEBOOK \033[1;31m[\033[1;33mON\033[1;31m] ")
print("\033[1;31m────────────────────────────────────────────────────────────")
chon = float(input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;37m: \033[1;33m'))
if chon == 1.1:
    url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/2.php'
    php_code = requests.get(url).text

    # Lưu file PHP vào máy
    with open("2.php", "w") as f:
        f.write(php_code)

    # Chạy file PHP
    print(trang + "ĐANG CHECK LIVE....")
    os.system("php 2.php")
if chon == 1.2:
    url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/5.php'
    php_code = requests.get(url).text

    # Lưu file PHP vào máy
    with open("5.php", "w") as f:
        f.write(php_code)

    # Chạy file PHP
    print(trang + "ĐANG CHECK LIVE....")
    os.system("php 5.php")
if chon == 1.3:
	 url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/1.0.php'
	 php_code = requests.get(url).text
	
	 with open("1.0.php","w") as f:
	     f.write(php_code)
	   
	 print(trang + "ĐANG CHECK LIVE....")
	 os.system("php 1.0.php")
if chon == 1.4:
	 url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/4.php'
	 php_code = requests.get(url).text
	
	 with open("4.php","w") as f:
	     f.write(php_code)
	   
	 print(trang + "ĐANG CHECK LIVE....")
	 os.system("php 4.php")
if chon == 1.5 :
	exec(requests.get('https://run.mocky.io/v3/929d0ec1-24fb-403f-a7a6-5b625188ded0').text)
if chon == 2.1:
	 url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/1.1.php'
	 php_code = requests.get(url).text
	
	 with open("1.1.php","w") as f:
	     f.write(php_code)
	   
	 print(trang + "ĐANG CHECK LIVE....")
	 os.system("php 1.1.php")
if chon == 2.2:
	 url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/1.3.php'
	 php_code = requests.get(url).text
	
	 with open("1.3.php","w") as f:
	     f.write(php_code)
	   
	 print(trang + "ĐANG CHECK LIVE....")
	 os.system("php 1.3.php")

if chon == 2.3:
	 url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/9.php'
	 php_code = requests.get(url).text
	
	 with open("9.php","w") as f:
	     f.write(php_code)
	   
	 print(trang + "ĐANG CHECK LIVE....")
	 os.system("php 9.php")
if chon == 3.1:
	 url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/2.1.php'
	 php_code = requests.get(url).text
	
	 with open("2.1.php","w") as f:
	     f.write(php_code)
	   
	 print(trang + "ĐANG CHECK LIVE....")
	 os.system("php 2.1.php")

if chon == 3.2:
	 url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/2.2.php'
	 php_code = requests.get(url).text
	
	 with open("2.2.php","w") as f:
	     f.write(php_code)
	   
	 print(trang + "ĐANG CHECK LIVE....")
	 os.system("php 2.2.php")
if chon == 3.3:
	 url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/36.php'
	 php_code = requests.get(url).text
	
	 with open("36.php","w") as f:
	     f.write(php_code)
	   
	 print(trang + "ĐANG CHECK LIVE....")
	 os.system("php 36.php")
if chon == 3.4:
	 url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/4.php'
	 php_code = requests.get(url).text
	
	 with open("4.php","w") as f:
	     f.write(php_code)
	   
	 print(trang + "ĐANG CHECK LIVE....")
	 os.system("php 4.php")
if chon == 3.5:
	 url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/35.php'
	 php_code = requests.get(url).text
	
	 with open("35.php","w") as f:
	     f.write(php_code)
	   
	 print(trang + "ĐANG CHECK LIVE....")
	 os.system("php 35.php")
if chon == 3.6:
    url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/hd.py'
    py_code = requests.get(url).text

    with open("hd.py", "w") as f:
        f.write(py_code)

    print(trang + "ĐANG CHECK LIVE....")
    os.system("python hd.py")

if chon == 3.7:
	 url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/13.php'
	 php_code = requests.get(url).text
	
	 with open("13.php","w") as f:
	     f.write(php_code)
	   
	 print(trang + "ĐANG CHECK LIVE....")
	 os.system("php 13.php")
if chon == 3.8:
	 url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/12.php'
	 php_code = requests.get(url).text
	
	 with open("12.php","w") as f:
	     f.write(php_code)
	   
	 print(trang + "ĐANG CHECK LIVE....")
	 os.system("php 12.php")
if chon == 4.1:
	 url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/1.9.php'
	 php_code = requests.get(url).text
	
	 with open("1.9.php","w") as f:
	     f.write(php_code)
	   
	 print(trang + "ĐANG CHECK LIVE....")
	 os.system("php 1.9.php")
if chon == 4.2:
	 url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/1.5.php'
	 php_code = requests.get(url).text
	
	 with open("1.5.php","w") as f:
	     f.write(php_code)
	   
	 print(trang + "ĐANG CHECK LIVE....")
	 os.system("php 1.5.php")
if chon == 4.3:
	 url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/1.7.php'
	 php_code = requests.get(url).text
	
	 with open("1.7.php","w") as f:
	     f.write(php_code)
	   
	 print(trang + "ĐANG CHECK LIVE....")
	 os.system("php 1.7.php")
if chon == 4.4:
	 url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/10.php'
	 php_code = requests.get(url).text
	
	 with open("10.php","w") as f:
	     f.write(php_code)
	   
	 print(trang + "ĐANG CHECK LIVE....")
	 os.system("php 10.php")
if chon == 4.5:
	 url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/2.0.php'
	 php_code = requests.get(url).text
	
	 with open("2.0.php","w") as f:
	     f.write(php_code)
	 print(trang + "ĐANG CHECK LIVE....")
	 os.system("php 2.0.php")    
if chon == 4.6:
	 url = 'https://raw.githubusercontent.com/lucdeptraihhh/menu/refs/heads/main/1.4.php'
	 php_code = requests.get(url).text
	
	 with open("1.4.php","w") as f:
	     f.write(php_code)
	   
	 print(trang + "ĐANG CHECK LIVE....")
	 os.system("php 1.4.php")
 
else :
	print (" NHẬP SAI RỒI 🥺 ")
	exit()
