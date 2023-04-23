import tkinter as tk

# 自定义按钮样式
button_style = {
    "font": ("Arial", 16),
    "bg": "#101010",  # 修改为深灰色背景
    "fg": "#00FFAA",  # 修改为亮绿色前景
    "relief": tk.FLAT,  # 修改为扁平样式边框
    "borderwidth": 0,  # 取消边框宽度
    "highlightthickness": 0,  # 取消高亮边框
    "activebackground": "#00FFAA",  # 设置点击后的背景颜色为亮绿色
    "cursor": "hand2",  # 鼠标悬停时显示手型光标
}


# 定义布局参数
layout_params = {
    "side": tk.TOP,
    "fill": tk.BOTH,
    "expand": True,
}
