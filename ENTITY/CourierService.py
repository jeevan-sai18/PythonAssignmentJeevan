from DAO.implementation import DbConnection

class CourierService(DbConnection):
    def __init__(self):
        self.ServiceId=''
        self.ServiceName=''
        self.Cost=''
    def Create_table(self):
        create_str='''
        Create table if not exists CourierService(
        ServiceId Int primary key,
        ServiceName varchar(200),
        Cost Decimal(10,2)
        )
        '''
        self.open()
        self.s.execute(create_str)
        print("Table created successfully")
        self.close()
obj=CourierService()
obj.Create_table()