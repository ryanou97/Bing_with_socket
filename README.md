# Bingo 遊戲 withsocket

## 簡介

這是一個使用 Python 和 Socket 實現的簡單 Bingo 遊戲。遊戲包括兩名玩家，兩名玩家連線至 server 便能進行 Bingo 遊戲。

## 檔案

- **socket_server.py**：做為server，負責管理遊戲邏輯、兩個客戶端之間的出牌溝通。
- **socket_client1.py**：玩家 1 的客戶端腳本，負責連接到伺服器並進行遊戲。
- **socket_client2.py**：玩家 2 的客戶端腳本，與 client1.py 類似，連接到伺服器參與遊戲。
- **bingo_with_man.py**：包含生成 Bingo 卡片、顯示卡片、檢查 Bingo 和進行遊戲的功能的模塊。

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
開始時每位玩家會隨機分配到5*5的卡牌，並傳到server端。
從client1開始先選擇號碼，接著換client2，被選到的號碼會以0表示，每次選號server也都會同步更新，直到先連成一條線者獲勝。


## 程式說明
- serve可以看到雙方的卡牌變化進程，以防玩家在本地端作弊取勝。
- 由server判定是否獲勝。
- 其中用到 pickle 函式庫處理list的socket傳送
   - 在client用以下函式將list序列化
   ```python
   serialized_data = pickle.dumps()
   ```
   - 在server端收到msg後再返序列化
   ```python
   pickle.loads()
   ```
   
## 注意事項
遊戲使用客戶端-伺服器架構，並使用 Socket 處理客戶端和伺服器之間的通信。
Bingo 卡片的生成、顯示和遊戲邏輯實現在 module.py 文件中。
歡迎探索並根據需要修改代碼。享受遊戲！

遊戲主要邏輯完成，沒有防呆。

