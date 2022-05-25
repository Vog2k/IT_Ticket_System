import random

problems = ['Lost_ID_card', 'Misplaced laptop, ']

Storage = open("Stored", "r")


def Start_up():
    welcome = print("Welcome")


def sign_Up():
    first_name = input("Please enter first name: ")
    last_name = input("Please enter last name: ")
    first_char = [0]
    last_char = [0]
    ID = (first_char + last_char, random.randint(1, 100))

    if first_name != input():
        print("Please try again ...")
        sign_Up()
    else:
        if len(first_name) <= 2:
            print("First name is too short")
            sign_Up()


def generate_identification():
    pass


def Login():
    id_card = input()
if id_card == 'Random id':
    print("Welcome" + fis)


"""def login(first_name, last_name, first_char, last_char, ID):
    first_name = input("Please enter first name: ")
    last_name = input("Please enter last name: ")
    first_char = [0]
    last_char = [0]
    print(first_char + last_char, random.randint(1, 100))


# Free phone 08008 38383

def main():
    login()"""
