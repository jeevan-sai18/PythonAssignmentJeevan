class TrackingNumberNotFoundException(Exception):
    def __init__(self,message="Tracking number not found"):
        self.message=message
        super().__init__(self.message)

class User:
    def __init__(self,user_id,name,email,password,contact_number,address):
        self.UserID=user_id
        self.Name=name
        self.Email=email
        self.Password=password
        self.ContactNumber=contact_number
        self.Address=address

def withdraw_amount(user,amount,target_email):
    try:
        if user.Email!=target_email:
            raise TrackingNumberNotFoundException("Withdrawal not allowed: Different email address")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        print("Withdrawal successful")
user1 = User(1,"jeevan","jeevan@email.com","password1","1234567890","Main St")
withdraw_amount(user1,50,"jeevan@email.com")
withdraw_amount(user1,50,"different@example.com")