import requests

'''使用API的另一种方法'''
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'#Hacker News上当前最热门的文章的ID
r = requests.get(url)
print('Status code:', r.status_code)
results_list = r.json()
print(results_list)