# -*- coding: utf-8 -*-
"""
@author: smile
"""
import socket
import threading
import pickle
import bingo_with_man
import numpy as np

def handle_client(client_socket, client_id):
    
    # 2*5*5 Arry to store the card numbers from two players
    global player1_card, player2_card
    
    num = 1
    while True:
            
        try:
            
            if num == 1:
                print("num == 1")
                num = num + 1
                received_data = client_socket.recv(1024)
                a = pickle.loads(received_data)
                
                if client_id == 0:
                    player1_card = pickle.loads(received_data)
                    print(f"player {client_id+1}\'s card: ")
                    bingo_with_man.print_bingo_card(player1_card)
                elif client_id == 1:
                    player2_card = pickle.loads(received_data)
                    print(f"player {client_id+1}\'s card: ")
                    bingo_with_man.print_bingo_card(player2_card)
            
            
            print(f"\nwaiting msg from palyer{client_id+1}")
            message = client_socket.recv(1024).decode('utf-8')
            print(f"msg from client: {message}")
            
            if not message:
                break
            
            num = num+1
            print(f"client_id: {client_id}")
            print(f"times: {num}")
            print(f'card number from player{client_id+1} : {message}')
            
            
            ### 更新雙方牌組、確認是否贏了
            print(f"player1\'s card:")
                
            bingo_with_man.check_choose_v2(player1_card, int(message))
            bingo_with_man.print_bingo_card(player1_card)
            if bingo_with_man.check_bingo(player1_card):
                clients[0].send("player 1 win".encode('utf-8'))
                clients[1].send("player 1 win".encode('utf-8'))
                print(f"congratulations, player{client_id+1} win!")
                break
            
            print("-------------------------------------------------------")
            
            print(f"player2\'s card:")
            bingo_with_man.check_choose_v2(player2_card, int(message))
            bingo_with_man.print_bingo_card(player2_card)
            if bingo_with_man.check_bingo(player2_card):
                clients[0].send("player 2 win".encode('utf-8'))
                clients[1].send("player 2 win".encode('utf-8'))
                print(f"\ncongratulations, player{client_id+1} win!")  
                break
            
            
            # 等待下一个客户端发送消息
            next_client_id = 1 if client_id == 0 else 0
            next_client = clients[next_client_id]
            next_client.send(message.encode('utf-8'))
            
            
        except ZeroDivisionError as e:  # 在这里处理 ZeroDivisionError 异常
            print(f"Caught an exception: {e}")
            
        except Exception as e:          # 在这里处理其他异常
            print(f"Caught a generic exception: {e}")


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
    print(f'from {addr} clien{client_id}')

    # 等待第一个客户端发送消息
    if client_id == 0:
        client_socket.send("123456".encode('utf-8'))

    # 创建处理客户端消息的线程
    client_handler_thread = threading.Thread(target=handle_client, args=(client_socket, client_id))
    client_handler_thread.start()
    
    print(f"client_handler_thread: {client_handler_thread}")
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
