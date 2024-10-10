import re


class Account:
    @staticmethod
    def _validate_birthday(date_str: str):
        pattern = r"^(\d{2})[\/\-]?(\d{2})[\/\-]?(\d{4})$"
        match = re.match(pattern, date_str)
        if not match:
            return ""

        day, month, year = match.groups()

        return f"{day}{month}{year}"

    @staticmethod
    def _create_new(element: str) -> bool:
        while True:
            should_create_new = input(f"Create new {element}? [Y/N]: ").lower()
            if should_create_new == "y":
                return True
            elif should_create_new == "n":
                print(f"Exiting without creating new {element}...")
                return False
            else:
                print("Invalid input. Please enter Y or N.")

    @staticmethod
    def create_user(
        users: dict[int, dict[str, str]], user_counter: int
    ) -> dict[str, str] | None:
        existing_user = False
        new_user: dict[str, str] = {}

        if not Account._create_new("user"):
            return None

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
            if Account._validate_birthday(user_birthday):
                valid_user_birthday = Account._validate_birthday(user_birthday)
                break
            else:
                print(
                    "\033[31mInvalid birthday format, must be DD/MM/YYYY\033[0m"
                )

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
            new_user = {
                "name": user_name,
                "birthday": valid_user_birthday,
                "person_ID": user_person_ID,
                "address": user_address,
            }
            print(f"Your user {new_user.get('name')} was created successfully")
            return new_user

    @staticmethod
    def create_account(
        users: dict[int, dict[str, str]],
        accounts: dict[int, dict[str, str]],
        account_counter: int,
    ) -> dict[str, str] | None:
        new_account: dict[str, str] = {}

        if not Account._create_new("account"):
            return None

        while True:
            user_input_ID = input("Insert user personID: ")
            if len(user_input_ID) >= 4 and user_input_ID.isnumeric():
                for _, value in users.items():
                    try:
                        if value.get("person_ID") == user_input_ID:
                            option = input(
                                f"User \033[34m{value.get('name')}\033[0m with person ID \033[33m{user_input_ID}\033[0m was found, create account [Y/N]: "
                            )
                            if option.lower() == "y":
                                account_counter += 1
                                new_account = {
                                    "agency": "0001",
                                    "account_number": str(account_counter),
                                    "user": user_input_ID,
                                }
                                print(
                                    f"Creating new account \033[33m{account_counter}\033[0m for user \033[34m{value.get('name')}\033[0m..."
                                )
                                return new_account
                            elif option.lower() == "n":
                                print(
                                    "Exiting without creating new account..."
                                )
                                return
                            else:
                                print("Invalid input. Please enter Y or N.")
                    except KeyError:
                        print("Some random error")
                print(
                    "\033[31mUser not found, please became a client before opening an account\033[0m"
                )  # test this
                break
            else:
                print(
                    "Invalid input. Please enter a numeric value for the person ID."
                )

    @staticmethod
    def list_users(users: dict[int, dict[str, str]]):
        if users:
            print(f"There are {len(users)} users registered!")
            for user in users:
                print("=" * 70)
                print(f"Name: \033[34m{users[user].get("name")}\033[0m")
                print(
                    f"Birthday: \033[34m{users[user].get("birthday")}\033[0m"
                )
                print(
                    f"Person_ID: \033[34m{users[user].get("person_ID")}\033[0m"
                )
                print(f"Address: \033[34m{users[user].get("address")}\033[0m")
        else:
            print("Theres no Users created!")

    @staticmethod
    def list_accounts(
        users: dict[int, dict[str, str]], accounts: dict[int, dict[str, str]]
    ):
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

        for name, account_numbers in account_owners.items():
            print(f"User \033[34m{name}\033[0m owns:")
            for account_number in account_numbers:
                print(f"Account \033[92m{account_number}\033[0m")
