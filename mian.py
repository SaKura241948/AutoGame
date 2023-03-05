'''设计原理
main。py调用其他功能
获取图片或视频通过main
'''
import cv2

import ModifyPicture

# 卷积核数量
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# 加载图源
ImgUrl = 'photo/YHDOOR.png'
ImgRead = ModifyPicture.PhotoUrl(ImgUrl)
# 先转为单通道，便于后续处理
getGrayphoto = ModifyPicture.RePhotoGray(ImgRead)
# 形态学处理
cvt_img = ModifyPicture.RePhotoMorphGradient(getGrayphoto, kernel)

while True:
    # BitBltPrintWindow()
    key = cv2.waitKey(10)
    if key & 0xFF == ord('q'):
        break