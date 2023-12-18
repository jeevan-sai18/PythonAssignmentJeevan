# I can insert all values through main function by creating object for ENTITY

# Now I retrieve Variables and values

from DAO.Courier import *
obj1=Courier()
obj1.getter()
#obj1.setter()
#obj1.update()
#obj1.delete()
print("............................")

from DAO.CourierCompany import *
obj2=CourierCompany()
obj2.getter()
#obj2.setter()
#obj2.update()
#obj2.delete()

print(".................................")

from DAO.CourierService import *
obj3=CourierService()
obj3.getter()
#obj3.setter()
#obj3.update()
#obj3.delete()

print(".....................................")

from DAO.Employee import *

obj4=Employee()
obj4.getter()
#obj4.setter()
#obj4.update()
#obj4.delete()

print(".......................")

from DAO.Location import *

obj5=Location()
obj5.getter()
#obj5.setter()
#obj5.update()
#obj5.delete()

print(".........................")

from DAO.Payment import *

obj6=Payment()
obj6.getter()
#obj6.setter()
#obj6.update()
#obj6.delete()

print("...........................")

from DAO.User import *

obj7=User()
obj7.getter()
#obj7.setter()
#obj7.update()
#obj7.delete()

print("..............................")


from EXCEPTION.InvalidEmployeeIdException import *

obj8=EmployeeException()
obj8.RaiseException()
print(".........................")

from EXCEPTION.TrackingNumberNotFoundException import *

withdraw_amount(user1,50,"jeevan@email.com")