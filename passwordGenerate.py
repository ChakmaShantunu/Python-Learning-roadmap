import random
import string

length = int(input("Enter password length: "))

charecters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(charecters) for i in range(length))


print("Generated Password: ", password)    