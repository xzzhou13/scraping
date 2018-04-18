import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

'''程序首先使用Lambda 函数（第2 章介绍过）选择首页上所有带src 属性的标签。然
后对URL 链接进行清理和标准化，获得文件的绝对路径（而且去掉了外链）。
最后，每个文件都会下载到程序所在文件夹的downloaded 文件里。'''

downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"
def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://"+source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://" + source
    else:
        url = baseUrl + "/" + source
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
        path = absoluteUrl.replace("www.", "")

        path = path.replace(baseUrl, "")
        path = downloadDirectory + path
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        return path

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html)
downloadList = bsObj.findAll(src=True)#Lambda表达式
for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download["src"])
    if fileUrl is not None:
        print(fileUrl)
urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
