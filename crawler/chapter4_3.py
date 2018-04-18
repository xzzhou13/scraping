from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime
import json
import random
import re

'''在爬虫中使用API'''
random.seed(datetime.datetime.now())
#获得当前页面的所有词条链接
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

#获得某词条链接的历史页面并找出编辑历史的IP地址
def getHistoryIPs(pageUrl):
    # Format of revision history pages is:
    # http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title=" + pageUrl + "&action=history"
    #print("history url is: " + historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    # finds only the links with class "mw-anonuserlink" which has IP addresses
    # instead of usernames
    ipAddresses = bsObj.findAll("a", {"class": "mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

'''使用API获得相应IP地址的国家号'''
def getCountry(ipAddress):
    try:
        #such as http://freegeoip.net/json/39.36.182.41
        response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson["region_name"]


links = getLinks("/wiki/Python_(programming_language)")

while (len(links) > 0):
    for link in links:
        print("-------------------")
        print(link.attrs["href"])
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP + " is from " + country)

    newLink = links[random.randint(0, len(links) - 1)].attrs["href"]
    links = getLinks(newLink)
