# conding=utf-8
import os, time
import extractTxt as ET

class TraversalFun():
    # 1.初始化, rootDir目標文件路徑
    def __init__(self, rootDir, func=None, saveDir=''):
        self.rootDir = rootDir # 目標文件夾路徑
        self.func = func # 方法參數, 實現文本提取
        self.saveDir = saveDir # 文件夾保存路徑

    # 2.遍歷目錄文件
    def traversalDir(self):
        # 切分文件目錄和文件名
        dirs, filename = os.path.split(self.rootDir)

        # 保存目錄
        save_dir = ''
        if self.saveDir == '':
            save_dir = os.path.abspath(os.path.join(dirs, 'new_' + filename))
        else:
            save_dir = self.save_dir

        # 創建保存路徑
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        print('保存目錄:\n', save_dir)
        # 遍歷文件抽取txt文本內容
        TraversalFun.allFiles(self, self.rootDir, save_dir)

    # 3.遞歸算法遍歷所有文件, 並打應文建銘(非目錄文件)
    def allFiles(self, rootDir, save_dir=''):
        # 獲取根目錄下的所有文件
        for lists in os.listdir(rootDir):
            path = os.path.join(rootDir, lists)
            # 核心算法,對文件類型文本信息抽取並保存
            if os.path.isfile(path):
                self.func(os.path.abspath(path), os.path.abspath(save_dir))
            # 遞歸遍歷目錄
            elif os.path.isdir(path):
                newsave_dir = os.path.join(save_dir, lists)
                if not os.path.exists(newsave_dir):
                    os.mkdir(newsave_dir)
                TraversalFun.allFiles(self, path, save_dir)



if __name__ == '__main__':
    time_start = time.time()
    
    saveDir = r'E:\\'
    rootDir = r'E:\python\nlp-data-etl-01\wordtotxt'
    tra = TraversalFun(rootDir, ET.files2Txt)
    tra.traversalDir()

    time_end = time.time()
    print('Totally cost', (time_end - time_start), 's')