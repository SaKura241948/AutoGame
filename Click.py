import random
import time
from ctypes import windll

import pythoncom
import win32api
import win32com.client
import win32con
import win32gui

import BitBltPrintWindow


# 鼠标的点击
def clickLeftCur():
    win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# 返回鼠标坐标
def getCurPos():
    return win32gui.GetCursorPos()


# 鼠标移动
def moveCurPos(x, y):
    # 获取要截取窗口的句柄
    if BitBltPrintWindow.hwnd <= 0:
        BitBltPrintWindow.hwnd
    if BitBltPrintWindow.hwnd > 0:
        pythoncom.CoInitialize()
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        # 设置为最前端窗口
        win32gui.SetForegroundWindow(BitBltPrintWindow.hwnd)
        stop = random.randint(0, 3)
        time.sleep(stop)
    windll.user32.SetCursorPos(x + BitBltPrintWindow.left, y + BitBltPrintWindow.top)
    clickLeftCur()
