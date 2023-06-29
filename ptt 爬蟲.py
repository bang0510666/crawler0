# 抓取網頁原始碼
import urllib.request as req
url="https://www.ptt.cc/bbs/Gossiping/index.html"
# 建立一個 Request物件，附加Request.Header的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# 解析原始碼
import sys
sys.path.append("c:/users/05731/appdata/local/programs/python/python311/lib/site-packages")
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find("div", class_="title")# 尋找 class="title" 的div標籤
print(titles)