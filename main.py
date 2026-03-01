from bank_account import BankAccount

account = BankAccount("Saleh Alsuwat", 500)

print("Account Holder:", account.get_account_holder())
print("Initial Balance:", account.get_balance())

new_balance = account.deposit(300)
print("Balance after deposit:", new_balance)

try:
    account.withdraw(1000)
except Exception as e:
    print("Withdraw Error:", e)

account.withdraw(200)
print("Final Balance:", account.get_balance())