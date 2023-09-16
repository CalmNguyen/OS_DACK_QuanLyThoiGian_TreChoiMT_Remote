import time
import tkinter as tk
from tkinter import simpledialog
from datetime import datetime
from datetime import timedelta
import io
import ctypes
import Parent
import os
import imutils
import pyautogui
import PIL
import cv2

logged_in = 0
def login(logged_in):
    ROOT = tk.Tk()
    ROOT.withdraw()

    # username: join, password: 123456 là phụ huynh
    # username: anna, password: 1234 là trẻ em

    while logged_in == 0:
        login_username = simpledialog.askstring(title="Log in", prompt="What's your name ?")
        if login_username == "join":
            login_password = simpledialog.askstring(title="Log in", prompt="Hi {}, password ?".format(login_username))
            if login_password == "123456":
                logged_in = 1
            else:
                ctypes.windll.user32.MessageBoxW(0, "Incorrect password!", "Warning!", 36)
        elif login_username == "anna":
            login_password = simpledialog.askstring(title="Log in", prompt="Hi {}, password ?".format(login_username))
            if login_password == "1234":
                logged_in = 2
            else:
                ctypes.windll.user32.MessageBoxW(0, "Incorrect password!", "Warning!", 36)
        else:
            ctypes.windll.user32.MessageBoxW(0, "Wrong username", "Warning!", 36)
    return logged_in

def login_parent(on_off):
    filename = 'parent.txt'
    # 1 ~ on
    # 0 ~ off
    with io.open(filename, 'w', encoding='utf-8', newline='\n') as f:
        f.write(on_off)


logged_in = login(logged_in)
login_parent("0")
# logged == 1
# suy ra là cha me dang dùng máy
# vậy cần chờ sau 60 phút mới tắt máy
if logged_in == 1:
    print("p")
    time_i = 1
    while time_i > 0:
        time.sleep(60*60)
        login(0)

# logged == 2
# suy ra là trẻ đang dùng máy
# vậy đọc file
# rồi xử lý theo từng trường hợp
elif logged_in == 2:
    print("c")
    now = datetime.now()
    format_time = "%H:%M"
    current_time = now.strftime(format_time)
    print("time =", current_time)
    from_time_1 = "00:00"
    to_time_1 = "00:00"
    from_time_2 = "00:00"
    to_time_2 = "00:00"
    once_time_2 = 0
    break_time_2 = 0
    max_time_2 = 0
    from_time_3 = "00:00"
    to_time_3 = "00:00"
    max_time_3 = 0

    # load dữ liệu
    filename = "time.txt"

    i = 0

    # lấy thông tin từ file time
    with io.open(filename, 'r', encoding='utf-8', newline='\n') as f:
        for line in f.readlines():
            line = line.strip('\n')  # xóa ký tự xuống dòng
            line = line.strip('\r')
            print(line)
            i += 1
            if i == 1:
                from_time_1 = line[line.find('F') + 1:line.find('T') - 1]
                to_time_1 = line[line.find('T') + 1:len(line) + 1]
            elif i == 2:
                from_time_2 = line[line.find('F') + 1:line.find('T') - 1]
                to_time_2 = line[line.find('T') + 1:line.find('D') - 1]
                once_time_2 = line[line.find('D') + 1:line.find('I') - 1]
                break_time_2 = line[line.find('I') + 1:line.find('S') - 1]
                max_time_2 = line[line.find('S') + 1:len(line) + 1]
            elif i == 3:
                from_time_3 = line[line.find('F') + 1:line.find('T') - 1]
                to_time_3 = line[line.find('T') + 1:line.find('S') - 1]
                max_time_3 = line[line.find('S') + 1:len(line) + 1]

    # thời gian hiện tại thuộc thời gian dòng 1
    if current_time > from_time_1 and current_time < to_time_1:
        print("1")
        login_parent("1")
        time_1 = datetime.strptime(to_time_1, format_time) - datetime.strptime(from_time_1, format_time)
        time_mins = timedelta.total_seconds(time_1)
        time_mins = int(time_mins / 60)
        i = 0
        while time_mins > 1:
            time.sleep(60)
            i = i + 1
            time_mins = time_mins - 1
            pyautogui.screenshot("pic1_{}.png".format(i))
        ctypes.windll.user32.MessageBoxW(0, "Còn 1 phút nữa là tắt máy", "Notification", 36)
        time.sleep(60)
        login_parent("0")
        os.system("shutdown /p")

    # thời gian hiện tại thuộc thời gian dòng 2
    elif current_time > from_time_2 and current_time < to_time_2:
        print("2")
        login_parent("1")
        i = 0
        once_time = int(once_time_2)
        while once_time > 0:
            time.sleep(60)
            i = i + 1
            once_time = once_time - 1
            pyautogui.screenshot("pic2_{}.png".format(i))
            max_time_2 = max_time_2 - 1
            if max_time_2 == 0:
                ctypes.windll.user32.MessageBoxW(0, "Còn 1 phút nữa là tắt máy", "Notification", 36)
                time.sleep(60)
                login_parent("0")
                os.system("shutdown /p")
        ctypes.windll.user32.MessageBoxW(0, "Tạm ngừng {} phút".format(break_time_2), "Notification", 36)
        time.sleep(60)
        login_parent("0")
        break_time = break_time_2
        while break_time > 0:
            ctypes.windll.user32.MessageBoxW(0, "Tạm ngừng {} phút".format(break_time_2), "Notification", 36)
            time.sleep(60)
            break_time = break_time - 1

        # os.system("shutdown /p")

    # thời gian hiện tại thuộc thời gian dòng 3
    elif current_time > from_time_3 and current_time < to_time_3:
        print("3")
        login_parent("1")
        i = 0
        now = datetime.now()

        now_time = now.strftime(format_time)
        while int(max_time_3) > 0 and now_time < to_time_3:
            now = datetime.now()
            now_time = now.strftime(format_time)
            time.sleep(60)
            i = i + 1
            pyautogui.screenshot("pic3_{}.png".format(i))
            max_time_3 = max_time_3 - 1
        ctypes.windll.user32.MessageBoxW(0, "Còn 1 phút nữa là tắt máy".format(break_time_2), "Notification", 36)
        login_parent("0")
        os.system("shutdown /p")

    # không nằm trong thời gian dùng máy tính
    else:
        print("4")
        time_1 = datetime.strptime(to_time_1, format_time) - datetime.strptime(from_time_1, format_time)
        time_next = "00:00"
        time_list = [current_time, from_time_1, from_time_2, from_time_3, to_time_1, to_time_2, to_time_3]
        time_list = sorted(time_list)
        print(time_list)
        for i in range(len(time_list)):
            if current_time == time_list[i]:
                if i + 1 < len(time_list):
                    time_next = time_list[i + 1]
                    ctypes.windll.user32.MessageBoxW(0, "Chờ đến {} mới được dùng máy".format(time_next),
                                                     "Notification", 36)
                    time.sleep(15)
                    os.system("shutdown /p")
                else:
                    time_next = time_list[0]
                    ctypes.windll.user32.MessageBoxW(0, "Chờ đến {} hôm sau mới được dùng máy".format(time_next),
                                                     "Notification", 36)
                    time.sleep(15)
                    os.system("shutdown /p")

else:
    ctypes.windll.user32.MessageBoxW(0, "Xảy ra lỗi", "Warning!", 36)