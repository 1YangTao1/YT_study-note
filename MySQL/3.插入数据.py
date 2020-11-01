import pymysql
id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host = 'localhost',user = 'root',password = 'woaiziji',db = 'spiders')
cursor = db.cursor()
sql = 'INSERT INT0 students(id,name,age) values(%s, %s, %s)'
try:
    cursor.execute(sql,(id,user,age))
    db.commit()
    #需要执行db对象的Commit()方法才可实现数据的插入。对于数据插入、更新、删除操作，都需要调用该方法才能生效
except:
    db.rollback()
    #数据插入异常，执行数据回滚
db.close()
