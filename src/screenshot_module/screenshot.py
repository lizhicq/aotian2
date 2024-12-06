import win32gui
import win32ui
import win32con
import win32api
from PIL import Image

def capture_specific_window(window_title):
    """精确截取指定窗口的内容"""
    # 找到窗口
    hwnd = win32gui.FindWindow(None, window_title)
    
    # 获取窗口客户区大小（不包括标题栏和边框）
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    
    # 转换客户区坐标到屏幕坐标
    point = win32gui.ClientToScreen(hwnd, (left, top))
    left, top = point
    
    # 获取窗口实际大小
    width = right - left
    height = bot - top
    
    # 创建设备上下文
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    
    # 创建位图
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    saveDC.SelectObject(saveBitMap)
    
    # 截取客户区
    saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)
    
    # 转换图像
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    im = Image.frombuffer(
        'RGB', 
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']), 
        bmpstr, 
        'raw', 
        'BGRX', 
        0, 
        1
    )
    
    # 保存图像
    im.save('window_screenshot.png')
    
    # 释放资源
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

# 使用示例
if __name__ == "__main__":
    capture_specific_window('短线精灵')