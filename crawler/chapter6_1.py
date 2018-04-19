from urllib.request import urlopen
from bs4 import BeautifulSoup

'''读取纯文本（英文字符）'''
# textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
# print(textPage.read())

'''读取纯文本（含有非英文字符，需要制定编码方式）'''
# textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
# print(str(textPage.read(), 'utf-8'))

'''对爬取到的HTML文本内容指定编码方式'''
html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
content = bytes(content, "UTF-8")
content = content.decode("UTF-8")
print(content)

