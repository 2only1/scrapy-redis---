'''
将数据从redis中导入到mongo中
- redis 不适合长期 存储数据
'''
# pip install redis == 4.3.4

import redis
import pymongo
from json import loads

# 链接redis
r_client = redis.Redis(host='localhost', port=6379, db=0)
# 链接mongodb
m_client = pymongo.MongoClient()
# 指定mongo的数据库与集合
lianjia = m_client.room.lianjia
while True:
    # 取出redis中的数据,s是key d是数据，是bytes类型
    s,d = r_client.blpop(['lianjia3:items']) 
    # 将bytes类型转换为oject类型
    data = loads(d)
    # 将数据插入到mongodb中
    lianjia.insert_one(data)