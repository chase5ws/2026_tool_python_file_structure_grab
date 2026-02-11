你需要的完整 `readme.md` 內容已全部整合到單一程式碼區塊中，你可以直接複製整個區塊內容保存為 `readme.md` 文件：

```markdown
# Windows 資料夾文件清單生成器

![version](https://img.shields.io/badge/version-1.0.0-green)
![license](https://img.shields.io/badge/license-MIT-blue)
![python](https://img.shields.io/badge/Python-3.6%2B-orange)
![tkinter](https://img.shields.io/badge/tkinter-built--in-lightgrey)
![platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-brightgreen)

---

## 專案說明

**Windows 資料夾文件清單生成器** 是一款基於 Python tkinter 開發的圖形介面工具，專為快速生成指定資料夾的完整文件清單設計。  
本工具可遞迴掃描目標資料夾（包含所有子資料夾），並生成 UTF-8 編碼的 TXT 格式文件清單，支援視覺化選擇掃描路徑與輸出位置，解決手動整理文件清單耗時且易出錯的問題。

---

## 功能特色

- **直覺式圖形介面**：無需命令列操作，透過按鈕即可完成所有操作，新手友好。
- **智慧路徑處理**：自動清理路徑首尾引號、空格，相容 Windows 複製貼上的各種路徑格式。
- **遞迴掃描**：完整掃描目標資料夾下所有子資料夾與文件，不遺漏任何內容。
- **自定義輸出位置**：可自由選擇生成的 TXT 清單文件保存路徑與文件名。
- **UTF-8 編碼**：生成的文件採用 UTF-8 編碼，徹底解決中文文件名亂碼問題。
- **即時結果反饋**：操作結果同時顯示在介面與彈窗中，包含文件統計數據。
- **跨平台支援**：基於 Python 與 tkinter，可在 Windows/macOS/Linux 上執行。

---

## 安裝指南

### 1. 環境要求
- Python 3.6 或更高版本（建議 3.8+）
- tkinter（Python 內建庫，Windows 預裝，macOS/Linux 需確認安裝）

### 2. 安裝步驟
#### Windows 用戶
1. 下載並安裝 Python：前往 [Python 官方網站](https://www.python.org/downloads/) 下載，安裝時勾選「Add Python to PATH」與「tcl/tk and IDLE」。
2. 驗證安裝：開啟命令提示字元，執行以下指令確認 Python 與 tkinter 可用：
   ```bash
   python --version
   python -m tkinter  # 若彈出 tkinter 測試視窗則表示正常
   ```

#### macOS 用戶
1. 透過 Homebrew 安裝 Python（含 tkinter）：
   ```bash
   brew install python
   ```
2. 驗證安裝：
   ```bash
   python3 --version
   python3 -m tkinter
   ```

#### Linux 用戶（Ubuntu/Debian）
1. 安裝 Python 與 tkinter：
   ```bash
   sudo apt update
   sudo apt install python3 python3-tk
   ```
2. 驗證安裝：
   ```bash
   python3 --version
   python3 -m tkinter
   ```

### 3. 取得程式碼
將程式碼保存為 `folder_list_generator.py`（或任意名稱），可直接複製專案程式碼並貼上保存。

---

## 使用方法

### 1. 啟動程式
#### Windows
- 方法 1：雙擊 `folder_list_generator.py` 檔案直接啟動。
- 方法 2：透過命令提示字元啟動：
  ```bash
  python folder_list_generator.py
  ```

#### macOS/Linux
```bash
python3 folder_list_generator.py
```

### 2. 操作步驟
1. **選擇來源資料夾**：點擊「選擇資料夾」按鈕，選取需要掃描的目標資料夾。
2. **設定輸出文件**：
   - 預設輸出路徑為程式所在目錄的「文件清單.txt」；
   - 點擊「選擇保存位置」可自定義保存路徑與文件名（建議保留 `.txt` 副檔名）。
3. **生成清單**：點擊「開始生成文件清單」按鈕，等待程式掃描並生成文件。
4. **查看結果**：執行結果會顯示在介面的「執行結果」區域，同時彈出提示視窗告知生成狀態。

---

## 輸出文件範例
生成的 TXT 文件內容範例如下：
```
========== 資料夾文件清單 ==========
目標資料夾：C:\Users\user\Desktop\測試資料夾
====================================

【文件列表（含所有子資料夾）】
1. 文檔1.txt
2. 圖片\photo.jpg
3. 子資料夾\報告.pdf

====================================
📊 統計：共掃描到 3 個文件
====================================
```

---

## 檔案結構
```
.
└── folder_list_generator.py  # 主程式檔（唯一執行檔）
    ├── generate_folder_file_list()  # 核心掃描與生成函數
    ├── select_source_folder()       # 選擇來源資料夾函數
    ├── select_output_file()         # 選擇輸出文件函數
    ├── start_generate()             # 執行生成操作函數
    └── GUI 介面初始化與事件綁定
```

---

## 常見問題

### Q1：啟動程式時提示「No module named 'tkinter'」？
- **解決方案**：
  - Windows：重新安裝 Python，確保勾選「tcl/tk and IDLE」選項；
  - macOS：執行 `brew install python-tk`；
  - Linux：執行 `sudo apt install python3-tk`。

### Q2：生成文件失敗，提示「權限不足」？
- **原因**：目標保存路徑（如系統資料夾、程式檔案夾）無寫入權限；
- **解決方案**：選擇桌面、文件夾等普通路徑保存輸出文件。

### Q3：掃描的文件數量與實際不符？
- **原因**：部分隱藏文件/系統文件可能被作業系統保護，無法讀取；
- **解決方案**：以管理員身份執行程式（Windows 右鍵「以管理員身份執行」）。

---

## 注意事項

1. 掃描大量文件（數千/數萬個）時，程式執行時間會相應增加，請耐心等待。
2. 確保目標資料夾路徑不含特殊字元（如全形符號、非 ASCII 字元），避免解析錯誤。
3. 生成的文件清單採用相對路徑顯示，便於閱讀與分享。
4. 若需批量生成多個資料夾的清單，可多次執行程式並更換輸出文件名。

---

## 授權

MIT License

---

> 本專案僅供個人學習與日常辦公使用，如需商業應用請自行評估風險。
```

### 总结
1. 上述程式碼區塊包含了 `readme.md` 的完整內容，無任何缺失或截斷；
2. 直接複製整個區塊內容，保存為名為 `readme.md` 的文件即可直接使用；
3. 內容包含專案說明、功能、安裝、使用、常見問題等所有核心模組，格式與樣式完整。
