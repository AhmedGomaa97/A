import re

def get_user_info():
    while True:
        try:
            name = input("Please enter your name: ")
            
            if not name.isalpha():
                raise ValueError("Wrong name. Please enter a valid name (only letters).")
            break  
        except ValueError as e:
            print(e)

    while True:
        try:
            email = input("Please enter your email address: ")
            email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            if not re.match(email_pattern, email):
                raise ValueError("Invalid email address. Please enter a valid email.")

            break  

        except ValueError as e:
            print(e)
    
    print("Name:", name)
    print("Email:", email)

get_user_info()
