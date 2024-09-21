# Challenge 1: Bank Account

### Instructions
Just one user, no account, no login

### Bank Menu
- [x] Should have an option menu for the user.
- [x] Bank options include: deposit, withdraw, and balance. (one letter for each option D, W, and B)

### Deposit Rules
- [x] All deposits are stored in the variable balance.

### Withdrawal Rules
- [x] Withdrawals are stored in the variable balance.
- [x] 3 withdrawals limit per day
- [x] Withdrawals are limited to a maximum of R$500.

### Balance Rules
- [x] The balance is stored in the variable balance.
- [x] The balance can never be negative.
- [x] If the balance is not enough to complete the transaction, print "Saldo Insuficiente".
- [x] balance option should list all deposits made
- [x] balance option should list all withdrawals made
- [x] balance option should list total balance
- [x] if balance is zero, print "Não foram realizadas movimentações"
- [x] format should be: R$ xxx.xx

# Challenge 2: Timestamps

### Transactions Limit
- [x] Transactions limit per day should be 10
- [x] An Alert if user has exceeded transactions limit
- [x] Balance must show the timestamp (date and hour) of the all transactions

# Challenge 3: Refactor using functions
obs - didn't know it was the challenge and already did the refactor of the logic into separated functions on Challenge 2

- [x] separate deposit, withdraw and balance logic into functions
- [x] create function create user
- [x] create function create bank account
- Optional
- [x] create function to list Accounts or Users
- [] create func to list how many accounts each user has

User: Dictionary (can't have two users with same person_ID)
    name: str
    birthday: date
    person_ID: str (validation: only numbers, no letters or special characters)
    address: str (street, number - neighborhood - city/state_acronym)

Account: Dictionary
    agency: str(only one agency, must be 0001)
    account_number: str (sequential initialized at 1)
    user: User

- Constraints
- [X] Can't have accounts without user 
- [ ] Only one account per person_ID
- [ ] One user can have multiple accounts