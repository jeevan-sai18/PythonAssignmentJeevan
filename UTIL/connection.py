import mysql.connector as sql

class DBConnection:
    @staticmethod
    def getConnection():
        try:
            conn=sql.connect(host='localhost', database='assignment', user='root', password='jeeva')
            s=conn.cursor()
            print("Database is connected")
        except Exception as e:
            print(str(e) + "---Database is not Connected:--")


