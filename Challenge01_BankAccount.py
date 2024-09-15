import datetime as dt
from typing import Dict, Union

balance = 0
counter = 0
DAILY_TRANSACTION_LIMIT = 10
transactions: Dict[int, Dict[str, Union[str, float | dt.datetime]]] = {}


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


while True:
    print("=================================")
    option = input("Choose an option: [D]eposit, [W]ithdraw, [B]alance, [Q]uit \n: ")
    if option.lower() == "d":
        balance = deposit_handler(balance)

    elif option.lower() == "w":
        balance = withdraw_handler(balance)

    elif option.lower() == "b":
        balance = balance_handler(balance)

    elif option.lower() == "q":
        print("\33[96mService terminated. \nHave a nice day.\33[0m")
        break
    else:
        print("\033[31m!!!Invalid Option!!!\033[0m")
