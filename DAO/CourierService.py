from DAO.implementation import DbConnection

class CourierService(DbConnection):

    def __init__(self):
        self.serviceId=''
        self.serviceName=''
        self.cost=''

    def setter(self):
        self.serviceId=int(input('Enter ServiceId:'))
        self.serviceName=input('Enter Service Name:')
        self.cost=float(input('Enter Cost:'))

        insert_str='''
            INSERT INTO CourierService (
                ServiceId,ServiceName,Cost
            ) VALUES (%s, %s, %s)
        '''

        data=[(self.serviceId,self.serviceName,self.cost)]

        self.open()
        self.s.executemany(insert_str, data)
        self.conn.commit()
        print('CourierService record inserted successfully..')
        self.close()

    def getter(self):
        self.open()
        select_str='''SELECT * FROM CourierService'''
        self.s.execute(select_str)
        records=self.s.fetchall()
        print('')
        print('Records in CourierService Table')
        for i in records:
            print(i)
        self.close()

    def update(self):
        self.getter()
        serviceId=int(input('Enter ServiceId to be Updated: '))
        self.serviceName=input('Enter Service Name:')
        self.cost=float(input('Enter Cost:'))

        update_str='''
            UPDATE CourierService
            SET ServiceName=%s, Cost=%s
            WHERE ServiceId=%s
        '''

        data=[(self.serviceName,self.cost,serviceId)]

        self.open()
        self.s.executemany(update_str,data)
        self.conn.commit()
        print('Record updated successfully..')
        self.close()

    def delete(self):
        serviceId=int(input('Enter the ServiceId to be deleted: '))
        delete_str=f'DELETE FROM CourierService WHERE ServiceId={serviceId}'
        self.open()
        self.s.execute(delete_str)
        self.conn.commit()
        print('Record Deleted Successfully..')
        self.close()

