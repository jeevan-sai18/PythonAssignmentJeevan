from DAO.implementation import DbConnection

class CourierCompany(DbConnection):
    def __init__(self):
        self.CompanyName=''
        self.CourierDetails=''
        self.EmployeeDetails=''
        self.LocationDetails=''
    def Create_table(self):
        create_str='''
        Create table if not exists CourierCompany(
        CompanyName varchar(200) primary key,
        CourierDetails Int,
        EmployeeDetails Int,
        LocationDetails Int,
        foreign key (CourierDetails) references Courier(CourierID),
        foreign key (EmployeeDetails) references Employee(EmployeeID),
        foreign key (LocationDetails) references Location(LocationId)
        )
        '''
        self.open()
        self.s.execute(create_str)
        print("Table created successfully")
        self.close()
obj=CourierCompany()
obj.Create_table()