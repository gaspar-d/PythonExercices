# Lab to test code before put it in production
# remember to copy global variables to code base

import re

users: dict[int, dict[str, str]] = {}
accounts: dict[int, dict[str, str | None]] = {}
user_counter = 0
account_counter = 0


# For testing and debugging
# users = {
#     1: {
#         "name": "John",
#         "birthday": "01/01/2000",
#         "person_ID": "1234",
#         "address": "123 Main St",
#     },
#     2: {
#         "name": "Jane",
#         "birthday": "02/02/2000",
#         "person_ID": "4567",
#         "address": "456 Main St",
#     },
# }

# accounts = {
#     1: {
#         "agency": "0001",
#         "account_number": "1",
#         "user": users[1].get("person_ID"),
#     },
#     2: {
#         "agency": "0001",
#         "account_number": "2",
#         "user": users[2].get("person_ID"),
#     },
# }


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
                    print(
                        f"User {users[user].get('name')} with person ID {user_person_ID} already exists"
                    )
                    existing_user = True
                    return
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
        # print(f"users list: {users}")  # debug


def create_account():
    global accounts, account_counter

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
        user_input_ID = input("Insert user personID: ")
        if len(user_input_ID) >= 4 and user_input_ID.isnumeric():
            for user in users:
                if users[user].get("person_ID") == user_input_ID:
                    option = input(
                        f"User \033[34m{users[user].get('name')}\033[0m with person ID \033[33m{user_input_ID}\033[0m was found, create account [Y/N]: "
                    )
                    if option.lower() == "y":
                        account_counter += 1
                        accounts[account_counter] = {
                            "agency": "0001",
                            "account_number": str(account_counter),
                            "user": users[user].get("person_ID"),
                        }

                        # print(f"accounts list: {accounts}")  # debug

                        print(
                            f"Creating new account \033[33m{account_counter}\033[0m for user \033[34m{users[user].get('name')}\033[0m..."
                        )
                        return
                    elif option.lower() == "n":
                        print("Exiting without creating new account...")
                        return
                    else:
                        print("Invalid input. Please enter Y or N.")
            print("\033[31mUser not found, please became a client before opening an account\033[0m")
            break
        else:
            print("Invalid input. Please enter a numeric value for the person ID.")


def list_users():
    if users:
        print(f"There are {len(users)} users registered!")
        for user in users:
            print("=" * 70)
            print(f"Name: \033[34m{users[user].get("name")}\033[0m")
            print(f"Birthday: \033[34m{users[user].get("birthday")}\033[0m")
            print(f"Person_ID: \033[34m{users[user].get("person_ID")}\033[0m")
            print(f"Address: \033[34m{users[user].get("address")}\033[0m")
    else:
        print("Theres no Users created!")


def list_accounts():
    account_owners: dict[str | None, list[str | None]] = {}
    print(f"There are \033[33m{len(accounts)}\033[0m accounts created")
    
    for user in users.values():
        for account in accounts.values():
            if user.get("person_ID") == account.get("user"):
                name = user.get("name")
                account_number = account.get("account_number")

                if name in account_owners:
                    account_owners[name].append(account_number)
                else:
                    account_owners[name] = [account_number]
                    
                # print(f"The account number {account.get("account_number")} belongs to user {user.get("name")}")
                # print(f"This is the new list: {account_owners}")
    
    for name, account_numbers in account_owners.items():
        print(f"User \033[34m{name}\033[0m owns:")
        for account_number in account_numbers:
            print(f"Account \033[92m{account_number}\033[0m")
