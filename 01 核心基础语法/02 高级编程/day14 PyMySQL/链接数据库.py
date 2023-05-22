import pymysql

'''
1、建立数据库链接对象
pymysql.connect(
    host=,链接MySQL主机地址，本机就直接写localhost ， 127.0.0.1
    user=, 链接的MySQL数据库用户名
    password=,数据库密码
    charset=,字符编码utf8
    database= 要链接的数据库名称
)
2、创建游标对象（用来执行sql语句）
3、操作数据
4、关闭游标
5、关闭数据库链接
'''

db = pymysql.connect(
    host='localhost',
    user='root',
    password='rootbxml',
    charset='utf8',
    database='class13'
)

# 创建游标对象（用来执行sql语句）
cur = db.cursor()

# 创建数据表
# sql = 'create table ac(id int, name varchar(5))'

# 执行sql语句
# cur.execute(sql)

# 插入数据
# pymysql中插入数据需要对其进行提交操作
# sql = 'insert into ac values(1, "墨离")'
# cur.execute(sql)
# db.txt.commit()

# 把每一条数据用元组类型保存，最后将多个元组数据放到一个列表中，将列表跟sql语句一起交给游标执行
# sql = 'insert into ac values(%s, %s)'
# values = [
#     (2, '莫安心'),
#     (3, '李华'),
#     (4, '狂风'),
#     (5, '晓东'),
#     (6, '赴桂'),
#     (7, '阿真'),
# ]

# 提交多条数据时使用游标的方法：executemany(sql语句， 数据）
# cur.executemany(sql, values)
# db.txt.commit()

# 数据修改
# sql = 'update ac set id = 11 where name = "墨离"'
# cur.execute(sql)
# db.txt.commit()

# 删除
# sql = 'delete from ac where id=11'
# cur.execute(sql)
# db.txt.commit()

# 查询数据
sql = 'select * from ac'
cur.execute(sql)
# fetchall获取所有数据
print(cur.fetchall())

# fetchmany获取指定条数数据，不指定条数，只会返回一条数据
# print(cur.fetchmany(3))

# fetchone获取一条数据
# print(cur.fetchmany())

# 关闭游标
cur.close()

# 关闭数据库链接
db.close()
