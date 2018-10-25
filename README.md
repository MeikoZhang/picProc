图片版PDF无法复制,转化成文字版的PDF后使用更方便.

我们需要用到python3.6,pypdf2,ghostscript,PythonMagick,百度文字识别服务和pdfkit.

#安装

安装python3.6 略

安装ghostscript
https://ghostscript.com/download/gsdnld.html

安装wkhtmltopdf
https://wkhtmltopdf.org/downloads.html

pip安装PyPDF2,ghostscript,baidu-aip,pdfkit

    pip install PyPDF2
    pip install ghostscript
    pip install baidu-aip
    pip install pdfkit


pip安装PythonMagick
https://www.lfd.uci.edu/~gohlke/pythonlibs/

cd 下载目录
pip install PythonMagick‑0.9.13‑cp36‑cp36m‑win_amd64.whl

#pypdf2用于拆分和合并PDF

示例代码如下:

    #导入PdfFileReader和PdfFileWriter
    from PyPDF2 import PdfFileReader, PdfFileWriter
    #获取一个pdf对象
    pdf_input = PdfFileReader(open(r'pdf路径', 'rb'))
    #获取pdf页数
    page_count = pdf_input.getNumPages()
    #获取pdf第四页的内容
    page = pdf_input.getPage(3)
    page['/Contents']
    #获取一个pdfWriter对象
    pdf_output = PdfFileWriter()
    # 将一个 PageObject 加入到 PdfFileWriter 中
    pdf_output.addPage(page)
    #把新pdf保存
    pdf_output.write(open(r'新pdf路径','wb'))

#PythonMagick用于将单页PDF转化为jpg

#百度云-文字识别-python SDK
每天有500次免费的识别
示例代码如下:

    #导入baidu-aip
    from aip import AipOcr
    #https://console.bce.baidu.com/#/index/overview
    #产品服务->人工智能->文字识别->创建应用
    #获取以下三个值
    APP_ID = '??'
    API_KEY = '??'
    SECRET_KEY = '?? '
    #新建一个AipOcr
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    #读取本地图片的函数
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    #读取本地图片
    image = get_file_content('p1.jpg')
    #可选参数
    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["probability"] = "true"
    #通用文字识别
    client.basicGeneral(image, options)
    
    #读取网络图片
    url = "https://note.youdao.com/yws/public/resource/1577071c1ffa2b6bf4e238ef6dbcfbf5/xmlnote/E5A19BEDFEBA4879B217C5BBF53B0245/22138"
    #可选参数
    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["probability"] = "true"
    #通用文字识别
    client.basicGeneralUrl(url, options)
    
    #读取本地表格图片的函数
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    #读取本地表格图片
    image = get_file_content('p2.jpg')
    #可选参数
    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["probability"] = "true"
    #通用文字识别
    client.basicGeneral(image, options)
    #读取表格分割效果较差!


#pdfkit用于利用字符串生成pdf

示例代码如下:

    #pdfkit安装位置设置
    path_wk = r'pdfkit安装位置设置'
    pdfkit_config = pdfkit.configuration(wkhtmltopdf = path_wk)
    #pdfkit参数
    pdfkit_options = {'encoding': 'UTF-8',}
    #制作PDF
    pdfkit.from_string(('string'),'D:\test.pdf',configuration=pdfkit_config,options=pdfkit_options)
    
    
原文出自
    https://blog.csdn.net/sqq513/article/details/79368243
    
PythonMagic坑
    http://p-s.co.nz/wordpress/pdf-to-png-using-pythonmagick/

Python下ImportError: DLL load failed: 找不到指定的模块之问题分析
    https://blog.csdn.net/blueheart20/article/details/79612985    
    要管理员去运行命令
    
Python图片转换pdf
    https://blog.csdn.net/chaochao670/article/details/79349198