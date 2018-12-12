import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='rootlee212',
                                 db='hw',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "SELECT * FROM photo"
        cursor.execute(sql)
        photoDict = cursor.fetchall()
        print(photoDict)

    with connection.cursor() as cursor:
        line = "SELECT * FROM iso"
        cursor.execute(line)
        isoDict = cursor.fetchall()
        print(isoDict)

    with connection.cursor() as cursor:
        line = "SELECT * FROM device"
        cursor.execute(line)
        deviceDict = cursor.fetchall()
        print(deviceDict)
finally:
    connection.close()


class dbphoto:

    def __init__(self, height, width, path, device,iso):
        self.height=height
        self.width=width
        self.path=path
        self.device=deviceDict[device]['model']
        self.iso=isoDict[iso]['isov']
    def print(self):
        print(self.height,self.width,self.device,self.iso)

test=dbphoto(16,9,"path",1,2)

test.print()