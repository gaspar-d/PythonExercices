balance = 0
deposits = []
withdraws = []
DAILY_WITHDRAWAL_LIMIT = 3

while True:
    print("=================================")
    option = input("Choose an option: [D]eposit, [W]ithdraw, [B]alance, [Q]uit \n: ")
    if option.lower() == "d":
        try:
            deposit = float(input("Enter the amount to deposit: "))
            if deposit < 1:
                print("Deposit must be greater than 0")
            else:
                deposits.append(deposit)
                balance += deposit
                print(f"Deposited: R$ {deposit}")
        except ValueError:
            print("Deposit must be a number")

    elif option.lower() == "w":
        try:
            withdraw = float(input("Enter the amount to withdraw: "))
            if withdraw < 1:
                print("Withdraw must be greater than 0")
            else:
                withdraws.append(-(withdraw))
                if withdraw > 500:
                    print("Withdraw limit exceeded")
                elif withdraw > balance:
                    print("Balance is insufficient")
                elif len(withdraws) > DAILY_WITHDRAWAL_LIMIT:
                    print("Exceeded daily withdrawal limit of 3")
                else:
                    balance -= withdraw
                    print(f"Withdrawn: R$ {withdraw}")
        except ValueError:
            print("Withdraw must be a number")

    elif option.lower() == "b":
        formatted_deposits = [f"R$ {deposit:.2f}" for deposit in deposits]
        formatted_withdraws = [f"R$ {withdraw:.2f}" for withdraw in withdraws]

        print(
            f"Deposits: {formatted_deposits} \nWithdraws: {formatted_withdraws} \nBalance: R$ {balance:.2f}\n"
        )
    elif option.lower() == "q":
        print("Service terminated. \nHave a nice day.")
        break
    else:
        print("invalid option")
