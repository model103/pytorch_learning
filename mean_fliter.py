import numpy as np
import cv2


def mean_fliter(src, k: int):
    '''
    :param src: 源图
    :param k: 卷积核大小
    :return: dst：滤波后图片
    '''
    dst_mean = np.copy(src)
    dst_median = np.copy(src)
    src = np.pad(src, (int((k - 1) / 2), int((k - 1) / 2)), 'constant')
    w,h = dst_mean.shape
    for i in range(w):
        for j in range(h):
            dst_mean[i, j] = np.mean(src[i:i+k,j:j+k])
            dst_median[i, j] = np.median(src[i:i + k, j:j + k])
    return dst_mean,dst_median
img = cv2.imread('1.jpg',0)
dst_mean, dst_median = mean_fliter(img,15)
cv2.imshow('src',img)
cv2.imshow('dst_mean',dst_mean)
cv2.imshow('dst_meidan',dst_median)
cv2.waitKey(0)



