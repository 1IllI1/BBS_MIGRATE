import pymysql

##connect database
#parameter1 host IP   username  passwd  dataname
db = pymysql.connect("127.0.0.1",'root','root','bbs_test')

#create a cursor object
cursor = db.cursor()
##sql
sql = "insert into admin(name,pwd,addtime) values('test1','pbkdf2:sha256:50000$EcB0aUZG$07eb827c6253b2f72b54cb4f606e8922523a51a9d42952fc2235790d4903c13b','2019-01-06 16:44:11')"
##execute
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

cursor.close()
db.close()