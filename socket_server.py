# -*- coding: utf-8 -*-
"""
@author: smile
"""
import socket
import threading

def handle_client(client_socket, client_id):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f'接收来自 client {client_id} 的消息: {message}')

            # 等待下一个客户端发送消息
            next_client_id = 1 if client_id == 0 else 0
            print(f"next_client_id: {next_client_id}")
            next_client = clients[next_client_id]
            next_client.send("可以发送消息了".encode('utf-8'))
            print("44444444444444444444")
            
        except:
            break

# 创建 Socket 对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定 IP 地址和端口号
host = '127.0.0.1'
port = 12345
server_socket.bind((host, port))

# 设置最大连接数
server_socket.listen(2)
print('服务器启动，等待两个客户端连接...')

# 存储客户端套接字的列表
clients = []

# 接受两个客户端连接并创建线程处理
for client_id in range(2):
    client_socket, addr = server_socket.accept()
    clients.append(client_socket)
    print(f'连接来自 {addr} 的客户端{client_id}')

    # 等待第一个客户端发送消息
    if client_id == 0:
        client_socket.send("_可以发送消息了".encode('utf-8'))

    # 创建处理客户端消息的线程
    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_id))
    client_handler.start()
    print("here 00000000000000")

# 等待所有线程结束
for client_handler in threading.enumerate():
    print("here 111111111111111")
    if client_handler != threading.current_thread():
        client_handler.join()

# 关闭所有客户端连接
for client in clients:
    print("here 222222222222222")
    client.close()

# 关闭服务器端
server_socket.close()
