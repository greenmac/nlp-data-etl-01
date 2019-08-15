# conding=utf-8
import os, fnmatch
from win32com import client as wc
from win32com.client import Dispatch

def pdf2Txt(filePath, savePath=''):
    # 1.切分文件路徑為文件目錄和文件名
    dirs, filename = os.path.split(filePath)

    # 2.修改切分後的文件後綴
    new_name = ''
    if fnmatch.fnmatch(filename, '*.pdf') | fnmatch.fnmatch(filename, '*PDF'):
        new_name = filename[:-4] + '.txt'
    else:
        print('格式不正確, 僅支持 pdf or PDF 格式.')
        return
    
    # 3.設置新的文件保存路徑
    if savePath == '':
        savePath = dirs
    else:
        savePath = savePath
    word2txtPath = os.path.join(savePath, new_name)
    print('-->', word2txtPath)

    # 4.加載文本提取的處理程序, word-->txt
    wordapp = wc.Dispatch('Word.Application')
    mytxt = wordapp.Documents.Open(filePath)

    # 5.保存文本信息
    mytxt.SaveAs(word2txtPath, 4) # 參數4代表抽取文本
    mytxt.Close()
    



if __name__ == '__main__':
    filePath1 = os.path.abspath(r'E:\python\nlp-data-etl-01\wordtotxt\樸素被葉斯文本分類.docx')
    pdf2Txt(filePath1)

    filePath2 = os.path.abspath(r'E:\python\nlp-data-etl-01\wordtotxt\a-python-小甲魚-課後題目.doc')
    pdf2Txt(filePath2)

    filePath3 = os.path.abspath(r'E:\python\nlp-data-etl-01\wordtotxt\data-structure-note.pdf')
    pdf2Txt(filePath3)