import tkinter as tk
from tkinter import simpledialog
from datetime import datetime
from datetime import timedelta
import io
import ctypes
import os
import imutils
import pyautogui

format_time = "%H:%M"

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

with io.open(filename, 'r', encoding='utf-8', newline='\n') as f:
    for line in f.readlines():
        line = line.strip('\n') # xóa ký tự xuống dòng
        line = line.strip('\r')
        print(line)
        i+=1
        if i == 1:
            from_time_1 = line[line.find('F')+1:line.find('T')-1]
            to_time_1 = line[line.find('T')+1:len(line)+1]
        elif i == 2:
            from_time_2 = line[line.find('F')+1:line.find('T')-1]
            to_time_2 = line[line.find('T')+1:line.find('D')-1]
            once_time_2 = line[line.find('D')+1:line.find('I')-1]
            break_time_2 = line[line.find('I')+1:line.find('S')-1]
            max_time_2 = line[line.find('S')+1:len(line)+1]
        elif i == 3:
            from_time_3 = line[line.find('F')+1:line.find('T')-1]
            to_time_3 = line[line.find('T')+1:line.find('S')-1]
            max_time_3 = line[line.find('S')+1:len(line)+1]

on_off = ''
with io.open('parent.txt', 'r', encoding='utf-8', newline='\n') as f:
    for line in f.readlines():
        line = line.strip('\n') # xóa ký tự xuống dòng
        line = line.strip('\r')
        print(line)
        on_off = line
if on_off == '1':
    change_text = simpledialog.askstring(title="Parent", prompt="Bạn muốn thay đổi nội dung file text \n 1~yes, 0~no \n Lưu ý: trẻ đang dùng máy")
elif on_off == '0':
    change_text = simpledialog.askstring(title="Parent", prompt="Bạn muốn thay đổi nội dung file text \n 1~yes, 0~no \n Lưu ý: trẻ đang không dùng máy")
else:
    ctypes.windll.user32.MessageBoxW(0, "Xảy ra lỗi", "Warning!", 36)

if change_text == '1':
    change_line = simpledialog.askstring(title="Parent", prompt="Bạn muốn thay đổi nội dung dòng nào \n 1~dòng 1, 2~dòng 2, 3~dòng 3")
    if change_line == '1':
        from_time_1 = simpledialog.askstring(title="Parent", prompt="Giờ bắt đầu \n ex: 8h30 thì nhập 08:30")
        to_time_1 = simpledialog.askstring(title="Parent", prompt="Giờ kết thúc \n !!! Giờ kết thúc phải lớn hơn giờ bắt đầu")
    elif change_line == '2':
        from_time_2 = simpledialog.askstring(title="Parent", prompt="Giờ bắt đầu \n ex: 8h30 thì nhập 08:30")
        to_time_2 = simpledialog.askstring(title="Parent", prompt="Giờ kết thúc \n !!! Giờ kết thúc phải lớn hơn giờ bắt đầu")
        once_time_2 = simpledialog.askstring(title="Parent", prompt="Thời gian tối đa mỗi lượt \n !!! Tính theo phút")
        break_time_2 = simpledialog.askstring(title="Parent", prompt="Thời gian nghỉ \n !!! Tính theo phút")
        max_time_2 = simpledialog.askstring(title="Parent", prompt="Thời gian tối đa cho khung giờ này \n !!! Tính theo phút")
    elif change_line == '3':
        from_time_3 = simpledialog.askstring(title="Parent", prompt="Giờ bắt đầu \n ex: 8h30 thì nhập 08:30")
        to_time_3 = simpledialog.askstring(title="Parent", prompt="Giờ kết thúc \n !!! Giờ kết thúc phải lớn hơn giờ bắt đầu")
        max_time_3 = simpledialog.askstring(title="Parent", prompt="Thời gian tối đa cho khung giờ này \n !!! Tính theo phút")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Wrong", "Warning!", 36)
elif change_text == '0':
    ctypes.windll.user32.MessageBoxW(0, "Bye", "Warning!", 36)
else:
    ctypes.windll.user32.MessageBoxW(0, "Wrong", "Warning!", 36)

filename = 'time.txt'
with io.open(filename, 'w', encoding='utf-8', newline='\n') as f:
    f.write("F" + from_time_1 + " T" + to_time_1 + "\n")
    f.write("F" + from_time_2 + " T" + to_time_2 + " D" + once_time_2 + " I" + break_time_2 + " S" + max_time_3 + "\n")
    f.write("F" + from_time_3 + " T" + to_time_3 + " S" + max_time_3 + "\n")

