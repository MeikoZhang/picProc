import glob
import fitz
import os


def pic2pdf():
    doc = fitz.open()
    for img in sorted(glob.glob("C:/Users/Administrator/Desktop/pdf/pdf_proc/*.jpg")):  # 读取图片，确保按文件名排序
        print(img)
        imgdoc = fitz.open(img)                 # 打开图片
        pdfbytes = imgdoc.convertToPDF()        # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)                   # 将当前页插入文档
    if os.path.exists("C:/Users/Administrator/Desktop/pdf/pdf_proc/allimages.pdf"):
        os.remove("C:/Users/Administrator/Desktop/pdf/pdf_proc/allimages.pdf")
    doc.save("C:/Users/Administrator/Desktop/pdf/pdf_proc/allimages.pdf")                   # 保存pdf文件
    doc.close()


if __name__ == '__main__':
    pic2pdf()
