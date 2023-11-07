# -*- coding: utf-8 -*-
"""
@author: ryanou97
"""

import random



# 生成Bingo游戏卡片
def generate_bingo_card():
    card = []
    used_numbers = set()
    for _ in range(5):
        row = []
        while len(row) < 5:
            number = random.randint(1, 25)
            if number not in used_numbers:
                row.append(number)
                used_numbers.add(number)
        row.sort()
        card.append(row)
    return card



# 打印Bingo卡片
def print_bingo_card(card):
    print(" B   I   N   G   O")
    for row in card:
        print(" | ".join(f"{number:2d}" for number in row))
        print("-" * 25)



# 检查Bingo卡片是否获胜
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



# 主游戏循环
def play_bingo():
    computer_card = generate_bingo_card()
    player_card = generate_bingo_card()
    
    print("欢迎来玩Bingo游戏！")
    print("您的Bingo卡片：")
    print_bingo_card(player_card)
    
    while True:
        called_number = random.randint(1, 75)
        print(f"叫号：{called_number}")
        
        for row in player_card:
            if called_number in row:
                index = row.index(called_number)
                row[index] = 0
        
        print("您的Bingo卡片：")
        print_bingo_card(player_card)
        
        if check_bingo(player_card):
            print("恭喜！您获得了Bingo！")
            break
        
        for row in computer_card:
            if called_number in row:
                index = row.index(called_number)
                row[index] = 0
        
        if check_bingo(computer_card):
            print("计算机获得了Bingo！")
            break


if __name__ == "__main__":
    play_bingo()
    #card = generate_bingo_card()
    



