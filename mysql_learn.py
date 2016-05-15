#-*-coding:utf-8-*-

#导入mysql驱动
import mysql.connector

conn = mysql.connector.connect(user ='root',password='843113495gh',database='test')
cursor = conn.cursor()

#创建user表
cursor.execute('create table user_1 (id varchar(20) primary key,name varchar(20))')
#插入一行记录，注意mysql的占位符是%s
cursor.execute('insert into user_1 (id,name) values (%s,%s)',['1','michael'])

#提交事务
conn.commit()
cursor.close()

#运行查询
cursor = conn.cursor()
cursor.execute('select * from user_1 where id =%s',('1',))
values = cursor.fetchall()
print (values)

#关闭cursor和connection
cursor.close()
conn.close()