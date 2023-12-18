import mysql.connector as sql


class DbConnection:

    def open(self):
        try:
            self.conn = sql.connect(host='localhost',database='assignment',user='root',password='jeeva')
            self.s = self.conn.cursor()
            print("Database is connected")
        except Exception as e:
            print(str(e) + "---Database is not Connected:--")

    def close(self):
        self.conn.close()
        print('Connection Close:')
