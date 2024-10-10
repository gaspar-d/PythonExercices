import datetime as dt
from CreateUserAndAccount import Account as cua

Balance = float
Transaction = dict[str, float | dt.datetime]
Balance_and_Transaction = tuple[Balance, Transaction]


def transactions_record(
    option: str,
    amount: float,
    date: dt.datetime,
) -> bool:
    counter = 0
    DAILY_TRANSACTION_LIMIT = 10

    counter += 1
    today = dt.date.today()
    if option.lower() == "d":
        if today and counter > DAILY_TRANSACTION_LIMIT:
            print("\033[31mExceeded daily transaction limit of 10\033[0m")
            return False
        else:
            return True
    elif option.lower() == "w":
        if today and counter > DAILY_TRANSACTION_LIMIT:
            print("\033[31mExceeded daily transaction limit of 10\033[0m")
            return False
        else:
            return True
    else:
        return False


def deposit_handler(balance: float) -> Balance_and_Transaction:
    new_transactions: dict[str, float | dt.datetime] = {}
    try:
        deposit = float(input("Enter the amount to deposit: "))
        if deposit < 1:
            print("\033[33mDeposit must be greater than 0\033[0m")
        else:
            date = dt.datetime.now()
            willRecord = transactions_record("d", deposit, date)
            if willRecord:
                balance += deposit
                new_transactions = {"amount": deposit, "date": date}
                print(f"Deposited: R$ \033[32m{deposit}\033[0m")
        return (balance, new_transactions)
    except ValueError:
        print("\033[33mDeposit must be a number\033[0m")
        return (balance, new_transactions)


def withdraw_handler(balance: float) -> Balance_and_Transaction:
    new_transactions: dict[str, float | dt.datetime] = {}
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
                willRecord = transactions_record("w", withdraw, date)
                if willRecord:
                    balance -= withdraw
                    new_transactions = {"amount": -(withdraw), "date": date}
                    print(f"Withdrawn: R$ \033[31m{withdraw}\033[0m")
        return (balance, new_transactions)
    except ValueError:
        print("\033[33mWithdraw must be a number\033[0m")
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
    transactions: dict[int, dict[str, float | dt.datetime]] = {}

    # from CreateUserAccount class
    users: dict[int, dict[str, str]] = {}
    accounts: dict[int, dict[str, str]] = {}
    user_counter = 0
    account_counter = 0

    # global balance
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
            new_account = cua.create_account(users, accounts, account_counter)
            if new_account is not None:
                account_counter += 1
                accounts[account_counter] = new_account

        elif option.lower() == "cu":
            new_users = cua.create_user(users, user_counter)
            if new_users is not None:
                user_counter += 1
                users[user_counter] = new_users

        elif option.lower() == "la":
            cua.list_accounts(users, accounts)

        elif option.lower() == "lu":
            cua.list_users(users)

        elif option.lower() == "q":
            print("\33[96mService terminated. \nHave a nice day.\33[0m")
            break

        else:
            print("\033[1;31;43m!!!Invalid Option!!!\033[0m")


# NOTE - Calling main
main()
