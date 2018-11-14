# pip install pymongo
import pymongo

myclient = pymongo.MongoClient("mongodb://172.16.0.10:27017/")

dblist = myclient.list_database_names()

for db in dblist:
    print(db)

if "uic" in dblist:
    print("数据库已存在！")

myclient.close()