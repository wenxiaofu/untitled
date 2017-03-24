# server.py
# 从wsgiref模块导入:
# 导入我们自己编写的application函数:
from wsgiref.simple_server import make_server
from hylo import application1

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application1)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()