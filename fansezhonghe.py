import numpy as numpy
import cv2 as cv2


def reverse_pixel():
    test_dir = 'D:/ztest/test_dir/test.jpg'
    mask_dir = 'D:/ztest/mask_dir/mask.jpg'
    save_dir = 'D:/ztest/save_dir/save.jpg'
    src = cv2.imread(test_dir)
    mask = cv2.imread(mask_dir)
    save = numpy.zeros(src.shape, numpy.uint8)
    for row in range(src.shape[0]):
        for col in range(src.shape[1]):
            for channel in range(src.shape[2]):
                if mask[row, col, channel] == 0:
                    val = 0
                else:
                    reverse_val = 255 - src[row, col, channel]
                    val = 255 - reverse_val * 256 / mask[row, col, channel]
                    if val < 0:
                        val = 0
                save[row, col, channel] = val
    cv2.imwrite(save_dir, save)


def inpaint():
    # 默认的彩色图(IMREAD_COLOR)方式读入原始图像
    src = cv2.imread('D:/ztest/test_dir/test1.jpg')
    #  灰度图(IMREAD_GRAYSCALE)方式读入水印蒙版图像
    mask = cv2.imread('D:/ztest/mask_dir/mask1.jpg', cv2.IMREAD_GRAYSCALE)
    print(src.shape)
    print(mask.shape)
    #  参数：目标修复图像; 蒙版图（定位修复区域）; 选取邻域半径; 修复算法(包括INPAINT_TELEA/INPAINT_NS， 前者算法效果较好)
    dst = cv2.inpaint(src, mask, 3, cv2.INPAINT_TELEA)
    cv2.imwrite('D:/ztest/save_dir/save.jpg', dst)


inpaint()

