from DAO.implementation import DbConnection

class Payment(DbConnection):
    def __init__(self):
        self.PaymentId=''
        self.CourierId=''
        self.LocationId=''
        self.Amount=''
        self.PaymentDate=''
    def Create_table(self):
        create_str='''
        Create table if not exists Payment(
        PaymentId Int primary key,
        CourierId Int,
        LocationId int,
        Amount Decimal(10,2),
        PaymentDate date,
        foreign key (CourierId) references Courier (CourierID),
        foreign key (LocationId) references Location (LocationId)
        )
        '''
        self.open()
        self.s.execute(create_str)
        print("Table created successfully")
        self.close()
obj=Payment()
obj.Create_table()