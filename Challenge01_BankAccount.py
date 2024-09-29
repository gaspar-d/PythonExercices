import datetime as dt
import CreateUserAndAccount as cua

menu = """
Choose an option: 
[\033[32mD\033[0m]eposit
[\033[32mW\033[0m]ithdraw
[\033[32mB\033[0m]alance
[\033[32mCA\033[0m]create account
[\033[32mCU\033[0m]create user
[\033[32mLA\033[0m]ist accounts
[\033[32mLU\033[0m]list users
[\033[31mQ\033[0m]uit
"""

balance = 0
counter = 0
DAILY_TRANSACTION_LIMIT = 10
transactions: dict[int, dict[str, float | dt.datetime]] = {}


def transactions_record(option: str, amount: float, date: dt.datetime) -> bool:
    global counter
    counter += 1
    today = dt.date.today()
    if option.lower() == "d":
        if today and counter > DAILY_TRANSACTION_LIMIT:
            print("\033[31mExceeded daily transaction limit of 10\033[0m")
            return False
        else:
            transactions[counter] = {"amount": amount, "date": date}
            return True
    elif option.lower() == "w":
        if today and counter > DAILY_TRANSACTION_LIMIT:
            print("\033[31mExceeded daily transaction limit of 10\033[0m")
            return False
        else:
            transactions[counter] = {"amount": -(amount), "date": date}
            return True
    else:
        return False


def deposit_handler(balance: float) -> float:
    try:
        deposit = float(input("Enter the amount to deposit: "))
        if deposit < 1:
            print("\033[33mDeposit must be greater than 0\033[0m")
        else:
            date = dt.datetime.now()
            if transactions_record("d", deposit, date):
                balance += deposit
                print(f"Deposited: R$ \033[32m{deposit}\033[0m")
        return balance
    except ValueError:
        print("\033[33mDeposit must be a number\033[0m")
        return balance


def withdraw_handler(balance: float) -> float:
    try:
        withdraw = float(input("Enter the amount to withdraw: "))
        if withdraw < 1:
            print("\033[33mWithdraw must be greater than 0\033[0m")
        else:
            if withdraw > 500:
                print("\033[32mWithdraw limit exceeded\033[0m")
            elif withdraw > balance:
                print("\033[32mBalance is insufficient\033[0m")
            else:
                date = dt.datetime.now()
                if transactions_record("w", withdraw, date):
                    balance -= withdraw
                    print(f"Withdrawn: R$ \033[31m{withdraw}\033[0m")
        return balance
    except ValueError:
        print("\033[33mWithdraw must be a number\033[0m")
        return balance


def balance_handler(balance: float) -> float:
    for transaction in transactions.values():
        amount = transaction["amount"]
        date = transaction["date"]
        if isinstance(amount, float) and amount > 0:
            if isinstance(date, dt.datetime):
                print(
                    f"R$ \033[92m{transaction['amount']:10.2f}\033[0m : {date.strftime('%d/%m/%Y %H:%M:%S')}"
                )
        elif isinstance(amount, float) and amount < 0:
            if isinstance(date, dt.datetime):
                print(
                    f"R$ \033[91m{transaction['amount']:10.2f}\033[0m : {date.strftime('%d/%m/%Y %H:%M:%S')}"
                )

    print(f"Balance: R$ \033[94m{balance:.2f}\033[0m\n")
    return balance


# NOTE - Main program


def main():
    global balance
    while True:
        print("=" * 70)
        option = input(f"{menu}\n-> ")
        if option.lower() == "d":
            balance = deposit_handler(balance)

        elif option.lower() == "w":
            balance = withdraw_handler(balance)

        elif option.lower() == "b":
            print("=" * 70)
            print("Transactions:")
            balance = balance_handler(balance)

        elif option.lower() == "ca":
            cua.create_account()

        elif option.lower() == "cu":
            cua.create_user()

        elif option.lower() == "la":
            cua.list_accounts()

        elif option.lower() == "lu":
            cua.list_users()

        elif option.lower() == "q":
            print("\33[96mService terminated. \nHave a nice day.\33[0m")
            break

        else:
            print("\033[1;31;43m!!!Invalid Option!!!\033[0m")


# NOTE - Calling main
main()
