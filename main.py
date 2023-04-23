import tkinter as tk
import menubar
import button

# 创建主窗口
root = tk.Tk()
root.title("LLAS")
root.geometry("600x400")
root.resizable(True, True)

# 创建菜单条对象
menubar = menubar.create_menubar(root)

# 将菜单条设置为主界面的菜单条
root.config(menu=menubar)

# 创建单词背诵按钮
button.create_word_button(root)

# 创建对话模拟按钮
button.create_convo_button(root)

# 进入消息循环
root.mainloop()
