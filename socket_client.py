# -*- coding: utf-8 -*-
"""
@author: smile
"""

import socket

# 创建 socket 对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
port = 12345

# 连接服务，指定主机和端口
client_socket.connect((host, port))

# 接收欢迎消息
message = client_socket.recv(1024)
print(message.decode('utf-8'))

# 关闭连接
client_socket.close()
