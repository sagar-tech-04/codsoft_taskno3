import random 

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%&*_-+/=()"

length = int(input("How long should Password be: "))

def generaterandompw():
    password = ''

    for i in range(length):
        password += random.choice(characters)
    return password

password = generaterandompw()
print("Password is:",password)
        
