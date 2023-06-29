import urllib.request

def check_url(url):
    try:
        response = urllib.request.urlopen(url)
        return True  # 網址可存取
    except urllib.error.URLError:
        return False  # 網址無法存取

# 測試網址
url = "https://www.ptt.cc/bbs/Gossiping/index.html"
if check_url(url):
    print("網址可存取")
else:
    print("網址無法存取")







