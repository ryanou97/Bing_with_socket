# -*- coding: utf-8 -*-
"""
@author: smile
"""
import socket
import threading

def send_message(client_socket, client_id):
    while True:
        try:
            message = input('输入消息: ')
            client_socket.send(message.encode('utf-8'))

            # 等待服务器端的指示，表示可以发送消息了
            server_message = client_socket.recv(1024).decode('utf-8')
            print(server_message)

        except:
            break

# 创建 Socket 对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
host = '127.0.0.1'
port = 12345
client_socket.connect((host, port))

# 创建发送消息的线程
send_thread = threading.Thread(target=send_message, args=(client_socket, 0))
send_thread.start()

# 等待发送消息的线程结束
send_thread.join()

# 关闭客户端连接
client_socket.close()

