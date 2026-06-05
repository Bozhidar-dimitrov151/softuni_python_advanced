class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass


pin_cod, balance, age = input().split(", ")
balance = int(balance)
age = int(age)

while True:
    com = input().split("#")

    if com[0] == "End":
        break

    if com[0] == "Send Money":
        _, money_to_send, pin_code = com
        money_to_send = int(money_to_send)

        if age < 18:
            raise UnderageTransactionError(
                "You must be 18 years or older to perform online transactions"
            )

        if money_to_send > balance:
            raise MoneyNotEnoughError(
                "Insufficient funds for the requested transaction"
            )

        if pin_cod != pin_code:
            raise PINCodeError("Invalid PIN code")

        balance -= money_to_send

        print(f"Successfully sent {money_to_send} money to a friend")
        print(f"There is {balance} money left in the bank account")

    elif com[0] == "Receive Money":
        _, money = com
        money = float(money)

        if money < 0:
            raise MoneyIsNegativeError("Money cannot be negative")

        bank_account = money / 2

        print(f"{bank_account:.2f} money went straight into the bank account")