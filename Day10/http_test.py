
import requests

# 发送GET请求并获取响应内容
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Request failed with status code:", response.status_code)


# 发送带参数的GET请求
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "Shanghai,CN",
    "appid": "your_api_key"
}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Request failed with status code:", response.status_code)


# 发送POST请求并传递数据
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
response = requests.post(url, json=data)

if response.status_code == 201:
    created_post = response.json()
    print("Created post:", created_post)
else:
    print("Request failed with status code:", response.status_code)