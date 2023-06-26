import time
import tkinter as tk
from tkinter.font import Font

wait_time = 1800  # 默认等待时间为30分钟（1800秒）

def update_wait_time():
    global wait_time  # 声明全局变量
    new_wait_time = time_entry.get()
    if new_wait_time.isdigit():  # 判断用户输入的是否是数字
        wait_time = int(new_wait_time)
    root.destroy()  # 关闭窗口

def popup_reminder():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 打印当前时间
    try:
        reminder_window = tk.Tk()
        reminder_window.title("喝水提醒")
        reminder_window.geometry("1920x1080") # 调整窗口大小
        reminder_window.attributes("-topmost", True) # 置于最前面
        font = Font(family="微软雅黑", size=24, weight="bold") # 创建自定义字体
        reminder_label = tk.Label(reminder_window, text="该喝水啦！", font=font, fg="DarkBlue", bg="Linen") # 使用自定义字体和背景颜色
        reminder_label.pack(expand=True, fill="both") # 将标签填充整个窗口
        reminder_window.after(5000, reminder_window.destroy)  # 5秒后自动关闭窗口
        reminder_window.mainloop() # 显示窗口
    except Exception as e:
        print("窗口弹出失败:", e)

while True:
    popup_reminder()
    time.sleep(wait_time)  # 等待一段时间后再次弹出提醒窗口


