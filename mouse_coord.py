import win32api
import win32gui
from win32con import *
import time


def findWindowShopTitans():
    hWnd = win32gui.FindWindow(None, "Shop Titans")
    return hWnd


def callback(handle, param):
    s = win32gui.GetClassName(handle)
    print(f'Handle {handle}, {s}')


def printMouseCoordinate():
    hWnd = findWindowShopTitans()
    while True:
        coordinateCursor = win32api.GetCursorPos()
        print("toScreen", coordinateCursor)
        clientCoordinates = win32gui.ScreenToClient(hWnd, coordinateCursor)
        print("toShopTitans", clientCoordinates)
        time.sleep(1)


if __name__ == '__main__':
    #time.sleep(3)
    #hWnd = findWindowShopTitans()
    printMouseCoordinate()
    #win32gui.EnumChildWindows(hWnd, callback, 0)
