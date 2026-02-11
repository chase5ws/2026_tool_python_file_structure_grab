import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def generate_folder_file_list(folder_path, output_txt):
    """
    讀取指定資料夾所有內容（含子資料夾），生成utf-8編碼的文件清單TXT
    :param folder_path: 目標資料夾路徑
    :param output_txt: 生成的TXT檔案完整路徑
    """
    # 路徑預處理：移除首尾引號、空格
    folder_path = folder_path.strip().strip('"').strip("'")
    
    # 路徑校驗
    if not os.path.exists(folder_path):
        return False, f"❌ 錯誤：資料夾路徑不存在 -> {folder_path}"
    if not os.path.isdir(folder_path):
        return False, f"❌ 錯誤：該路徑不是資料夾 -> {folder_path}"

    # 初始化清單內容
    file_list_content = [
        "========== 資料夾文件清單 ==========\n",
        f"目標資料夾：{os.path.abspath(folder_path)}\n",
        "====================================\n\n",
        "【文件列表（含所有子資料夾）】\n"
    ]

    # 遞迴遍歷所有文件
    total_file_num = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            total_file_num += 1
            file_abs_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_abs_path, folder_path)
            file_list_content.append(f"{total_file_num}. {relative_path}\n")


    # 寫入TXT檔案
    try:
        with open(output_txt, "w", encoding="utf-8") as f:
            f.writelines(file_list_content)
        return True, f"✅ 生成成功！\n📁 清單檔案：{os.path.abspath(output_txt)}\n📈 共掃描 {total_file_num} 個文件（含子資料夾）"
    except Exception as e:
        return False, f"❌ 生成失敗：{str(e)}（可能是權限不足/文件被占用）"

def select_source_folder():
    """選擇來源資料夾"""
    folder_path = filedialog.askdirectory(title="選擇要掃描的資料夾")
    if folder_path:
        entry_source.delete(0, tk.END)
        entry_source.insert(0, folder_path)

def select_output_file():
    """選擇輸出文件的保存位置和名稱"""
    file_path = filedialog.asksaveasfilename(
        title="選擇生成的清單文件保存位置",
        defaultextension=".txt",
        filetypes=[("文字檔案", "*.txt"), ("所有檔案", "*.*")],
        initialfile="文件清單.txt"  # 預設文件名
    )
    if file_path:
        entry_output.delete(0, tk.END)
        entry_output.insert(0, file_path)

def start_generate():
    """執行生成操作"""
    # 获取输入的路径
    source_folder = entry_source.get().strip()
    output_file = entry_output.get().strip()
    
    # 驗證輸入
    if not source_folder:
        messagebox.showwarning("警告", "請先選擇要掃描的資料夾！")
        return
    if not output_file:
        messagebox.showwarning("警告", "請先選擇生成文件的保存位置！")
        return
    
    # 執行生成
    success, msg = generate_folder_file_list(source_folder, output_file)
    
    # 顯示結果
    text_result.delete(1.0, tk.END)  # 清空結果區
    text_result.insert(tk.END, msg)
    
    # 彈窗提示最終結果
    if success:
        messagebox.showinfo("成功", msg)
    else:
        messagebox.showerror("錯誤", msg)

# 創建主窗口
if __name__ == "__main__":
    # 初始化主窗口
    root = tk.Tk()
    root.title("Windows 資料夾文件清單生成器 By ChaseTseng")
    root.geometry("700x450")  # 視窗大小
    root.resizable(True, True)  # 允許調整大小

    # 設置樣式
    style = ttk.Style(root)
    style.configure("TLabel", font=("微軟正黑體", 10))
    style.configure("TButton", font=("微軟正黑體", 10))
    style.configure("TEntry", font=("微軟正黑體", 10))

    # ========== 來源資料夾區域 ==========
    frame_source = ttk.Frame(root, padding="10")
    frame_source.pack(fill=tk.X, padx=10, pady=5)

    label_source = ttk.Label(frame_source, text="來源資料夾：")
    label_source.pack(side=tk.LEFT, padx=5)

    entry_source = ttk.Entry(frame_source, width=60)
    entry_source.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

    btn_select_source = ttk.Button(frame_source, text="選擇資料夾", command=select_source_folder)
    btn_select_source.pack(side=tk.LEFT, padx=5)

    # ========== 輸出文件區域 ==========
    frame_output = ttk.Frame(root, padding="10")
    frame_output.pack(fill=tk.X, padx=10, pady=5)

    label_output = ttk.Label(frame_output, text="輸出文件：")
    label_output.pack(side=tk.LEFT, padx=5)

    entry_output = ttk.Entry(frame_output, width=60)
    entry_output.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
    # 默認填充輸出路徑（當前目錄的文件清單.txt）
    default_output = os.path.join(os.getcwd(), "文件清單.txt")
    entry_output.insert(0, default_output)

    btn_select_output = ttk.Button(frame_output, text="選擇保存位置", command=select_output_file)
    btn_select_output.pack(side=tk.LEFT, padx=5)

    # ========== 操作按鈕區域 ==========
    frame_btn = ttk.Frame(root, padding="10")
    frame_btn.pack(pady=10)

    btn_generate = ttk.Button(
        frame_btn, 
        text="開始生成文件清單", 
        command=start_generate,
        style="Accent.TButton"
    )
    btn_generate.pack(padx=5, pady=5)

    # ========== 結果顯示區域 ==========
    frame_result = ttk.Frame(root, padding="10")
    frame_result.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)

    label_result = ttk.Label(frame_result, text="執行結果：")
    label_result.pack(anchor=tk.W)

    # 滾動文本框顯示結果
    scrollbar = ttk.Scrollbar(frame_result)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text_result = tk.Text(frame_result, font=("微軟正黑體", 10), yscrollcommand=scrollbar.set, wrap=tk.WORD)
    text_result.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    scrollbar.config(command=text_result.yview)

    # 啟動主循環
    root.mainloop()