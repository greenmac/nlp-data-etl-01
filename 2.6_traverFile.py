# conding=utf-8
import os, time

class TraversalFun():
    # 1.初始化, rootDir目標文件路徑
    def __init__(self, rootDir):
        self.rootDir = rootDir

    # 2.遍歷目錄文件
    def traversalDir(self):
        TraversalFun.allFiles(self, self.rootDir)

    # 3.遞歸算法遍歷所有文件, 並打應文建銘(非目錄文件)
    def allFiles(self, rootDir):
        # 獲取根目錄下的所有文件
        for lists in os.listdir(rootDir):
            path = os.path.join(rootDir, lists)
            if os.path.isfile(path):
                print(os.path.abspath(path))
            elif os.path.isdir(path):
                TraversalFun.allFiles(self, path)



if __name__ == '__main__':
    time_start = time.time()
    
    rootDir = r'E:\python\nlp-data-etl-01\wordtotxt'
    tra = TraversalFun(rootDir)
    tra.traversalDir()

    time_end = time.time()
    print('totally cost', (time_end - time_start), 's')