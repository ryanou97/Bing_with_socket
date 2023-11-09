# -*- coding: utf-8 -*-
"""
@author: smile
"""

import socket

# 創建 socket 對象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 獲取本地主機名
host = socket.gethostname()
port = 12345

# 連線服務，指定主機和端口
client_socket.connect((host, port))

# 接收消息
message = client_socket.recv(1024)
print(message.decode('utf-8'))

# 關閉連線
client_socket.close()
