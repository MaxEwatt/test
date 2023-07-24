import win32api
import win32gui
from win32con import *
import time

#пробел вызывает меню крафта, i вызывает сундук, s - настройки, p - героев, j - задания
STW_MAIN = (800, 480)
STC_KEEPTHINGAFTERCRAFT = (626, 393)


def findWindowShopTitans():
    hWnd = win32gui.FindWindow(None, "Shop Titans")
    return hWnd


def click(hWnd, x, y):
    clientCoordinates = win32gui.ClientToScreen(hWnd, (x, y))
    lParam = win32api.MAKELONG(x, y)
    #win32api.SetCursorPos(clientCoordinates)
    #win32api.mouse_event(MOUSEEVENTF_LEFTDOWN, *clientCoordinates, 0, 0)
    #win32api.mouse_event(MOUSEEVENTF_LEFTUP, *clientCoordinates, 0, 0)
    #return
    #win32gui.SetActiveWindow(hWnd)
    #win32gui.SetForegroundWindow(hWnd)
    #win32gui.ShowWindow(hWnd, SW_SHOWNORMAL)
    win32gui.SetCapture(hWnd)
    #win32gui.PostMessage(hWnd, WM_NCHITTEST, HTCLIENT, lParam)
    #win32api.SetCursorPos(clientCoordinates)
    #win32gui.PostMessage(hWnd, WM_KEYDOWN, 0x20, 0)
    #win32gui.PostMessage(hWnd, WM_ACTIVATEAPP, True, 0)
    #win32gui.PostMessage(hWnd, WM_NCACTIVATE, True, 0)
    #win32gui.PostMessage(hWnd, WM_MOUSEMOVE, 0, lParam)
    #win32gui.PostMessage(hWnd, WM_SETFOCUS, 0, 0)
    #win32gui.SendMessage(hWnd, WM_ACTIVATE, WA_CLICKACTIVE, 0)
    #win32gui.SendMessage(hWnd, BM_CLICK, MK_LBUTTON, lParam)
    #lParam1 = win32api.MAKELONG(HTCLIENT, WM_LBUTTONDOWN)
    #win32gui.SendMessage(hWnd, WM_MOUSEACTIVATE, hWnd, lParam1)
    #win32gui.SendMessage(hWnd, WM_SETCURSOR, hWnd, lParam1)
    win32gui.SendMessage(hWnd, WM_LBUTTONDOWN, MK_LBUTTON, lParam)
    win32gui.SendMessage(hWnd, WM_LBUTTONUP, MK_LBUTTON, lParam)
    #win32gui.DefWindowProc(hWnd, WM_LBUTTONDOWN, 1, lParam)

    time.sleep(0.1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #time.sleep(3)
    hWnd = findWindowShopTitans()
    print(hex(hWnd))
    click(hWnd, *STC_KEEPTHINGAFTERCRAFT)
    #click(945, 654)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
