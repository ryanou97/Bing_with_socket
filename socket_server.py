# -*- coding: utf-8 -*-
"""
@author: smile
"""

import socket

# 創建socket對象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 獲取本地主機名
host = socket.gethostname()
port = 12345

# 绑定端口
server_socket.bind((host, port))

# 設置最大連接數
server_socket.listen(5)

while True:
    # 建立客戶端連線
    client_socket, addr = server_socket.accept()
    print('連線地址：', addr)

    # 發送消息
    message = 'welcome to server！'
    client_socket.send(message.encode('utf-8'))

    # 關閉連線
    client_socket.close()
