import pymysql

db = pymysql.connect(host = 'localhost',user = 'root',password = 'woaiziji',db = 'spiders')
cursor = db.cursor()
sql = 'UPDATE students SET age = 25 WHERE name = "Bob"'
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()