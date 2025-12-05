import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import requests
except ImportError:
    install("requests")
    import requests

try:
    from pystyle import Colors, Write, Anime
except ImportError:
    install("pystyle")
    from pystyle import Colors, Write, Anime

import requests
import os
import time
from pystyle import Colors, Write, Anime

def mua_follow_tiktok(link, key):
    url = "https://like.vn/api/mua-follow-tiktok/order"
    return mua_dichvu(link, key, url, server_order=6, amount=10)

def mua_like_tiktok(link, key):
    url = "https://like.vn/api/mua-like-tiktok/order"
    return mua_dichvu(link, key, url, server_order=6, amount=10)

def mua_view_tiktok(link, key):
    url = "https://like.vn/api/mua-view-tiktok/order"
    return mua_dichvu(link, key, url, server_order=4, amount=1000)

def mua_follow_facebook(link, key):
    url = "https://like.vn/api/mua-follow-facebook/order"
    return mua_dichvu(link, key, url, server_order=6, amount=10)

def mua_like_fanpage_facebook(link, key):
    url = "https://like.vn/api/mua-like-fanpage-facebook/order"
    return mua_dichvu(link, key, url, server_order=7, amount=10)

def mua_follow_fanpage_facebook(link, key):
    url = "https://like.vn/api/mua-like-fanpage-facebook/order"
    return mua_dichvu(link, key, url, server_order=6, amount=10)

def mua_dichvu(link, key, url, server_order, amount):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "x-requested-with": "XMLHttpRequest",
        "Origin": "https://like.vn",
        "Referer": "https://like.vn/mua-follow-tiktok",
        "api-token": key,
        "x-csrf-token": "<YOUR_CSRF_TOKEN>",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.6,en;q=0.5",
        "sec-ch-ua": '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }

    data = {
        "objectId": link,
        "server_order": server_order,
        "free": 1,
        "giftcode": "",
        "amount": amount,
        "note": ""
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        res_json = response.json()
        message = res_json.get("message", "Lỗi server!")
        return message
    except requests.exceptions.RequestException as e:
        return f"Lỗi kết nối: {e}"
    except ValueError:
        return "Server nghẽn, vui lòng thử lại sau!"

def animated_message(message):
    print(message)

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    Write.Print("[1] TikTok Follow\n[2] TikTok Like\n[3] TikTok View\n[4] Facebook Follow\n[5] Facebook Like Fanpage\n[6] Facebook Follow Fanpage\n", Colors.green)
    
    choice = Write.Input("Nhập Lựa Chọn: ", Colors.yellow)
    link = Write.Input("Nhập Link: ", Colors.cyan)
    key = Write.Input("Nhập Key (lấy tại https://like.vn/docs/api): ", Colors.purple)

    while True:
        if choice == "1":
            result = mua_follow_tiktok(link, key)
        elif choice == "2":
            result = mua_like_tiktok(link, key)
        elif choice == "3":
            result = mua_view_tiktok(link, key)
        elif choice == "4":
            result = mua_follow_facebook(link, key)
        elif choice == "5":
            result = mua_like_fanpage_facebook(link, key)
        elif choice == "6":
            result = mua_follow_fanpage_facebook(link, key)
        else:
            Write.Print("Lựa chọn không hợp lệ!", Colors.red)
            break

        animated_message(result)
        Write.Print("Có đơn đang chạy, chờ 3 phút thử lại..\n", Colors.cyan)
        time.sleep(180)
