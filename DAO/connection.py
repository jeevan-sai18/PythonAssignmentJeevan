from UTIL.connection import DBConnection

class CourierServiceDb:
    def __init__(self):
        CourierServiceDb.connection=DBConnection.getConnection()
obj=CourierServiceDb()