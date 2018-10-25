######图片切割##########

import os
import os.path
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import time

#########################切割函数#########################################
def segment(im):
    s = 6  # 首次第一个点的横坐标
    w = 16  # 宽度
    h = 20  # 第二个点的纵坐标
    t = 0  # 第一个点的纵坐标
    im_new = []  # 在一张图片裁剪四个区域
    # for i in range(4):
    #       im1=im.crop((s+w*i,t,s+w*(i+1),h))  #crop函数得到局部区域
    #       im_new.append(im1)
    im1 = im.crop((6, 0, 6 + 17, 20))
    im_new.append(im1)
    im1 = im.crop((23, 0, 23 + 16, 20))
    im_new.append(im1)
    im1 = im.crop((39, 0, 39 + 16, 20))
    im_new.append(im1)

    im1 = im.crop((55, 0, 55 + 18, 20))
    im_new.append(im1)
    return im_new


#################图片增强######################################
def binarizing(im, threshold):
    pixdata = im.load()
    w, h = im.size
    for j in range(h):
        for i in range(w):
            if pixdata[i, j] < threshold:
                pixdata[i, j] = 0
            else:
                pixdata[i, j] = 255
    return im


################################图片去噪############################
def denoising(im):
    pixdata = im.load()
    w, h = im.size
    for j in range(1, h - 1):
        for i in range(1, w - 1):
            count = 0
            if pixdata[i, j - 1] > 245:
                count = count + 1
            if pixdata[i, j + 1] > 245:
                count = count + 1
            if pixdata[i + 1, j] > 245:
                count = count + 1
            if pixdata[i - 1, j] > 245:
                count = count + 1
            if count > 2:
                pixdata[i, j] = 255
    return im


##############图片转换:打开图片,滤波器,增强,灰度图转换,去噪,二值化############
def imgTransfer(f_name):
    im = Image.open(f_name)  # 打开图片
    im = im.filter(ImageFilter.MedianFilter(1))  # 对于输入图像的每个像素点，该滤波器从（size，size）的区域中拷贝中值对应的像素值存储到输出图像中
    # enhancer=ImageEnhance.Contrast(im)
    # im=enhancer.enhance(1)
    im = ImageEnhance.Contrast(im).enhance(
        1.5)  # enhance()的参数factor决定着图像的对比度情况。从0.1到0.5，再到0.8，2.0，图像的对比度依次增大.0.0为纯灰色图像;1.0为保持原始
    im = im.convert('L')  # 灰度图转换
    im = denoising(im)  # 图片去噪
    im = binarizing(im, 200)  # 图片二值化
    # im=nse.removeNoisy(im)
    # im.save('/User/iswin/Downloads/vim/test.clear.jpg','jpeg')
    # im.show()
    return im


#####批量裁剪图片,并保存######################################
def cutPictures(img):
        im = imgTransfer(img)  #####图片预处理,二值化,图片增强
        pics = segment(im)  #######用crop函数裁剪
        for pic in pics:
            pic.save('G:\Test\%s.jpg' % (int(time.time() * 1000000)), 'jpeg')


rootdir = u'G:\Test'
for parent, dirnames, filenames in os.walk(rootdir):
    for dirname in dirnames:
        print("dirname is:" + dirname)
        print("parent is:" + parent)

    for filename in filenames:
        print("filename is:" + filename)
        print("parent is:" + parent)
        print("the full name is:" + os.path.join(parent, filename))
        cutPictures(os.path.join(parent, filename))
