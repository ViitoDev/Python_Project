import random
 
def create_password():
    capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    specials = "!@#$%&*"
 
    password = [
        random.choice(capital),
        random.choice(lowercase),
        random.choice(numbers),     
        random.choice(specials)    
    ]
 
    all_characteres = capital + lowercase + numbers + specials
    password.extend(random.choices(all_characteres, k=8))
    random.shuffle(password)
    return ''.join(password)
 
print(f"Password created: {create_password()}")
