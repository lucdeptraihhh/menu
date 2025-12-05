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
def countdown(seconds):
    import time
    import itertools

    total = seconds
    bar_length = 30

    # độ sáng nhấp nháy: 1.0 → 0.5 → 1.0
    pulse_cycle = itertools.cycle([1.0, 0.8, 0.6, 0.8])

    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        time_format = f"{mins:02d}:{secs:02d}"

        filled = int(bar_length * (total - seconds) / total)
        unfilled = bar_length - filled

        pulse = next(pulse_cycle)

        # Nhấp nháy bằng cách thay đổi độ sáng ANSI
        bright = f"\033[38;2;255;255;255m"            # sáng
        dim    = f"\033[38;2;150;150;150m"            # mờ

        bar_color = bright if pulse > 0.7 else dim

        bar = bar_color + ("█" * filled) + ("░" * unfilled) + "\033[0m"

        print(f"\r[{bar}] {time_format}", end="")

        time.sleep(0.15)
        seconds -= 1

    print("\n⟹ Hoàn tất vòng lặp!\n")
if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    Write.Print("[1] TikTok Follow\n[2] TikTok Like\n[3] TikTok View\n[4] Facebook Follow\n[5] Facebook Like Fanpage\n[6] Facebook Follow Fanpage\n", Colors.green)
    
    choice = Write.Input("NHẬP LỰA CHỌN: ", Colors.yellow)
    link = Write.Input("NHẬP LINK : ", Colors.cyan)
    key = Write.Input("NHẬP KEY (lấy tại https://like.vn/docs/api): ", Colors.purple)

    Write.Print("\nĐANG CHẠY AUTO!\n", Colors.cyan)

    while True:   # VÒNG LẶP AUTO
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
        Write.Print("ĐANG CÓ ĐƠN...\n", Colors.cyan)

        countdown(180)   # loop mỗi 3 phút