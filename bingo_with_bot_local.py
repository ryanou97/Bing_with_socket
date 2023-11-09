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
    print(" B   I   N   G   O")
    
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


# 檢查這張牌能不能出
# def play_card()


# 主循環
def play_bingo():
    
    # 能出的牌 
    can_play_card = list(range(1, 26))
   
    # 亂數產生雙方的牌
    player_card = generate_bingo_card()
    computer_card = generate_bingo_card()
    
    print("歡迎B來玩ingo遊戲！")
    print("您的Bingo卡片：")
    print_bingo_card(player_card)

    
    while True:
        
        
        # 玩家出牌
        player_called_number = int(input("Player call number: "))
        can_play_card.remove(player_called_number)
        
        for row in player_card:
            if player_called_number in row:
                index = row.index(player_called_number)
                row[index] = 0
            
        print("您的Bingo卡片：")
        print_bingo_card(player_card)
        
        
        if check_bingo(player_card):
            print("恭喜！您獲得了Bingo！")
            break
        
        for row in computer_card:
            if player_called_number in row:
                index = row.index(player_called_number)
                row[index] = 0
        
        if check_bingo(computer_card):
            print("電腦獲勝！")
            break
        
    
        
        # 電腦出牌
        bot_called_number = random.choice(can_play_card)
        can_play_card.remove(bot_called_number)
        print(f"Bot call number: {bot_called_number}")
        
        
        for row in player_card:
            if bot_called_number in row:
                index = row.index(bot_called_number)
                row[index] = 0
        
        print("您的Bingo卡片：")
        print_bingo_card(player_card)
        
        
        if check_bingo(player_card):
            print("恭喜！您獲得了Bingo！")
            break
        
        for row in computer_card:
            if bot_called_number in row:
                index = row.index(bot_called_number)
                row[index] = 0
        
        if check_bingo(computer_card):
            print("電腦獲勝！")
            break


if __name__ == "__main__":
    play_bingo()
    #card = generate_bingo_card()



