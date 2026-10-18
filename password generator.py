import random
print("Welcome to random password generator")
randomchars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()?"
num=int(input("Enter number of passwords to generate:"))
length=int(input("Enter length of password"))
print("Here are your random password")
for i in range(num):
    pws=" "
    for a in range(length):
        pws=pws+random.choice(randomchars)
    print(pws)
