import json
from urllib.request import urlopen

'''使用API'''
# def getCountry(ipAddress):
#     response = urlopen("http://freegeoip.net/json/"+ipAddress)
#     result = response.read().decode('utf-8')
#     responseJson = json.loads(result)#将返回的信息用JSON格式存储
#     print(responseJson)
#     return responseJson.get("country_code")
#
#
# print(getCountry("50.78.253.58"))

'''解析JSON格式的数据'''
#Python将JSON转换成字典，将JSON数组转换成列表，将JSON字符串转换成python字符串
jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],' \
             ' "arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'
jsonObj = json.loads(jsonString)
print(jsonObj.get("arrayOfNums"))
print(jsonObj.get("arrayOfNums")[1])
print(jsonObj.get("arrayOfNums")[1].get("number")+
jsonObj.get("arrayOfNums")[2].get("number"))
print(jsonObj.get("arrayOfFruits")[2].get("fruit"))