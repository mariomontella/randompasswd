import random

print('Password Generator NetworkMario')

chars = 'abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ1234567890!?@#+-_'

number = input ('Quante password vuoi generare?')

number = int(number)

lenght = input('Quantità caratteri di password:')
lenght = int(lenght)

print('Queste sono le tue passwd:')

for pwd in range (number):
    passwords = ''
    for c in range(lenght):
        passwords += random.choice(chars)
    print(passwords)
