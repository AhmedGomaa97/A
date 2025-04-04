def get_user_info():
    while True:
        name = input("Please enter your name: ")
        if name and name.isalpha():
            break
        else:
            print("Invalid name. Please enter a valid name .")

    while True:
        email = input("Please enter your email address: ")
        if "@" in email and "." in email:  
            username, domain = email.split("@")
            if username and domain :
               x, y = domain.split(".")
               if x and y :
                 break
        else:
            print("Invalid email address. Please enter a valid email.")

        print("Name:", name)
    print("Email:", email)

get_user_info()    
