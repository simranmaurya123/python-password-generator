
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits 
    password = "".join(random.choice(characters) for i in range(length))
    return password

while True:
    permission = input("To generate a password type yes: ").strip().lower()
    if permission == "yes":
        password_length = 8
        password = generate_password(password_length)
        print("Generated password:", password)
        break
    else:
        print("Invalid input. Please type 'yes' to generate a password.")






    



    

