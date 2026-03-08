class OverdraftError(Exception):
    pass

class BankAccount:

    total_accounts = 0
    
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0
        self.transaction_history = []
        BankAccount.total_accounts += 1
        
    @property
    def balance(self):
        return self.__balance
        
    def __str__(self):
        return f"BankAccount Owner: {self.owner}, Balance: {self.__balance}"

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        elif amount > 1000:
            raise ValueError("Deposit limit is 1000.")
        self.__balance += amount
        self.transaction_history.append(f"Deposit: +{amount} on {self.owner}'s account")
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            raise OverdraftError("Insufficient funds.")
        elif amount > 1000:
            raise ValueError("Withdrawal limit is 1000.")
        self.__balance -= amount
        self.transaction_history.append(f"Withdraw: -{amount} on {self.owner}'s account")
        print(f"Withdrew {amount}. New balance: {self.__balance}")

    def transfer(self, amount, target_account):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        elif amount > self.__balance:
            raise OverdraftError("Insufficient funds.")
        elif amount > 10000:
            raise ValueError("Transfer limit is 10000.")
        self.__balance -= amount
        target_account.__balance += amount
        self.transaction_history.append(f"Transfer: -{amount} to {target_account.owner}'s account")
        target_account.transaction_history.append(f"Transfer: +{amount} from {self.owner}'s account")
        print(f"Transferred {amount} to {target_account.owner}. New balance: {self.__balance}")

    def show_transaction_history(self):
        if not self.transaction_history:
            print("No transactions yet.")
            return
        print(f"Transaction history for {self.owner}'s account:")
        for transaction in self.transaction_history:
            print(f"- {transaction}")

def main():
    account1 = BankAccount("Alice")
    account2 = BankAccount("Bob")
    
    account1.deposit(500)
    try:
        account1.withdraw(600)
    except OverdraftError as e:
        print(e)
    try:
        account1.transfer(100, account2)
    except OverdraftError as e:
        print(e)
    
    account1.show_transaction_history()
    account2.show_transaction_history()
    
    print(f"Total bank accounts: {BankAccount.total_accounts}")

if __name__ == "__main__":
    main()