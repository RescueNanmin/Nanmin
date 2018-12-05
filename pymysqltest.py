import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='Eddy12358',
                                 db='test',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "SELECT * FROM photo"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    connection.close()