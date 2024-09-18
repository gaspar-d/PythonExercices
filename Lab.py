# Lab to test code before put it in production
# remember to copy global variables to code base

import re

users: dict[int, dict[str, str]] = {}
accounts: dict[int, dict[str, str | None]] = {}
user_counter = 0


def validate_birthday(date_str: str):
    pattern = r"^(\d{2})[\/\-]?(\d{2})[\/\-]?(\d{4})$"

    match = re.match(pattern, date_str)
    if not match:
        return ""

    day, month, year = match.groups()

    return f"{day}{month}{year}"


def create_user():
    global users, user_counter
    existing_user = False

    while True:
        should_create_new_user = input("Create new user? [Y/N]: ").lower()
        if should_create_new_user == "y":
            break
        elif should_create_new_user == "n":
            print("Exiting without creating new user...")
            return
        else:
            print("Invalid input. Please enter Y or N.")

    while True:
        user_person_ID = input("Insert user person ID: ")
        if user_person_ID.isnumeric():
            for user in users:
                if users[user].get("person_ID") == user_person_ID:
                    print(f"User {user} already exists")
                    existing_user = True
                    break
            break
        else:
            print(
                "\033[31mPerson ID must be numeric, no letters or special characters allowed\033[0m"
            )

    while True:
        user_name = input("Insert user name: ").title()
        if user_name.isalpha():
            break
        else:
            print(
                "\033[31mName must be alphabetic, no numbers or special characters allowed\033[0m"
            )

    while True:
        user_birthday = input("Insert user birthday(DD/MM/YYYY): ")
        if validate_birthday(user_birthday):
            valid_user_birthday = validate_birthday(user_birthday)
            break
        else:
            print("\033[31mInvalid birthday format, must be DD/MM/YYYY\033[0m")

    while True:
        print("Insert user address: ")
        user_address_street = input("Insert street: ")
        user_address_number = input("Insert number: ")
        user_address_neighborhood = input("Insert neighborhood: ")
        user_address_city = input("Insert city: ")
        user_address_state_acronym = input("Insert state acronym: ")

        user_address = f"{user_address_street}, {user_address_number} - {user_address_neighborhood} - {user_address_city}/{user_address_state_acronym}".title()

        if user_address != "":
            break
        else:
            print(
                "\033[31mAddress must be alphabetic, no numbers or special characters allowed\033[0m"
            )

    if not existing_user:
        user_counter += 1
        users[user_counter] = {
            "name": user_name,
            "birthday": valid_user_birthday,
            "person_ID": user_person_ID,
            "address": user_address,
        }
        print(f"Your user {users[user_counter].get('name')} was created successfully")


def create_account():
    while True:
        create_acc = input("Create new account? [Y/N]: ").lower()
        if create_acc == "y":
            break
        elif create_acc == "n":
            print("Exiting without creating new account...")
            return
        else:
            print("Invalid input. Please enter Y or N.")

    while True:
        for_user = input("Insert user person ID: ")
        if for_user == "":
            print("Person ID cannot be empty")
            return

        elif for_user.isnumeric():
            for user in users:
                if users[user].get("person_ID") == for_user:
                    print(
                        f"user with person ID {for_user} was found, create account [Y/N]: "
                    )
                    if input().lower() == "y":
                        break
                    else:
                        print("Exiting without creating new account...")
                        return
            break
        else:
            print("Invalid input. Please enter a numeric value for the person ID.")

    print("Creating new account...")

    # agency: str = "0001" # always 0001
    # account_number: str # sequential starting on 1
    # user = users[1].get("person_ID") # use person_ID as user because it's unique


# create_user()

users = {
    1: {
        "name": "John",
        "birthday": "01/01/2000",
        "person_ID": "123",
        "address": "123 Main St",
    },
    2: {
        "name": "Jane",
        "birthday": "02/02/2000",
        "person_ID": "456",
        "address": "456 Main St",
    },
}

accounts = {
    1: {
        "agency": "0001",
        "account_number": "1",
        "user": users[1].get("person_ID"),
    },
    2: {
        "agency": "0001",
        "account_number": "2",
        "user": users[2].get("person_ID"),
    },
}
print(users)
print(accounts)

create_account()
