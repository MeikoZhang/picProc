import fitz
import glob


def rightinput(desc):
    flag=True
    while(flag):
        instr = input(desc)
        try:
            intnum = eval(instr)
            if type(intnum)==int:
                flag = False
        except:
            print('请输入正整数！')
            pass
    return intnum


pdffile = glob.glob("*.pdf")[0]
doc = fitz.open(pdffile)

flag = rightinput("输入：1：全部页面；2：选择页面\t")
if flag == 1:
    strat = 0
    totaling = doc.pageCount
else:
    strat = rightinput('输入起始页面：') - 1
    totaling = rightinput('输入结束页面：')

for pg in range(strat, totaling):
    page = doc[pg]
    zoom = int(100)
    rotate = int(0)
    trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).preRotate(rotate)
    pm = page.getPixmap(matrix=trans, alpha=False)
    pm.writePNG('pdf2png/%s.png' % str(pg+1))