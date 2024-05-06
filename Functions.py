import time
import random
import string

def introduction():
    print("Welcome to Password Generator!")
    time.wait(0.5)
    print("In today's world, you need complex passwords that secure your accounts and systems.")
    time.wait(1)
    print("According to NIST, you need a password atleast 8 characters in length and it needs complexity. However, the more characters, the better!")
    time.wait(1)

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

askUser()