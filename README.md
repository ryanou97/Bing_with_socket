# Bingo 遊戲 withsocket

## 簡介

這是一個使用 Python 和 Socket 實現的簡單 Bingo 遊戲。遊戲包括兩名玩家，兩名玩家連線至 server 便能進行 Bingo 遊戲。

## 檔案

- **server.py**：伺服器腳本，負責管理遊戲邏輯和兩個客戶端之間的通信。
- **client1.py**：玩家 1 的客戶端腳本，負責連接到伺服器並進行遊戲。
- **client2.py**：玩家 2 的客戶端腳本，與 client1.py 類似，連接到伺服器參與遊戲。
- **module.py**：包含生成 Bingo 卡片、顯示卡片、檢查 Bingo 和進行遊戲的功能的模塊。

## 如何執行

1. **執行伺服器:**
   ```bash 1.
   python socket_server.py
   ```
   ```bash 2.
   python socket_client1.py
   ```
   ```bash 3.
   python socket_client2.py
   ```

## 使用方式
1. socket_server.py 需要先執行
2. socket_client1.py 執行
3. socket_client2.py 執行

## 遊戲玩法
每位玩家都獲得一張 Bingo 卡片。
玩家輪流宣讀一個數字，相應的卡片格將被標記。
第一位完成一行、一列或對角線的玩家大喊「Bingo」，贏得遊戲。


## 注意事項
遊戲使用客戶端-伺服器架構，並使用 Socket 處理客戶端和伺服器之間的通信。
Bingo 卡片的生成、顯示和遊戲邏輯實現在 module.py 文件中。
歡迎探索並根據需要修改代碼。享受遊戲！


