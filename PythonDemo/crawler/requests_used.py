'''
Requests库 API
http://docs.python-requests.org/en/master/api/
'''
# pip install requests
import requests
import json

r = requests.get('http://www.baidu.com')
r.status_code # 200
r.encoding # UTF-8
print(r.cookies)    #<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>

#   参数请求
url_get = "http://httpbin.org/get"
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url_get, params=payload)
print(r.url)

#   增加请求头
payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'content-type': 'application/json'}
r = requests.get(url_get, params=payload, headers=headers)

#   POST请求
url_post = 'http://httpbin.org/post'
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post(url_post, data=payload)
payload = {'some': 'data'}
r = requests.post(url_post, data=json.dumps(payload))

#   Cookies
#   如果一个响应中包含了cookie，那么我们可以利用 cookies 变量来拿到
cookies = dict(cookies_are='working')
r = requests.get(url_get, cookies=cookies)

#   会话对象 Session
s = requests.Session()
#会话全局配置
s.headers.update({'x-test':'true'})
r1 = s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r2 = s.get('http://httpbin.org/cookies')
print(r1.cookies)
print(r2.cookies)


#   SSL证书验证
#r = requests.get('https://kyfw.12306.cn/otn/', verify=True) #需要验证
r = requests.get('https://kyfw.12306.cn/otn/', verify=False) #不需要验证

#   代理
proxies = {
    "https": "http://41.118.132.69:4433"
}

r = requests.post(url_post, proxies=proxies)
print(r.text)