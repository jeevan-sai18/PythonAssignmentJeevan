from DAO.implementation import DbConnection

class Employee(DbConnection):

    def __init__(self):
        self.employeeID=''
        self.name=''
        self.email=''
        self.contactNumber=''
        self.role=''
        self.salary=''

    def setter(self):
        self.employeeID=int(input('Enter EmployeeID:'))
        self.name=input('Enter Name:')
        self.email=input('Enter Email:')
        self.contactNumber=input('Enter Contact Number:')
        self.role=input('Enter Role:')
        self.salary=float(input('Enter Salary:'))

        data=[(self.employeeID,self.name,self.email,self.contactNumber,self.role,self.salary)]

        insert_str='''
            INSERT INTO Employee (
                EmployeeID,Name,Email,ContactNumber,Role,Salary
            ) VALUES (%s, %s, %s, %s, %s, %s)
        '''

        self.open()
        self.s.executemany(insert_str,data)
        self.conn.commit()
        print('Employee record inserted successfully..')
        self.close()

    def getter(self):
        self.open()
        select_str='''SELECT * FROM Employee'''
        self.s.execute(select_str)
        records=self.s.fetchall()
        print('')
        print('Records in Employee Table')
        for i in records:
            print(i)
        self.close()

    def update(self):
        self.getter()
        employeeID=int(input('Enter EmployeeID to be Updated:'))
        self.name=input('Enter Name:')
        self.email=input('Enter Email:')
        self.contactNumber=input('Enter Contact Number:')
        self.role=input('Enter Role:')
        self.salary=float(input('Enter Salary:'))

        update_str='''
            UPDATE Employee
            SET Name=%s,Email=%s,ContactNumber=%s,Role=%s,Salary=%s
            WHERE EmployeeID=%s
        '''

        self.open()
        data=[(self.name,self.email,self.contactNumber,self.role,self.salary,employeeID)]
        self.s.executemany(update_str, data)
        self.conn.commit()
        print('Record updated successfully..')
        self.close()

    def delete(self):
        employeeID=int(input('Enter the EmployeeID to be deleted: '))
        delete_str=f'DELETE FROM Employee WHERE EmployeeID={employeeID}'
        self.open()
        self.s.execute(delete_str)
        self.conn.commit()
        print('Record Deleted Successfully..')
        self.close()

