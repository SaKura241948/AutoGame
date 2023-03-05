import random

import cv2

import Click
import ModifyPicture


def callback():
    pass

def JudgmentPhoto():
    img = cv2.imread('photo/YHDOOR.png')
    # 如果想测试，可将test.png换成HOME.png
    img2 = cv2.imread('photo/test.png')
    gray = ModifyPicture.RePhotoGray(img)
    gray2 = ModifyPicture.RePhotoGray(img2)
    # 创建sift特征检测器，4.4版本又重新get回sift特征提取，surf因专利，所以opencv暂时移除
    # ord多于多图片处理快，准确性低（因为减少了关键字和描述子）
    sift = cv2.SIFT_create()
    '''
    detect, computr = orb.detectAndCompute(img, mask)
    detect:关键点,计算关键点，用于检测
    compute：描述子,计算描述子，用于特征匹配
    mask：指明对img中哪个区域进行计算
    '''
    # 进行检测
    kp, des = sift.detectAndCompute(gray, None)
    kp2, des2 = sift.detectAndCompute(gray2, None)
    '''BFMatcher：暴力特征匹配
    流程
    创建匹配器：BFMatcher(normType, crossCheck)
    normType：匹配算法，下面描述算法对应用法
    NORM_L1或NORM_L2 :用于sift或surf
    NORM_HAMMING: 用于ORB
    croossCheck：是否进行交叉匹配, 默认false
    进行特征匹配：bf.match(des1, des2)
    展示绘制匹配点：cv2.drawMatches(img1, kp1, img2, kp2, bf.match(des1, des2))
    '''
    # bf = cv2.BFMatcher(cv2.NORM_L1)
    # matches = bf.match(des, des2)
    # # 绘制关键点
    # img3 = cv2.drawMatches(img, kp, img2, kp2, matches, None)
    # while True:
    #     cv2.imshow('img', img3)
    #     key = cv2.waitKey(0)
    #     if key & 0xFF == ord('q'):
    #         break
    # cv2.destroyAllWindows()
    '''
    FlannBasedMatcher:flann特征匹配
    进行批量特征匹配时，FLANN速度更快，使用的是邻近近似值， 所以精度较差
    流程
    创建匹配器：FlannBasedMatcher(index_params, search_params)
    index_params字典：匹配算法KDTREE用于sift，LSH用于orb
    search_params字典：指定KDTREE算法中遍历树的次数
    '''
    # 创建匹配器
    index_params = dict(algorithm=1, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    # 对描述子进行匹配计算，k表示取欧式距离最近的前K个关键点，返回DMatch
    '''
    DMatch的内容
    distance, 描述子之间的距离，值越低越好
    queryIdx,  第一个图像的描述子索引值
    trainIdx, 第二个图像的描述子索引值
    imgIdx, 第二个图像的索引值'''
    matchs = flann.knnMatch(des, des2, k=2)
    good = []
    CoordinateValue = []
    for i, (m, n) in enumerate(matchs):
        if m.distance < 0.3 * n.distance:
            img2_idx = m.trainIdx
            (x2, y2) = kp2[img2_idx].pt
            # 存储坐标
            CoordinateValue.append((int(x2), int(y2)))
            good.append(m)
    ret = cv2.drawMatchesKnn(img, kp, img2, kp2, [good], None)
    if len(CoordinateValue) != 0:
        getRadomNum = random.randint(0, len(CoordinateValue))
        Click.moveCurPos(CoordinateValue[getRadomNum][0], CoordinateValue[getRadomNum][1])
    # cv2.imshow('result', ret)
    cv2.waitKey(0)

JudgmentPhoto()