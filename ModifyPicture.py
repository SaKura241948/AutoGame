import cv2

''' WINDOW_NORMAL:手动设置窗口大小
    WINDOW_AUTOSIZE：自动设置窗口大小'''
# 读取图片
def PhotoUrl(url: str):
    # 加载图源
    SetImg = cv2.imread(url)
    # 展示图源
    cv2.imshow("photo", SetImg)
    return SetImg
# 图像转为灰色
def RePhotoGray(url: str):
    # 常用的图像颜色转换
    # 颜色空间转换API
    cvt_img = cv2.cvtColor(url, cv2.COLOR_BGR2GRAY)
    # 窗口等待
    return cvt_img
# 开运算
def RePhotoMorphOpen(url: str, kernel: list):
    updateImg = cv2.morphologyEx(url, cv2.MORPH_OPEN, kernel)
    return updateImg

# 闭运算
def RePhotoMorphClose(url: str, kernel: list):
    updateImg = cv2.morphologyEx(url, cv2.MORPH_CLOSE, kernel)
    return updateImg

# 形态学梯度
def RePhotoMorphGradient(url: str, kernel: list):
    updateImg = cv2.morphologyEx(url, cv2.MORPH_GRADIENT, kernel)
    return updateImg

# 顶帽运算
def RePhotoMorphTophat(url: str, kernel: list):
    updateImg = cv2.morphologyEx(url, cv2.MORPH_TOPHAT, kernel)
    return updateImg

# 黑帽运算
def RePhotoMorphBlackhat(url: str, kernel: list):
    updateImg = cv2.morphologyEx(url, cv2.MORPH_BLACKHAT, kernel)
    return updateImg