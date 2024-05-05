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
    for i in range(length):
        r = random.randint(1, 6)
        if r == 1:
            a += str(random.randint(1, 9))
        else:
            a += random.choice(string.ascii_letters) 
    print(a)
    

generate(15)