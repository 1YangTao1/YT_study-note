import pymysql

#建立数据库
db = pymysql.connect(host='localhost',user='root',password='woaiziji',port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
#获取MySQL当前版本
data = cursor.fetchone()
#调用fetchone获取第一条数据，即得到了版本号
print('Database version:',data)
#输出该版本号
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
#创建数据库，数据库名spiders

#创建表



