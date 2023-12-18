from DAO.implementation import DbConnection

class Courier(DbConnection):
    def __init__(self):
        self.CourierID=''
        self.SenderName=''
        self.SenderAddress=''
        self.ReceiverName=''
        self.ReceiverAddress=''
        self.Weight=''
        self.Status=''
        self.TrackingNumber=''
        self.DeliveryDate=''
        self.UserID=''
    def create_table(self):
        create_str = '''
            CREATE TABLE IF NOT EXISTS Courier (
                CourierID INT PRIMARY KEY,
                SenderName VARCHAR(255),
                SenderAddress TEXT,
                ReceiverName VARCHAR(255),
                ReceiverAddress TEXT,
                Weight DECIMAL(5, 2),
                Status VARCHAR(50),
                TrackingNumber VARCHAR(20) UNIQUE,
                DeliveryDate DATE,
                UserID INT,
                foreign key(UserID) References User(UserID)
            )
        '''
        self.open()
        self.s.execute(create_str)
        self.close()
        print('Courier table created successfully')

# Example usage:
obj = Courier()
obj.create_table()
