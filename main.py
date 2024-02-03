import string
import random
print("your password will be saved in a txt called password mega doc")
name = input("what is this password for")
open_file = open('password mega doc', 'a')

def pw_gen(size = int(input("lenght")), chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

password=str(pw_gen())


open_file.write("\SPACER\SPACER" + name + password)
open_file.close()
