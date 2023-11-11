# -*- coding: utf-8 -*-
"""
@author: smile
"""
import socket
import threading
import pickle
import bingo_with_man

def handle_client(client_socket, client_id):
    
    global palyer_card
    
    num = 1
    while True:
            
        try:
            
            if num == 1:
                print("num == 1")
                num = num + 1
                received_data = client_socket.recv(1024)
                print(f"received_data: {received_data}")
                palyer_card = pickle.loads(received_data)
                print(f"palyer {client_id+1}\'s card:")
                bingo_with_man.print_bingo_card(palyer_card)
                
            
            print("waiting msg from client")
            message = client_socket.recv(1024).decode('utf-8')
            print(f"msg from client: {message}")
            
            if not message:
                break
            
            num = num+1
            print(f"\nclient_socket: {client_socket}")
            print(f"client_id: {client_id}")
            print(f"times: {num}")
            print(f'card number from client{client_id} : {message}')
            
            
            ### 更新牌組、確認是否贏了
            print(f"palyer {client_id+1}\'s card:")
            bingo_with_man.check_choose_v2(palyer_card, int(message))
            bingo_with_man.print_bingo_card(palyer_card)
            
            if bingo_with_man.check_bingo(player1_card):
                print(f"congratulations, palyer{client_id+1} win!")
            
            
            # 等待下一个客户端发送消息
            next_client_id = 1 if client_id == 0 else 0
            print(f"next_client_id: {next_client_id}")
            next_client = clients[next_client_id]
            next_client.send(message.encode('utf-8'))
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
print('waiting for two players online...')



# 存储客户端套接字的列表
clients = []

# 接受两个客户端连接并创建线程处理
for client_id in range(2):
    client_socket, addr = server_socket.accept()
    clients.append(client_socket)
    print(f'连接来自 {addr} 的客户端{client_id}')

    # 等待第一个客户端发送消息
    if client_id == 0:
        client_socket.send("123456".encode('utf-8'))

    # 创建处理客户端消息的线程
    client_handler_thread = threading.Thread(target=handle_client, args=(client_socket, client_id))
    client_handler_thread.start()
    
    print(f"client_handler_thread: {client_handler_thread}")
    print(f"client_id: {client_id}")
    print("here 00000000000000\n")



# 等待所有线程结束
for client_handler_thread in threading.enumerate():
    print("here 111111111111111")
    
    if client_handler_thread != threading.current_thread():
        
        print("here 222222222222222")
        print(f"client_handler_thread: {client_handler_thread}")
        print(f"threading.current_thread(): {threading.current_thread()}\n")
        client_handler_thread.join()



# 关闭所有客户端连接
for client in clients:
    print("here 333333333333333333")
    client.close()

# 关闭服务器端
server_socket.close()
