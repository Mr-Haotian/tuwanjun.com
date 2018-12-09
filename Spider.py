from fake_useragent import UserAgent
from pymongo import MongoClient
import requests
import time


class TuWwanImages():
    '''
    兔玩网图片下载
    '''
    def __init__(self):
        self.url = 'https://api.tuwan.com/apps/Welfare/detail?format=json&id='
        self.headers = {
            'Referer': 'https://www.tuwanjun.com/',
            'User-Agent': UserAgent(use_cache_server=False).random,
        }
        # mongoDB初始化
        conn = MongoClient('mongodb://localhost:27017/')
        db = conn.testdb
        self.my_set = db.tuwanjun


    def get_info(self,id):
        '''
        获取图片标题,图片数量以及图片压缩包
        :return:返回一个包含ID,标题,长度,下载链接,原链接的字典
        '''
        url = self.url+str(id)
        res = requests.get(url,headers=self.headers)
        print("id:%s Stuse is %s" %(id,res.status_code))
        status = res.status_code
        if status == 200:
            info = res.json()
            if info['error'] == 0:
                title = info['title']
                total = info['total']
                id = info['id']
                image_zip_url = info['url']
                links = 'https://www.tuwanjun.com/?id=%d'%id
                if image_zip_url[-3:] != 'zip':
                    with open('Down_url_error.log','a') as f:
                        f.write("query:%s\nlinks:%s\nDown_url:%s" %(url,links,image_zip_url))
                    print("下载链接错误:%s"%image_zip_url)
                    return None
                print("id:%s title:%s total:%s\nimages:%s\nlinks:%s" % (id,title,total,image_zip_url,links))
                return {'ID':id,'Title':title,'Total':total,'down_url':image_zip_url,'links':links}
            else:
                with open('logs.log','a') as f:
                    f.write('url:%s\nid:%s\tstatus:%s\n'%(url,id,status))
                print(info['error_msg'])
                return None
        else:
            with open('network_logs','a') as f:
                f.write("id:%s Stuse is %s" %(id,status))


    def save_info(self,data):
        '''
        保存到MongoDB数据库,后面继续二次开发下载以及解压
        :return:
        '''
        self.my_set.save(data)
        pass

if __name__ == '__main__':
    TW = TuWwanImages()
    for i in range(1,1301):
        temp = TW.get_info(i)
        if temp:
            TW.save_info(temp)
    pass
    # temp = TW.get_info(1294)
    # TW.save_info(temp)
    # print(1111111)