from curses import init_pair
from ntpath import join
import string #import libraries required
import random

#put all the characters allowed in one place as a list
char_allowed = list(string.ascii_letters + string.digits + "!@#$%^&*()")

#ask user how many characters do they want in their password
pass_length = int(input("How long do you want your password to be?"))
#setup a dictionary to collect characters
password = []
#loop to add characters
for i in range(pass_length):
    password.append(random.choice(char_allowed))
    
random.shuffle(password)
print("".join(password))


