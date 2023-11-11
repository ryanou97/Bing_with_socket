# -*- coding: utf-8 -*-
"""
@author: ryanou97
"""

import random


# 生成Bingo卡片
def generate_bingo_card():
    
    numbers = list(range(1, 26))        # 生成1到25的数字列表
     
    random.shuffle(numbers)             # 随机排列列表
    
    card_number = [numbers[i:i+5] for i in range(0, len(numbers), 5)]  # 5個5個一組

    return card_number



# 顯示Bingo卡片
def print_bingo_card(card):
    
    for row in card:
        
        print(" | ".join(f"{number:2d}" for number in row))
        print("-" * 25)

 

# 檢查獲勝
def check_bingo(card):
    
    for row in card:
        if all(cell == 0 for cell in row):
            
            return True
        
    for col in range(5):
        if all(card[row][col] == 0 for row in range(5)):
            
            return True
        
        
    if all(card[i][i] == 0 for i in range(5)) or all(card[i][4 - i] == 0 for i in range(5)):
        
        return True
    
    return False



# 選出的牌換圈
def check_choose(player1_card, player2_card, choose_num):
    
    for row in player1_card:
        if choose_num in row:
            index = row.index(choose_num)
            row[index] = 0
    
    for row in player2_card:
        if choose_num in row:
            index = row.index(choose_num)
            row[index] = 0

    
def check_choose_v2(player_card, choose_num):
    
    for row in player_card:
        if choose_num in row:
            index = row.index(choose_num)
            row[index] = 0
    


# 主循環
def play_bingo():
    
    # 能出的牌 
    can_play_card = list(range(1, 26))
   
    # 亂數產生雙方的牌
    player1_card = generate_bingo_card()
    player2_card = generate_bingo_card()
    
    print("歡迎B來玩ingo遊戲！")
    print("Player 1 卡片：")
    print_bingo_card(player1_card)
    print("\nPlayer 2 卡片：")
    print_bingo_card(player2_card)
    
    while True:
        
        # player 1 出牌
        print("\n------------------------------\n")
        player1_called_number = int(input("Player call number 1: "))
        can_play_card.remove(player1_called_number)
        
        
        check_choose(player1_card, player2_card, player1_called_number)
                
        print("player1 的Bingo卡片：")
        print_bingo_card(player1_card)
        print("\nplayer2 的Bingo卡片：")
        print_bingo_card(player2_card)
        
        if check_bingo(player1_card):
            print("恭喜！您獲得了Bingo！")
            break
        
        if check_bingo(player2_card):
            print("電腦獲勝！")
            break
        
    
        # player 2 出牌
        print("\n------------------------------\n")
        player2_called_number = int(input("Player call number 2: "))
        can_play_card.remove(player2_called_number)
        
        
        check_choose(player1_card, player2_card, player2_called_number)
        
        print("player2 的Bingo卡片：")
        print_bingo_card(player2_card)
        print("\nplayer1 的Bingo卡片：")
        print_bingo_card(player1_card)
        
        if check_bingo(player1_card):
            print("恭喜！您獲得了Bingo！")
            break
        
        if check_bingo(player2_card):
            print("電腦獲勝！")
            break


if __name__ == "__main__":
    play_bingo()
    #card = generate_bingo_card()



