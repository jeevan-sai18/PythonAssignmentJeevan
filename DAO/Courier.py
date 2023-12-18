from DAO.implementation import DbConnection

class Courier(DbConnection):

    def __init__(self):
        self.courierID=''
        self.senderName=''
        self.senderAddress=''
        self.receiverName=''
        self.receiverAddress=''
        self.weight=''
        self.status=''
        self.trackingNumber=''
        self.deliveryDate=''
        self.userID=''

    def setter(self):
        self.courierID=int(input('Enter CourierID:'))
        self.senderName=input('Enter Sender Name:')
        self.senderAddress=input('Enter Sender Address:')
        self.receiverName=input('Enter Receiver Name:')
        self.receiverAddress=input('Enter Receiver Address:')
        self.weight=float(input('Enter Weight:'))
        self.status=input('Enter Status:')
        self.trackingNumber=input('Enter Tracking Number:')
        self.deliveryDate=input('Enter Delivery Date (YYYY-MM-DD):')
        self.userID=int(input('Enter UserID:'))

        data=[(self.courierID,self.senderName,self.senderAddress,self.receiverName,
                 self.receiverAddress,self.weight,self.status,self.trackingNumber,
                 self.deliveryDate,self.userID)]

        insert_str='''
            INSERT INTO Courier (
                CourierID,SenderName,SenderAddress,ReceiverName,
                ReceiverAddress,Weight,Status,TrackingNumber,
                DeliveryDate,UserID
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''

        self.open()
        self.s.executemany(insert_str,data)
        self.conn.commit()
        print('Courier record inserted successfully..')
        self.close()

    def getter(self):
        self.open()
        select_str='''SELECT * FROM Courier'''
        self.s.execute(select_str)
        records=self.s.fetchall()
        print('')
        print('Records in Courier Table')
        for i in records:
            print(i)
        self.close()

    def update(self):
        self.getter()
        courierID=int(input('Enter CourierID to be Updated: '))
        self.senderName=input('Enter Sender Name:')
        self.senderAddress=input('Enter Sender Address:')
        self.receiverName=input('Enter Receiver Name:')
        self.receiverAddress=input('Enter Receiver Address:')
        self.weight=float(input('Enter Weight:'))
        self.status=input('Enter Status:')
        self.trackingNumber=input('Enter Tracking Number:')
        self.deliveryDate=input('Enter Delivery Date (YYYY-MM-DD):')
        self.userID=int(input('Enter UserID:'))

        update_str='''
            UPDATE Courier
            SET SenderName=%s,SenderAddress=%s,ReceiverName=%s,
            ReceiverAddress=%s,Weight=%s,Status=%s,
            TrackingNumber=%s,DeliveryDate=%s,UserID=%s
            WHERE CourierID=%s
        '''

        self.open()
        data=[(self.senderName,self.senderAddress,self.receiverName,
                 self.receiverAddress,self.weight,self.status,
                 self.trackingNumber,self.deliveryDate,self.userID,courierID)]

        self.s.executemany(update_str, data)
        self.conn.commit()
        print('Record updated successfully..')
        self.close()

    def delete(self):
        courierID=int(input('Enter the CourierID to be deleted: '))
        delete_str=f'DELETE FROM Courier WHERE CourierID={courierID}'
        self.open()
        self.s.execute(delete_str)
        self.conn.commit()
        print('Record Deleted Successfully..')
        self.close()

