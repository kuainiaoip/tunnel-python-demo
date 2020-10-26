# -*- coding: utf-8 -*-
import requests

# 要访问的目标网页
page_urls = ["http://api.kuainiaoip.com/test",
             "https://httpbin.org/get",
             ]

# 隧道服务器
tunnel_host = "tunnel.kuainiaoip.com"
tunnel_port = "28999"

# 隧道用户名密码
tid = ""
password = ""

proxies = {
    "http": "http://%s:%s@%s:%s/" % (tid, password, tunnel_host, tunnel_port),
    "https": "https://%s:%s@%s:%s/" % (tid, password, tunnel_host, tunnel_port)
}
headers = {
    "Accept-Encoding": "Gzip",  # 使用gzip压缩传输数据让访问更快
}

for url in page_urls:
    r = requests.get(url, proxies=proxies, headers=headers)
    # 发送post请求
    # r = requests.post("http://api.kuainiaoip.com/test", proxies=proxies, data={"info": "send post request"})

    print(r.status_code)  # 获取Reponse的返回码

    if r.status_code == 200:
        r.enconding = "utf-8"  # 设置返回内容的编码
        print(r.content)  # 获取页面内容
