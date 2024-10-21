import re
from colors import *
from typing import Union
from collections.abc import Callable


class Account:

    Error_type = Union[
        str | Callable[[str], str]
    ]  # can be used as paramenter type in _get_valid_input, not in use right now.

    @staticmethod
    def _get_valid_input(prompt: str, validation_func, error_message) -> str:
        while True:
            user_input = input(prompt)
            if validation_func(user_input):
                return user_input
            else:
                if callable(error_message):
                    print(error_message(user_input))
                else:
                    print(error_message)

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
    def create_user(users: dict[int, dict[str, str]]) -> dict[str, str] | None:
        existing_user = False
        new_user: dict[str, str] = {}

        if not Account._create_new("user"):
            return None

        user_person_ID = Account._get_valid_input(
            "Insert user person ID: ",
            lambda x: x.isnumeric()
            and not any(users[user].get("person_ID") == x for user in users),
            f"{RED}Person ID must be numeric and unique, no letters or special characters allowed{RESET}",
        )

        user_name = Account._get_valid_input(
            "Insert user name: ",
            lambda x: x.replace(" ", "").isalpha(),
            f"{RED}Name must be aphabetic, no numbers os special characters allowed{RESET}",
        ).title()

        valid_user_birthday = Account._get_valid_input(
            "Insert user birthday(DD/MM/YYYY)",
            lambda x: Account._validate_birthday(x),
            f"{RED}Invalid birthday format, must be DD/MM/YYYY{RESET}",
        )

        print("=" * 10, f"{BLUE}Insert user address{RESET}", "=" * 10)

        user_address_street = Account._get_valid_input(
            "Insert street: ",
            lambda x: x.strip() != "" and x.replace(" ", "").isalpha(),
            lambda x: f"{RED}Street name {'cannot be empty' if x.strip() == '' else 'must only contain letters and spaces'}{RESET}",
        ).title()

        user_address_number = Account._get_valid_input(
            "Insert residence number: ",
            lambda x: x.strip() != "" and x.isnumeric(),
            lambda x: f"{RED}Residence number {'cannot be empty' if x.strip() == '' else 'must be numeric'}{RESET}",
        )

        user_address_neighborhood = Account._get_valid_input(
            "Insert neighborhood: ",
            lambda x: x.strip() != "" and x.replace(" ", "").isalpha(),
            lambda x: f"{RED}Neighborhood name {'cannot be empty' if x.strip() == '' else 'must only contain letters and spaces'}{RESET}",
        ).title()

        user_address_city = Account._get_valid_input(
            "Insert city: ",
            lambda x: x.strip() != "" and x.replace(" ", "").isalpha(),
            lambda x: f"{RED}City name {'cannot be empty' if x.strip() == '' else 'must only contain letters and spaces'}{RESET}",
        ).title()

        user_address_state_acronym = Account._get_valid_input(
            "Insert state acronym: ",
            lambda x: len(x) == 2 and x.isalpha(),
            f"{RED}Acronym must have exact two letters{RESET}",
        ).upper()

        user_address = f"{user_address_street}, {user_address_number} - {user_address_neighborhood} - {user_address_city}/{user_address_state_acronym}"

        if not existing_user:
            new_user = {
                "name": user_name,
                "birthday": valid_user_birthday,
                "person_ID": user_person_ID,
                "address": user_address,
            }
            print(f"Your user {BLUE}{new_user.get('name')}{RESET} was created successfully")
            return new_user

    @staticmethod
    def create_account(
        users: dict[int, dict[str, str]],
        account_counter: int,
    ) -> dict[str, str] | None:
        new_account: dict[str, str] = {}

        if not Account._create_new("account"):
            return None

        user_input_ID = Account._get_valid_input(
            "Insert user personID: ",
            lambda x: len(x) >= 4 and x.isnumeric(),
            lambda x: f"{RED}Invalid input. {'Person_ID must be at least 4 digits long' if len(x) < 4 else 'Please enter a numeric value for the person ID!'} {RESET}",
        )

        while True:
            for _, value in users.items():
                try:
                    if value.get("person_ID") == user_input_ID:
                        option = input(
                            f"User {BLUE}{value.get('name')}{RESET} with person ID {YELLOW}{user_input_ID}{RESET} was found, create account [Y/N]: "
                        )
                        if option.lower() == "y":
                            account_counter += 1
                            new_account = {
                                "agency": "0001",
                                "account_number": str(account_counter),
                                "user": user_input_ID,
                            }
                            print(
                                f"Creating new account {YELLOW}{account_counter}{RESET} for user {BLUE}{value.get('name')}{RESET}..."
                            )
                            return new_account
                        elif option.lower() == "n":
                            print("Exiting without creating new account...")
                            return
                        else:
                            print("Invalid input. Please enter Y or N.")
                except KeyError:
                    print("Some random error")
            print(
                f"{RED}User not found, please became a client before opening an account{RESET}"
            )  # test this
            break

    @staticmethod
    def list_users(users: dict[int, dict[str, str]]):
        if users:
            print(f"There are {len(users)} users registered!")
            for user in users:
                print("=" * 70)
                print(f"Name: {BLUE}{users[user].get('name')}{RESET}")
                print(f"Birthday: {BLUE}{users[user].get('birthday')}{RESET}")
                print(f"Person_ID: {BLUE}{users[user].get('person_ID')}{RESET}")
                print(f"Address: {BLUE}{users[user].get('address')}{RESET}")
        else:
            print("Theres no Users created!")

    @staticmethod
    def list_accounts(users: dict[int, dict[str, str]], accounts: dict[int, dict[str, str]]):
        account_owners: dict[str | None, list[str | None]] = {}
        print(f"There are {YELLOW}{len(accounts)}{RESET} accounts created")

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
            print(f"User {BLUE}{name}{RESET} owns:")
            for account_number in account_numbers:
                print(f"Account {BRIGHT_GREEN}{account_number}{RESET}")
