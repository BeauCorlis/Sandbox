

MINIMUM_PASSWORD_LENGTH = 4

"""Request password with valid length"""
password = input("Enter password of at least {} characters: ".format(MINIMUM_PASSWORD_LENGTH))
while len(password) < MINIMUM_PASSWORD_LENGTH:
    password = input("Enter password of at least {} characters: ".format(MINIMUM_PASSWORD_LENGTH))

print('*' * len(password))
