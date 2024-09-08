import random
import string

def generate(x):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    gen_pass =  ''.join(random.choice(characters) for _ in range(x))
    
    return gen_pass

length = int(input("Enter the length of the password : "))
print(f"The password : {generate(length)}")

