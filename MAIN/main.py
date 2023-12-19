from DAO.Courier import Courier
from DAO.CourierCompany import CourierCompany
from DAO.CourierService import CourierService
from DAO.Employee import Employee
from DAO.Location import Location
from DAO.Payment import Payment
from DAO.User import User

def main():
    while True:
        print("Select an option:")
        print("1. Courier")
        print("2. Courier Company")
        print("3. Courier Service")
        print("4. Employee")
        print("5. Location")
        print("6. Payment")
        print("7. User")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            obj = Courier()
        elif choice == '2':
            obj = CourierCompany()
        elif choice == '3':
            obj = CourierService()
        elif choice == '4':
            obj = Employee()
        elif choice == '5':
            obj = Location()
        elif choice == '6':
            obj = Payment()
        elif choice == '7':
            obj = User()

        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
            continue

        obj.getter()
        print("............................")
        operation_choice = input("Do you want to perform additional operations? (Y/N): ").upper()
        if operation_choice != 'Y':
            break

        print("Select an operation:")
        print("1. Setter")
        print("2. Update")
        print("3. Delete")
        operation = input("Enter your operation choice: ")

        if operation == '1':
            obj.setter()
        elif operation == '2':
            obj.update()
        elif operation == '3':
            obj.delete()
        else:
            print("Invalid operation choice. Returning to main menu.")

if __name__ == "__main__":
    main()
