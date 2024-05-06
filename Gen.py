# In todays world of cyber threats, we all need quality passwords to ensure our data is secure. I recently have been studying CompTIA Security+ and I realized I
# needed to brush up on my python skills. So I am mixing cybersecurity with python with pratical application :)

import time
import random
import string

def introduction():
    print("Welcome to Password Generator!")
    time.sleep(0.5)
    print("In today's world, you need complex passwords that secure your accounts and systems.")
    time.sleep(1)
    print("According to NIST, you need a password atleast 8 characters in length and it needs complexity. However, the more characters, the better!")
    time.sleep(1)

def generate(length):
    a = ""
    b = ['!','@','#','$','%']
    for i in range(length):
        r = random.randint(1, 6)
        if r == 1:
            a += str(random.randint(1, 9))
        elif r == 2:
            a += random.choice(b)
        else:
            a += random.choice(string.ascii_letters) 
    return a

def askUser():
    while True:
        passlen = input("How long would you like your password?")
        try:
            passlen_int = int(passlen)
            print("Your password:", generate(passlen_int))
        except ValueError:
            print("Enter only integers, no characters or symbols. Run again.")
        break

introduction()
askUser()