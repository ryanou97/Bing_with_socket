# -*- coding: utf-8 -*-
"""
@author: ryanou97
"""
import socket
import threading
import pickle
import bingo_with_man

def send_message(client_socket, client_id):
    
    print("\nmy card：")
    bingo_with_man.print_bingo_card(player2_card)
    
    times = 1
    
    while True:    
        
        try:
            # 第一次傳送自己卡牌
            if times == 1:
                times = times + 1
                serialized_data = pickle.dumps(player2_card)
                client_socket.send(serialized_data)
           
            print("\nwaiting for player1...")
            
            # waiting the msg from server
            server_message = client_socket.recv(1024).decode('utf-8')
            
            if server_message == 'player 1 win':
                print("I lose the bingo")
                break
            elif server_message == 'player 2 win':
                print("I am winner")
                break
            else:
                print(f"Player1's card number: {server_message}")
            
            bingo_with_man.check_choose_v2(player2_card, int(server_message))
            
            print("\nmy card：")
            bingo_with_man.print_bingo_card(player2_card)
            
            
            # 我出牌
            player2_called_number = input('\nmy call number: ')
            client_socket.send(player2_called_number.encode('utf-8'))
            
            bingo_with_man.check_choose_v2(player2_card, int(player2_called_number))
            
            print("\nmy card：")
            bingo_with_man.print_bingo_card(player2_card)


        except ZeroDivisionError as e:  # 在这里处理 ZeroDivisionError 异常
            print(f"Caught an exception: {e}")
            
        except Exception as e:          # 在这里处理其他异常
            print(f"Caught a generic exception: {e}")
            
            

# 创建 Socket 对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
host = '127.0.0.1'
port = 12345
client_socket.connect((host, port))


# 遊戲初始
player2_card = bingo_with_man.generate_bingo_card()
print("Game Start！")



# 创建发送消息的线程
send_thread = threading.Thread(target=send_message, args=(client_socket, 0))
send_thread.start()

# 等待发送消息的线程结束
send_thread.join()

# 关闭客户端连接
client_socket.close()

