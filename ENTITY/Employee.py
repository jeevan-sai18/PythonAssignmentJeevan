from DAO.implementation import DbConnection

class Employee(DbConnection):
    def __init__(self):
        self.EmployeeID=''
        self.EmployeeName=''
        self.email=''
        self.Contact=''
        self.Role=''
        self.Salary=''

    def Create_table(self):
        create_str='''
        Create table if not exists Employee(
        EmployeeID INT PRIMARY KEY,
        Name VARCHAR(255),
        Email VARCHAR(255) UNIQUE,
        ContactNumber VARCHAR(20),
        Role VARCHAR(50),
        Salary DECIMAL(10, 2)
        )
        '''
        self.open()
        self.s.execute(create_str)
        print("Table Created successfully")
        self.close()
obj=Employee()
obj.Create_table()