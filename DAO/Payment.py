from DAO.implementation import DbConnection

class Payment(DbConnection):

    def __init__(self):
        self.paymentId=''
        self.courierId=''
        self.locationId=''
        self.amount=''
        self.paymentDate=''

    def setter(self):
        self.paymentId=int(input('Enter PaymentId:'))
        self.courierId=int(input('Enter CourierId:'))
        self.locationId=int(input('Enter LocationId:'))
        self.amount=float(input('Enter Amount:'))
        self.paymentDate=input('Enter Payment Date (YYYY-MM-DD):')

        insert_str='''
            INSERT INTO Payment (
                PaymentId, CourierId, LocationId, Amount, PaymentDate
            ) VALUES (%s, %s, %s, %s, %s)
        '''

        data=[(self.paymentId, self.courierId, self.locationId, self.amount, self.paymentDate)]

        self.open()
        self.s.executemany(insert_str, data)
        self.conn.commit()
        print('Payment record inserted successfully..')
        self.close()

    def getter(self):
        self.open()
        select_str='''SELECT * FROM Payment'''
        self.s.execute(select_str)
        records=self.s.fetchall()
        print('')
        print('Records in Payment Table')
        for i in records:
            print(i)
        self.close()

    def update(self):
        self.getter()
        paymentId=int(input('Enter PaymentId to be Updated: '))
        self.courierId=int(input('Enter CourierId:'))
        self.locationId=int(input('Enter LocationId:'))
        self.amount=float(input('Enter Amount:'))
        self.paymentDate=input('Enter Payment Date (YYYY-MM-DD):')

        update_str='''
            UPDATE Payment
            SET CourierId=%s, LocationId=%s, Amount=%s, PaymentDate=%s
            WHERE PaymentId=%s
        '''

        data=[(self.courierId,self.locationId,self.amount,self.paymentDate,paymentId)]

        self.open()
        self.s.executemany(update_str, data)
        self.conn.commit()
        print('Record updated successfully..')
        self.close()

    def delete(self):
        paymentId=int(input('Enter the PaymentId to be deleted: '))
        delete_str=f'DELETE FROM Payment WHERE PaymentId={paymentId}'
        self.open()
        self.s.execute(delete_str)
        self.conn.commit()
        print('Record Deleted Successfully..')
        self.close()


