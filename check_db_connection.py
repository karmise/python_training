import pymysql.cursors


connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")


try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for raw in cursor.fetchall():
        print(raw)
finally:
    connection.close
