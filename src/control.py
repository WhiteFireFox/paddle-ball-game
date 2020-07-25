import time
import win32gui, win32ui, win32con, win32api
import selenium.webdriver
from selenium.webdriver.remote.command import Command

# 获取窗口截图
def window_capture(image_name):
    hwnd = 0  # 0表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, image_name)

if __name__ == '__main__':

    # 定义参数
    distance = 1      #鼠标移动distance距离，可以调整
    image_name = '0.jpg'
    
    # 启动火狐浏览器
    driver = selenium.webdriver.Firefox()

    while True:
        window_capture(image_name)
        result = model.predict(image_name)

        # 计算球的中心和板子的中心
        center_x1 = result[0]['bbox'][0]+result[0]['bbox'][2]/2
        center_y1 = result[0]['bbox'][1]+result[0]['bbox'][3]/2
        center_x2 = result[1]['bbox'][0]+result[1]['bbox'][2]/2
        center_y2 = result[1]['bbox'][1]+result[1]['bbox'][3]/2

        # 实现控制
        if(center_x1>center_x2):
            driver.execute(Command.MOVE_TO,{'xoffset':distance,'yoffset':0})
        else:
            driver.execute(Command.MOVE_TO,{'xoffset':-distance,'yoffset':0})
