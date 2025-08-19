# 🦖 Auto Dino - 遊戲自動化腳本

這是一個使用 Python 製作的遊戲自動化工具，透過圖片辨識與鍵盤模擬操作，能自動進行兩款網頁遊戲。專案結合 `pyautogui`、`pynput`、`imagesearch` 等模組，實現快速反應與視覺控制。

## 📖 專案簡介

非機器學習，純粹透過影像處理方式實現 2D 物件偵測與自動操作。適合用於學習 GUI 自動化、圖片辨識與鍵盤控制技術。

## 🚀 功能特色

- 🎯 自動辨識遊戲畫面中的特定圖片
- ⌨️ 根據圖片位置模擬鍵盤按鍵（左右鍵、空白鍵、上下鍵）
- 🕹️ 支援兩款不同遊戲的自動操作流程
- ⚙️ 可自訂辨識精度與取樣週期

## 🖼️ 使用圖片

- 第一款遊戲：
  - `flag_start.png`：開始旗幟
  - `pancake.png`：左鍵觸發物件
  - `drink.png`：右鍵觸發物件

- 第二款遊戲：
  - `disconnect1.png`：開始畫面
  - `cactus.png`：障礙物（仙人掌）
  - `fly1.png`, `fly2.png`：飛行物
  - `restart.png`：重新開始按鈕

## 🛠️ 安裝方式

```bash
git clone https://github.com/StanLinCat/auto_dino.git
cd auto_dino
pip install -r requirements.txt
```
📌 請確認你已安裝 pyautogui, pynput, imagesearch 等模組
## 🧪 使用方式
- 將所需圖片放入 img/ 資料夾。
- 根據螢幕解析度調整圖片辨識範圍與座標。
- 執行 main.py，程式將自動開始遊戲並進行操作。
```bash
python main.py
```
## 🎬 使用示範影片

點擊下方圖片觀看 Auto Dino 的實際運作效果：

[![Auto Dino Demo](https://img.youtube.com/vi/Tgs7ZFv4YLU/0.jpg)](https://youtu.be/Tgs7ZFv4YLU?si=LkscFoRJHDlOysJN)
