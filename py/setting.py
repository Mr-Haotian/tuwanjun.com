from pymongo import MongoClient
from py.Logs import Logger
# 数据库初始化
conn = MongoClient('mongodb://localhost:27017/')
db = conn.testdb
my_set = db.tuwanjun
# 日志初始化
# LogPath = 'Logs_dir/'
iszip_logs = Logger('Invalid_download_link.log', 1, 'iszip').getlog()
isres_logs = Logger('Invalid_response_status.log', 1, 'isres').getlog()
isnetw_logs = Logger('Invalid_network_status.log', 1, 'isnetw').getlog()
isfile_logs = Logger('temp.log',1,'isfile').getlog()
isdown_logs = Logger('file_down.log',1,'isdown').getlog()
