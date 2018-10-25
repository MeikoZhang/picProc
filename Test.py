from PIL import Image
import os


def proc_img(path):

    img = Image.open(path)
    # img = img.convert('L')

    pixdata = img.load()
    w, h = img.size
    print((w, h))

    for j in range(h):
        for i in range(w):
            r, g, b = pixdata[i,j]
            # if i < 153 or i > w - 152 or j < 123 or j > h - 150:
            #     pixdata[i, j] = 255
            # else:
            #     if pixdata[i, j] < 180:
            #         pixdata[i, j] = pixdata[i, j]
            #     else:
            #         pixdata[i, j] = 255

    # img.show()
    # img.save(path)


# proc_img("C:/Users/Administrator/Desktop/pdf处理/俄罗斯/pdf_img/AA_GOST_IEC_61189-3-2013_页面_02_图像_0001.jpg")
count = 0
rootdir = 'C:/Users/Administrator/Desktop/pdf处理/俄罗斯/pdf_img'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(list)):
    path = os.path.join(rootdir, list[i])
    if os.path.isfile(path):
        # 你想对文件的操作
        proc_img(path)

    count += 1
    print('已处理完成第%s个文件' % (count))


# getMinThreadhold()


