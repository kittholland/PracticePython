import random

def new_password(length=16):
    return ''.join([(chr(random.randint(32,126))) for i in range(0,length)])

length = int(input("How long should your password be? "))
print(new_password(length))