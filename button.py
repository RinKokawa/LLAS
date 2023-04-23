import tkinter as tk
import style

def show_word_window(root):
    # 隐藏主窗口
    root.withdraw()

    # 创建新的窗口
    word_window = tk.Toplevel(root)
    word_window.title("单词背诵窗口")
    word_window.geometry("400x300")

    # 更新窗口属性
    word_window.update_idletasks()

    # 计算要设置为窗口左上角的坐标
    width = word_window.winfo_width()
    height = word_window.winfo_height()
    x = (word_window.winfo_screenwidth() - width) // 2
    y = (word_window.winfo_screenheight() - height) // 2

    # 设置窗口位置和大小
    word_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # 在新窗口中添加组件
    label = tk.Label(word_window, text="这是单词背诵窗口")
    label.pack()

    # 关闭新窗口时显示主窗口
    def on_close():
        word_window.destroy()
        root.deiconify()

    word_window.protocol("WM_DELETE_WINDOW", on_close)

def create_word_button(root):
    word_button = tk.Button(root, text="单词背诵", **style.button_style, command=lambda: show_word_window(root))
    word_button.pack()

def show_convo_window(root):
    # 隐藏主窗口
    root.withdraw()

    # 创建新的窗口
    convo_window = tk.Toplevel(root)
    convo_window.title("对话模拟窗口")
    convo_window.geometry("400x300")

    # 更新窗口属性
    convo_window.update_idletasks()

    # 计算要设置为窗口左上角的坐标
    width = convo_window.winfo_width()
    height = convo_window.winfo_height()
    x = (convo_window.winfo_screenwidth() - width) // 2
    y = (convo_window.winfo_screenheight() - height) // 2

    # 设置窗口位置和大小
    convo_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # 在新窗口中添加组件
    label = tk.Label(convo_window, text="这是对话模拟窗口")
    label.pack()

    # 关闭新窗口时显示主窗口
    def on_close():
        convo_window.destroy()
        root.deiconify()

    convo_window.protocol("WM_DELETE_WINDOW", on_close)

def create_convo_button(root):
    convo_button = tk.Button(root, text="对话模拟", **style.button_style, command=lambda: show_convo_window(root))
    convo_button.pack()