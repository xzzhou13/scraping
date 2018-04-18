from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

'''找出当前网页中所有的词条链接'''
# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html,"html.parser")
# for link in bsObj.find("div",{'id':'bodyContent'}).findAll('a',href = re.compile('^(/wiki/)((?!:).)*$')):
#     #print(link)
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

'''从当前网页词条链接列表中随机选一个链接获取网页并找出其词条链接，重复执行，直至网页中没有词条链接'''
# random.seed(datetime.datetime.now())#用系统当前时间生成一个随机数生成器
# def getLinks(articleUrl):
#     html = urlopen("http://en.wikipedia.org"+articleUrl)
#     bsObj = BeautifulSoup(html)
#     return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
#                         href=re.compile("^(/wiki/)((?!:).)*$"))
#
# links = getLinks("/wiki/Kevin_Bacon")
# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
#     print(newArticle)
#     links = getLinks(newArticle)

'''采集整个网站的所有网页——采用链接去重简化爬虫任务'''
# pages = set()
# def getLinks(pageUrl):
#     global pages
#     html = urlopen("http://en.wikipedia.org"+pageUrl)
#     bsObj = BeautifulSoup(html)
#     try:
#         print(bsObj.h1.get_text())
#         print(bsObj.find(id="mw-content-text").findAll("p")[0])
#         print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
#     except AttributeError:
#         print("页面缺少一些属性！不过不用担心！")
#
#      #针对所有内链（不区分词条链接和其它链接）
#     for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 # 我们遇到了新页面
#                 newPage = link.attrs['href']
#                 print("----------------\n"+newPage)
#                 pages.add(newPage)
#                 getLinks(newPage)
#                 getLinks("")

'''在互联网上采集——借助外链'''
# from urllib.request import urlparse
#
# pages = set()
# random.seed(datetime.datetime.now())
#
# # 获取页面所有内链的列表
# def getInternalLinks(bsObj, includeUrl):
#     includeUrl = urlparse(includeUrl).scheme + '://'+urlparse(includeUrl).netloc
#     internalLinks = []
#     # 找出所有以"/"开头的链接
#     for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
#         if link.attrs['href'] is not None:
#             if link.attrs['href'] not in internalLinks:
#                 if link.attrs['href'].startwith('/'):
#                     internalLinks.append(includeUrl + link.attrs['href'])
#                 else:
#                     internalLinks.append(link.attrs['href'])
#     return internalLinks
#
# # 获取页面所有外链的列表
# def getExternalLinks(bsObj, excludeUrl):
#     externalLinks = []
#     # 找出所有以"http"或"www"开头且不包含当前URL的链接
#     for link in bsObj.findAll("a",
#         href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
#         if link.attrs['href'] is not None:
#             if link.attrs['href'] not in externalLinks:
#                 externalLinks.append(link.attrs['href'])
#     return externalLinks
#
# def getRandomExternalLink(startingPage):
#     html = urlopen(startingPage)
#     bsObj = BeautifulSoup(html, "html.parser")
#     externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
#     if len(externalLinks) == 0:
#         print('No external links.')
#         domain= urlparse(startingPage).scheme + '://' + urlparse(startingPage).netloc
#         internalLinks = getInternalLinks(bsObj, domain)
#         return getRandomExternalLink(internalLinks[random.randint(0,
#                                     len(internalLinks)-1)])
#     else:
#         return externalLinks[random.randint(0, len(externalLinks)-1)]
#
# def followExternalOnly(startingSite):
#     externalLink = getRandomExternalLink("http://oreilly.com")
#     print("随机外链是："+externalLink)
#     followExternalOnly(externalLink)
#
#
# followExternalOnly("http://oreilly.com")

'''另一种写法，不用urlparse'''
pages = set()
random.seed(datetime.datetime.now())

# 获取页面所有内链的列表
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # 找出所有以"/"开头的链接
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

# 获取页面所有外链的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 找出所有以"http"或"www"开头且不包含当前URL的链接
    for link in bsObj.findAll("a",
    href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(bsObj, splitAddress(startingPage)[0])
        return getRandomExternalLink(internalLinks[random.randint(0,
                                    len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink("http://oreilly.com")
    print("随机外链是："+externalLink)
    followExternalOnly(externalLink)


followExternalOnly("http://oreilly.com")