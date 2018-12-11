from threading import Thread
from Logs import Logger
from setting import *
import requests
import pymongo
import os

class  DownFile():
    '''
    根据地址下载图片
    '''
    def __init__(self):
        '''日志初始化'''
        self.isfile = isfile_logs
        self.isdown = isdown_logs


    def load_db(self):
        '''读取MongoDB数据库信息'''
        sql = my_set.find({},{'_id':0,'links':0}).limit(3)
        return sql


    def get_images_res(self,data):
        '''图片下载模块,处理下载与存储'''
        ID = data['ID']
        Title = data['Title']
        Total = data['Total']
        path = './zip_dir/'
        filename = '%s_%s_%s.zip'%(ID,Title,Total)
        if os.path.exists(path + filename):
            self.isfile.info('%s已经存在,跳过下载!'% filename)
        else:
            res = requests.get(data['down_url'])
            with open(path + filename,'wb') as f:
                f.write(res.content)
            self.isdown.info('%s下载完成!'%filename)




if __name__ == '__main__':
    df = DownFile()
    data = df.load_db()
    for info in data:
        t = Thread(target=df.get_images_res, args=(info,))
        t.start()

