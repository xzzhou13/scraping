from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

'''程序从http://pythonscraping.com 下载logo 图片，然后在程序运行的文件夹里保存为logo.jpg 文件'''
html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html)
imageLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
urlretrieve (imageLocation, "logo.jpg")#保存下载文件的方法


