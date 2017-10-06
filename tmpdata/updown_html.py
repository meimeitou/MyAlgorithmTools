import urllib.request
__author__ = 'yinqiwei'


req = urllib.request.Request("http://www.baidu.com")
html = urllib.request.urlopen(req)

cont = html.readline()

print(cont)
print(html.info())
print(html.getcode())
print(html.geturl())
