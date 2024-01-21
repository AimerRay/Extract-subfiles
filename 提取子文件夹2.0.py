#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import shutil
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import threading

def extract_files_from_folders(folder_path, destination_path, text_output_widget):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            destination_file_path = os.path.join(destination_path, file)
            
            # 获取源文件的文件名和扩展名
            file_name, file_extension = os.path.splitext(file)
            
            # 构建目标文件路径
            count = 1
            new_file_path = os.path.join(destination_path, f"{file_name}_{count}{file_extension}")
            
            # 检查目标文件是否存在，如果存在，则在文件名后加上计数器
            while os.path.exists(new_file_path):
                count += 1
                new_file_path = os.path.join(destination_path, f"{file_name}_{count}{file_extension}")
            
            # 复制文件到目标路径
            shutil.copy(file_path, new_file_path)
            
            # 在提取的同时更新GUI文本框
            text_output_widget.insert(tk.END, f"提取文件: {os.path.basename(new_file_path)}\n")
            text_output_widget.update()  # 强制更新GUI，确保文本框实时显示

    # 文件提取完成后弹出通知框
    messagebox.showinfo("提取完成", "文件提取完成！")

def browse_folder(entry_widget):
    folder_selected = filedialog.askdirectory()
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, folder_selected)

def extract_files_gui():
    folder_path = entry_source.get()
    destination_path = entry_destination.get()
    
    # 清空文本框
    text_output.delete(1.0, tk.END)
    
    # 创建一个线程来执行提取文件的任务
    extract_thread = threading.Thread(target=extract_files_from_folders, args=(folder_path, destination_path, text_output))
    extract_thread.start()

# 创建 GUI 窗口
root = tk.Tk()
root.title("文件提取工具")

# 添加提取目录输入框和浏览按钮
label_source = tk.Label(root, text="选择提取目录:")
label_source.grid(row=0, column=0, pady=10)

entry_source = tk.Entry(root, width=50)
entry_source.grid(row=0, column=1)

button_browse_source = tk.Button(root, text="浏览", command=lambda: browse_folder(entry_source))
button_browse_source.grid(row=0, column=2)

# 添加目标目录输入框和浏览按钮
label_destination = tk.Label(root, text="选择目标目录:")
label_destination.grid(row=1, column=0, pady=10)

entry_destination = tk.Entry(root, width=50)
entry_destination.grid(row=1, column=1)

button_browse_destination = tk.Button(root, text="浏览", command=lambda: browse_folder(entry_destination))
button_browse_destination.grid(row=1, column=2)

# 添加提取按钮
button_extract = tk.Button(root, text="开始提取", command=extract_files_gui)
button_extract.grid(row=2, column=0, columnspan=3, pady=10)

# 添加用于显示提取过程的文本框
text_output = scrolledtext.ScrolledText(root, width=60, height=15)
text_output.grid(row=3, column=0, columnspan=3, pady=10)

# 运行 GUI
root.mainloop()


# In[ ]:




