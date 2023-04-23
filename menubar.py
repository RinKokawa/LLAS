import tkinter as tk

def create_menubar(root):
    # 创建菜单条对象
    menubar = tk.Menu(root)
    # 创建菜单对象
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="New")
    file_menu.add_command(label="Open")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    # 将菜单添加到菜单条上
    menubar.add_cascade(label="File", menu=file_menu)
    # ---------------------------创建帮助菜单----------------------------- #
    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="User Manual")
    help_menu.add_separator()
    help_menu.add_command(label="Support The Author")
    menubar.add_cascade(label="Help", menu=help_menu)

    # 返回菜单条对象
    return menubar
