from DAO.implementation import DbConnection

class Loction(DbConnection):
    def __init__(self):
        self.LocationId=''
        self.LocationName=''
        self.Adress=''
    def Create_table(self):
        create_str='''
        Create table if not exists Location(
        LocationId Int primary key,
        LocationName varchar(200),
        Address varchar(200) 
        
        )
        '''
        self.open()
        self.s.execute(create_str)
        print("Table created successfully")
        self.close()
obj=Loction()
obj.Create_table()