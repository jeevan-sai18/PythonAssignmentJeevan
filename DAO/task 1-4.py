#1. Write a program that checks whether a given order is delivered or not based on its status (e.g.,
#"Processing," "Delivered," "Cancelled"). Use if-else statements for this.

order_status=input("Enter the order status: ")

if order_status=="Delivered":
  print("The order has been delivered.")
elif order_status=="Processing":
  print("The order is still being processed.")
elif order_status=="Cancelled":
  print("The order has been cancelled.")
else:
  print("Invalid order status.")

#2.Implement a switch-case statement to categorize parcels based on their weight into "Light,"
#"Medium," or "Heavy."
weight=float(input("Enter the weight of the parcel (kg): "))

if weight<=0.5:
    category="Light"
elif weight<=2:
    category="Medium"
else:
    category="Heavy"

print(f"The parcel is categorized as {category}.")


#3.Implement User Authentication 1. Create a login system for employees and customers using Java
#control flow statements.
user_credentials={
    'employee1': 'employee_password1',
    'customer1': 'customer_password1'
}

def login():
    max_attempts=3
    attempts=0

    while attempts<max_attempts:
        username=input("Enter username: ")
        password=input("Enter password: ")

        if username in user_credentials and user_credentials[username]==password:
            print("Login successful!")
            break
        else:
            print("Invalid username or password. Please try again.")
            attempts+=1

    if attempts==max_attempts:
        print("Too many login attempts. Please try again later.")

login()


#4.Implement Courier Assignment Logic 1. Develop a mechanism to assign couriers to shipments based
#on predefined criteria (e.g., proximity, load capacity) using loops.
#  we will here define a list of available couriers and their capacities (dictionary)
couriers=[
    {"name": "Emma Davis", "capacity": 5.0},
    {"name": "William Brown", "capacity": 4.0}]
shipments=[
    {"sender": "John Doe", "receiver": "Jane Smith", "weight": 2.5},
    {"sender": "Alice Johnson", "receiver": "Bob Anderson", "weight": 1.8}]

for shipment in shipments:
    assigned=False
    for courier in couriers:
        if courier["capacity"] >= shipment["weight"]:
            print(f"Courier '{courier['name']}' assigned to deliver from {shipment['sender']} to {shipment['receiver']}")
            courier["capacity"]-=shipment["weight"]
            assigned=True
            break

    if not assigned:
        print(f"No available courier for the shipment from {shipment['sender']} to {shipment['receiver']}")


#W5.rite a Python program that uses a for loop to display all the orders for a specific customer.
orders = [
    {"order_id": 1, "customer_name": "John Doe", "product": "Product A"},
    {"order_id": 2, "customer_name": "Jane Smith", "product": "Product B"},
    {"order_id": 3, "customer_name": "John Doe", "product": "Product C"},
    {"order_id": 4, "customer_name": "Alice Johnson", "product": "Product D"},
    {"order_id": 5, "customer_name": "John Doe", "product": "Product E"}]

customer_to_display="John Doe"
print(f"Orders for customer '{customer_to_display}':")
for order in orders:
    if order["customer_name"]==customer_to_display:
        print(f"Order ID: {order['order_id']}, Product: {order['product']}")


#6.Implement a while loop to track the real-time location of a courier until it reaches its destination.
import time
courier_location="Main Office"
destination="Branch Office"
while courier_location!=destination:
    print(f"Courier is currently at: {courier_location}")
    courier_location=destination
print(f"The courier has reached the destination: {destination}")


#9.Create a program that allows users to input a parcel tracking number.Store the
#tracking number and Status in 2d String Array. Initialize the array with values. Then, simulate the
#tracking process by displaying messages like "Parcel in transit," "Parcel out for delivery," or "Parcel
#delivered" based on the tracking number's status.

class CourierTrackingSystem:
    def __init__(self):
        self.tracking_data=[
            ['TRK123','In Transit'],
            ['TRK456','Delivered'],
            ['TRK789','Pending'],
            ['TRK987','In Transit'],
            ['TRK654','Delivered']
        ]

    def track_parcel(self, tracking_number):
        for data in self.tracking_data:
            if data[0]==tracking_number:
                return data[1]
        return None

    def display_status(self, status):
        if status=='In Transit':
            print("Parcel is in transit.")
        elif status=='Pending':
            print("Parcel is pending.")
        elif status=='Delivered':
            print("Parcel has been delivered.")
        else:
            print("Invalid tracking number.")

    def run(self):
        while True:
            tracking_number=input("Enter tracking number (or 'quit' to exit): ")
            if tracking_number.lower()=='quit':
                break

            status=self.track_parcel(tracking_number)
            if status is not None:
                self.display_status(status)
            else:
                print("Tracking number not found.")

if __name__ == "__main__":
    tracking_system = CourierTrackingSystem()
    tracking_system.run()



#11. Develop a function that takes an address as input (street, city, state, zip code) and formats it correctly, including capitalizing the first letter of each word and properly formatting the zip code.
def format_address(street,city,state,zip_code):
    formatted_street=' '.join(word.capitalize() for word in street.split())
    formatted_city=city.capitalize()
    formatted_state=state.upper()

    formatted_zip=str(zip_code)
    if len(formatted_zip)>5:
        formatted_zip=formatted_zip[:5] + '-' + formatted_zip[5:]

    formatted_address=f"{formatted_street}, {formatted_city}, {formatted_state} {formatted_zip}"
    return formatted_address

street_address="123 example street"
city_name="city"
state_name="state"
zip_code="123456789"

formatted_result=format_address(street_address, city_name, state_name, zip_code)
print(formatted_result)


#13. Develop a function that calculates the shipping cost based on the distance
#between two locations and the weight of the parcel. You can use string inputs for the source and
#destination addresses.

def calculate_shipping_cost(source_address,destination_address,weight):
    distances={
        ('123 Main St, City, Country', '456 Oak Ave, Town, Country'): 30,
        ('789 Elm St, Village, Country', '101 Pine St, City, Country'): 50,
        ('222 Cedar Ave, Town, Country', '123 Main St, City, Country'): 20,
        ('456 Oak Ave, Town, Country', '789 Elm St, Village, Country'): 40,
        ('101 Pine St, City, Country', '222 Cedar Ave, Town, Country'): 25
    }

    try:
        if (source_address, destination_address) in distances:
            distance=distances[(source_address, destination_address)]
        else:
            return "Distance not available for the given addresses."

        cost_per_mile = 0.5
        shipping_cost=distance * cost_per_mile + (weight * 2)

        return shipping_cost

    except Exception as e:
        return f"An error occurred: {str(e)}"

source_address='123 Main St, City, Country'
destination_address='456 Oak Ave, Town, Country'
parcel_weight=5.2

estimated_cost=calculate_shipping_cost(source_address, destination_address, parcel_weight)

if isinstance(estimated_cost, (int, float)):
    print(f"The estimated shipping cost is: ${estimated_cost:.2f}")
else:
    print(estimated_cost)



#14. Create a function that generates secure passwords for courier system accounts. Ensure the passwords contain a mix of uppercase letters, lowercase letters, numbers, and special characters.

import random
import string

def generate_secure_password(length=12):
    uppercase_letters=string.ascii_uppercase
    lowercase_letters=string.ascii_lowercase
    numbers=string.digits
    special_characters=string.punctuation
    all_characters=uppercase_letters+lowercase_letters+numbers+special_characters

    password=random.choice(uppercase_letters)
    password+=random.choice(lowercase_letters)
    password+=random.choice(numbers)
    password+=random.choice(special_characters)

    password+=''.join(random.choice(all_characters) for _ in range(length - 4))

    password_list=list(password)
    random.shuffle(password_list)
    password=''.join(password_list)

    return password

generated_password=generate_secure_password()
print("Generated Password:",generated_password)
