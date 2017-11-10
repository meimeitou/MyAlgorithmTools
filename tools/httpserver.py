'''
#简单http 服务器 可通过浏览器实现多平台文件传输需求
使用：
在命令窗口直接运行 pyhton httpserver.py
默认端口8080
'''
import sys
try:
    # for python3
    from http.server import HTTPServer, CGIHTTPRequestHandler
except ImportError:
    # for python2
    from BaseHTTPServer import HTTPServer
    from CGIHTTPServer import CGIHTTPRequestHandler

n=len(sys.argv)
port = 8080

httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()
