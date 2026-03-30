import random
import string

charecters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(8): 
    password += random.choice(charecters)

print("Generated Password: ", password)    