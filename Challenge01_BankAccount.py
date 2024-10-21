import datetime as dt
from CreateUserAndAccount import Account as cua
from colors import *

# These Types are just for testing global behaviour
Balance = float
Transaction = dict[str, float | dt.datetime]
Balance_and_Transaction = tuple[Balance, Transaction]
transactions_counter = 7


def transactions_record() -> bool:
    global transactions_counter
    DAILY_TRANSACTION_LIMIT = 10
    today = dt.date.today()

    transactions_counter += 1
    if today and transactions_counter > DAILY_TRANSACTION_LIMIT:
        print(f"{RED}Exceeded daily transaction limit of 10{RESET}")
        return False
    else:
        return True


def deposit_handler(balance: float) -> Balance_and_Transaction:
    new_transactions: dict[str, float | dt.datetime] = {}
    try:
        deposit = float(input("Enter the amount to deposit: "))
        if deposit < 1:
            print(f"{YELLOW}Deposit must be greater than 0{RESET}")
        else:
            date = dt.datetime.now()
            willRecord = transactions_record()
            if willRecord:
                balance += deposit
                new_transactions = {"amount": deposit, "date": date}
                print(f"Deposited: R$ {GREEN}{deposit}{RESET}")
        return (balance, new_transactions)
    except ValueError:
        print(f"{YELLOW}Deposit must be a number{RESET}")
        return (balance, new_transactions)


def withdraw_handler(balance: float) -> Balance_and_Transaction:
    new_transactions: dict[str, float | dt.datetime] = {}
    try:
        withdraw = float(input("Enter the amount to withdraw: "))
        if withdraw < 1:
            print(f"{YELLOW}Withdraw must be greater than 0{RESET}")
        else:
            if withdraw > 500:
                print(f"{GREEN}Withdraw limit exceeded{RESET}")
            elif withdraw > balance:
                print(f"{GREEN}Balance is insufficient{RESET}")
            else:
                date = dt.datetime.now()
                willRecord = transactions_record()
                if willRecord:
                    balance -= withdraw
                    new_transactions = {"amount": -(withdraw), "date": date}
                    print(f"Withdrawn: R$ {RED}{withdraw}{RESET}")
        return (balance, new_transactions)
    except ValueError:
        print(f"{YELLOW}Withdraw must be a number{RESET}")
        return (balance, new_transactions)


def balance_handler(
    balance: float, transactions: dict[int, dict[str, float | dt.datetime]]
) -> float:
    for transaction in transactions.values():
        amount = transaction.get("amount")
        if amount is None:
            continue

        date = transaction["date"]
        if isinstance(amount, float) and amount > 0:
            if isinstance(date, dt.datetime):
                print(
                    f"R$ {BRIGHT_GREEN}{transaction['amount']:10.2f}{RESET} : {date.strftime('%d/%m/%Y %H:%M:%S')}"
                )
        elif isinstance(amount, float) and amount < 0:
            if isinstance(date, dt.datetime):
                print(
                    f"R$ {BRIGHT_RED}{transaction['amount']:10.2f}{RESET} : {date.strftime('%d/%m/%Y %H:%M:%S')}"
                )

    print(f"Balance: R$ {BRIGHT_BLUE}{balance:.2f}{RESET}\n")
    return balance


# NOTE - Main program


def main():
    menu = f"""
        Choose an option: 
        [{GREEN}D{RESET}]eposit
        [{GREEN}W{RESET}]ithdraw
        [{GREEN}B{RESET}]alance
        [{GREEN}CA{RESET}]create account
        [{GREEN}CU{RESET}]create user
        [{GREEN}LA{RESET}]ist accounts
        [{GREEN}LU{RESET}]list users
        [{RED}Q{RESET}]uit
    """

    balance = 0
    transactions: dict[int, dict[str, float | dt.datetime]] = {}

    users: dict[int, dict[str, str]] = {}
    accounts: dict[int, dict[str, str]] = {}
    user_counter = 0
    account_counter = 0

    while True:
        print("=" * 70)
        option = input(f"{menu}\n-> ")
        if option.lower() == "d":
            balance, new_transaction = deposit_handler(balance)
            trans_number = len(transactions) + 1
            transactions[trans_number] = new_transaction

        elif option.lower() == "w":
            balance, new_transaction = withdraw_handler(balance)
            trans_number = len(transactions) + 1
            transactions[trans_number] = new_transaction

        elif option.lower() == "b":
            print("=" * 70)
            print("Transactions:")
            balance = balance_handler(balance, transactions)

        elif option.lower() == "ca":
            new_account = cua.create_account(users, account_counter)
            if new_account is not None:
                account_counter += 1
                accounts[account_counter] = new_account

        elif option.lower() == "cu":
            new_users = cua.create_user(users)
            if new_users is not None:
                user_counter += 1
                users[user_counter] = new_users

        elif option.lower() == "la":
            cua.list_accounts(users, accounts)

        elif option.lower() == "lu":
            cua.list_users(users)

        elif option.lower() == "q":
            print(f"{BRIGHT_CYAN}Service terminated. \nHave a nice day.{RESET}")
            break

        else:
            print(f"{BOLD_RED_ON_YELLOW}!!!Invalid Option!!!{RESET}")


main()
