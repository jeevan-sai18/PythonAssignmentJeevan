from DAO.implementation import DbConnection

class Location(DbConnection):

    def __init__(self):
        self.locationId=''
        self.locationName=''
        self.address=''

    def setter(self):
        self.locationId=int(input('Enter LocationId:'))
        self.locationName=input('Enter Location Name:')
        self.address=input('Enter Address:')

        data=[(self.locationId,self.locationName,self.address)]

        insert_str='''
            INSERT INTO Location (
                LocationId, LocationName, Address
            ) VALUES (%s,%s,%s)
        '''

        self.open()
        self.s.executemany(insert_str,data)
        self.conn.commit()
        print('Location record inserted successfully..')
        self.close()

    def getter(self):
        self.open()
        select_str='''SELECT * FROM Location'''
        self.s.execute(select_str)
        records=self.s.fetchall()
        print('')
        print('Records in Location Table')
        for i in records:
            print(i)
        self.close()

    def update(self):
        self.getter()
        locationId=int(input('Enter LocationId to be Updated: '))
        self.locationName=input('Enter Location Name:')
        self.address=input('Enter Address:')

        update_str='''
            UPDATE Location
            SET LocationName=%s,Address=%s
            WHERE LocationId=%s
        '''

        self.open()
        data=[(self.locationName,self.address,locationId)]
        self.s.executemany(update_str,data)
        self.conn.commit()
        print('Record updated successfully..')
        self.close()
        return True

    def delete(self):
        locationId=int(input('Enter the LocationId to be deleted:'))
        delete_str=f'DELETE FROM Location WHERE LocationId={locationId}'
        self.open()
        self.s.execute(delete_str)
        self.conn.commit()
        print('Record Deleted Successfully..')
        self.close()

