from DAO.implementation import DbConnection

class CourierCompany(DbConnection):

    def __init__(self):
        self.companyName=''
        self.courierDetails=''
        self.employeeDetails=''
        self.locationDetails=''

    def setter(self):
        self.companyName=input('Enter Company Name:')
        self.courierDetails=int(input('Enter CourierDetails (CourierID):'))
        self.employeeDetails=int(input('Enter EmployeeDetails (EmployeeID):'))
        self.locationDetails=int(input('Enter LocationDetails (LocationId):'))

        insert_str='''
            INSERT INTO CourierCompany (
                CompanyName, CourierDetails, EmployeeDetails, LocationDetails
            ) VALUES (%s, %s, %s, %s)
        '''

        data = [(self.companyName,self.courierDetails,self.employeeDetails,self.locationDetails)]

        self.open()
        self.s.executemany(insert_str, data)
        self.conn.commit()
        print('CourierCompany record inserted successfully..')
        self.close()

    def getter(self):
        self.open()
        select_str='''SELECT * FROM CourierCompany'''
        self.s.execute(select_str)
        records=self.s.fetchall()
        print('')
        print('Records in CourierCompany Table')
        for i in records:
            print(i)
        self.close()

    def update(self):
        self.getter()
        companyName=input('Enter Company Name to be Updated: ')
        self.courierDetails=int(input('Enter CourierDetails (CourierID):'))
        self.employeeDetails=int(input('Enter EmployeeDetails (EmployeeID):'))
        self.locationDetails=int(input('Enter LocationDetails (LocationId):'))

        update_str='''
            UPDATE CourierCompany
            SET CourierDetails=%s, EmployeeDetails=%s, LocationDetails=%s
            WHERE CompanyName=%s
        '''

        data=[(self.courierDetails,self.employeeDetails,self.locationDetails,companyName)]

        self.open()
        self.s.executemany(update_str, data)
        self.conn.commit()
        print('Record updated successfully..')
        self.close()

    def delete(self):
        companyName=input('Enter the Company Name to be deleted: ')
        delete_str=f'DELETE FROM CourierCompany WHERE CompanyName={companyName}'
        self.open()
        self.s.execute(delete_str)
        self.conn.commit()
        print('Record Deleted Successfully..')
        self.close()


