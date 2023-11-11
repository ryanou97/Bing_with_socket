# Bingo 遊戲 with Socket

## 簡介

這是一個使用 Python 和 Socket 實現的簡單 Bingo 遊戲。遊戲包括兩名玩家，兩名玩家連線至 server 便能進行 Bingo 遊戲。

## 檔案

- **socket_server.py**：做為 server，負責管理遊戲邏輯、兩個客戶端之間的出牌溝通。
- **socket_client1.py**：玩家 1 連接到 server 以進行遊戲。
- **socket_client2.py**：玩家 2 連接到 server 以進行遊戲。
- **bingo_with_man.py**：包含生成 Bingo 卡片、顯示卡片、檢查 Bingo 連線和進行遊戲功能的module。
- **bingo_with_bot_local.py**：與電腦對戰，電腦出牌維亂輸，獨立於其他腳本，僅用於初步構想。

## 執行方式

1. **執行伺服器:**
   分別執行socket_server.py、socket_client1.py、socket_client2.py，即server啟動後，client1需先連線，接著client2連線後可開始遊戲。
   ```bash
   python socket_server.py
   ```
   ```bash
   python socket_client1.py
   ```
   ```bash
   python socket_client2.py
   ```

## 遊戲玩法
開始時每位玩家會隨機分配到 5*5 的卡牌，並將牌組傳到server端。
從 client1 開始先選擇號碼，接著換 client2，被選到的號碼會以0表示，每次選號 server 都會同步更新，直到先連成一條線者獲勝。


## 程式說明
- server 可以看到雙方的卡牌變化進程，以防玩家在本地端作弊取勝。
- 由 server 判定是否獲勝。
- 其中用到 pickle 函式庫處理 list 的 socket 傳送
   - 在 client 用以下函式將 list 序列化
   ```python
   serialized_data = pickle.dumps()
   ```
   - 在 server 端收到 msg 後再返序列化
   ```python
   pickle.loads()
   ```
   
## 注意事項
遊戲主要邏輯完成，沒有防呆。

