# 导入所需包
# os,操作文件和路径
import os
# ghostscript,代码简化
import ghostscript
# pypdf2,拆分pdf
from PyPDF2 import PdfFileReader, PdfFileWriter
# PythonMagick,单页PDF转图片
import PythonMagick
# baidu-aip,百度文字识别
from aip import AipOcr
# pdfkit,字符串制作PDF
import pdfkit

# 参数
path = 'C:/Users/Administrator/Desktop/pdf/pdf_proc'
pdfname = '51022-2008.pdf'
DPI = '300'

# https://console.bce.baidu.com/#/index/overview
# 产品服务->人工智能->文字识别->创建应用
# 获取以下三个值
APP_ID = '??'
API_KEY = '??'
SECRET_KEY = '?? '

# pdfkit安装位置设置,wkhtmltopdf的安装位置
path_wk = r'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
pdfkit_config = pdfkit.configuration(wkhtmltopdf=path_wk)
# pdfkit参数
pdfkit_options = {'encoding': 'UTF-8', }

# PDF转化为图片
os.chdir(path)
pdf_input = PdfFileReader(open(pdfname, 'rb'))
# 自动获取PDF页数
page_count = pdf_input.getNumPages()
page_range = range(page_count)
# 也可以手工指定PDF需要转换的页数
page_range=range(0,100)
# 使用PyPDF和ghostscript
# ==超级好用,超级直观,超级短==
for page_num in page_range:
    # im = Image()
    im = PythonMagick.Image(os.path.join(path, pdfname))
    # im = PythonMagick.Image()
    # im.density(str(DPI))
    im.read(pdfname + '[' + str(page_num) + ']')
    im.write(str(page_num) + '.jpg')

# 图片转化为字符串

# 新建一个AipOcr
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


# 读取本地图片的函数
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 可选参数
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "false"
options["detect_language"] = "false"
options["probability"] = "false"
allteststr = []
for page_num in page_range:
    # 读取本地图片
    image = get_file_content(r'%s\%s.jpg' % (path, page_num))
    # 通用文字识别,得到的是一个dict
    # testjson = client.basicGeneral(image, options)
    teststr = ''
    # for x in testjson['words_result']:
    #     teststr = teststr + x['words'] + '</br>'
    allteststr.append(teststr)

# 字符串写入PDF
for page_num in page_range:
    pdfkit.from_string((allteststr[page_num]), '%s.pdf' % (str(page_num)), configuration=pdfkit_config,
                       options=pdfkit_options)
    pdfkit.from_file()

# 合并单页PDF
pdf_output = PdfFileWriter()
for page_num in page_range:
    os.chdir(path)
    pdf_input = PdfFileReader(open('%s.pdf' % (str(page_num)), 'rw'))
    page = pdf_input.getPage(0)
    pdf_output.addPage(page)
pdf_output.write(open(os.path.join(path, 'newpdf.pdf'), 'wb'))
