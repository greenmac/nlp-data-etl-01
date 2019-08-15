# conding=utf-8
import os, fnmatch
from win32com import client as wc
from win32com.client import Dispatch

def files2Txt(filePath, savePath=''):
    # 1.切分文件路徑為文件目錄和文件名
    dirs, filename = os.path.split(filePath)

    # 2.修改切分後的文件後綴
    typename = os.path.splitext(filename)[-1].lower() # 獲得文件後綴
    new_name = tranType(filename, typename)

    # 3.設置新的文件保存路徑
    if savePath == '':
        savePath = dirs
    else:
        savePath = savePath
    new2txtPath = os.path.join(savePath, str(new_name))
    print('-->', new2txtPath)

    # 4.加載文本提取的處理程序, word-->txt
    wordapp = wc.Dispatch('Word.Application')
    mytxt = wordapp.Documents.Open(filePath)

    # 5.保存文本信息
    mytxt.SaveAs(new2txtPath, 4) # 參數4代表抽取文本
    mytxt.Close()
    
def tranType(filename, typename):
    new_name = ''
    if typename == '.pdf': # pdf-->txt
        if fnmatch.fnmatch(filename, '*.pdf'):
            new_name = filename[:-4] + '.txt'
        else:
            return
    elif typename == '.doc' or typename == '.docx': # word-->txt
        if fnmatch.fnmatch(filename, '*.doc'):
            new_name = filename[:-4] + '.txt'
        elif fnmatch.fnmatch(filename, '*.docx'):
            new_name = filename[:-5] + '.txt'
        else:
            return
    else:
        print('警告: \n 您輸入的[', typename, ']數據不合法, 本抽取工具僅支持doc/docx/pdf格式文件, 請輸入正確格式')
        return
    return new_name




if __name__ == '__main__':
    filePath1 = os.path.abspath(r'E:\python\nlp-data-etl-01\wordtotxt\樸素被葉斯文本分類.docx')
    files2Txt(filePath1)

    filePath2 = os.path.abspath(r'E:\python\nlp-data-etl-01\wordtotxt\a-python-小甲魚-課後題目.doc')
    files2Txt(filePath2)

    filePath3 = os.path.abspath(r'E:\python\nlp-data-etl-01\wordtotxt\data-structure-note.pdf')
    files2Txt(filePath3)