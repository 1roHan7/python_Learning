class BankAccount:
    def __init__(self,account_number, account_holder, balance=0):
        self.__account_number = account_number
        self._account_holder = account_holder
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}. New Balance: {self.__balance}")

    def withdraw(self, amount):
        self.__balance -= amount
        print(f"Withdrew: {amount}. New Balance: {self.__balance}")
    
    @property
    def balance(self):
        print(f"Current Balance: {self.__balance}")

class SavingsAccount(BankAccount):
    def __init__ (self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.__balance * self.interest_rate
        self.deposit(interest)
        print(f"Added interest: {interest}. New Balance: {self.__balance}") 
    
class CurrentAccount(BankAccount):
    def __init__ (self, account_number, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount > self.__balance + self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
        else:
            super().withdraw(amount)
class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_type,name,initial_deposit=0):
        self.account_type = account_type
        self.name = name    
        self.initial_deposit = initial_deposit
        if account_type == "savings":
            account = SavingsAccount("S"+str(len(self.accounts)+1), name, initial_deposit)
            self.accounts[account._BankAccount__account_number] = account
            print(f"Created Savings Account for {name} with account number {account._BankAccount__account_number}")

        else:
            account = CurrentAccount("C"+str(len(self.accounts)+1), name, initial_deposit)
            self.accounts[account._BankAccount__account_number] = account
            print(f"Created Current Account for {name} with account number {account._BankAccount__account_number}")
    
    def get_account(self, account_number):
        return self.accounts.get(account_number, None)
                
    def transfer(self, from_acc, to_acc, amount):
        from_account = self.get_account(from_acc)
        to_account = self.get_account(to_acc)
        if from_account and to_account:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            print(f"Transferred {amount} from {from_acc} to {to_acc}")
        else:
            print("One of the accounts does not exist.")
            
def main():
    bank = Bank()
    while True:
        print("\n--- Bank Account Management System ---")
        print("1. Create new account (Savings or Current)")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Transfer money between accounts")
        print("5. Display balance")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            acc_type = input("Enter account type (savings/current): ").lower()
            name = input("Enter account holder name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            bank.create_account(acc_type, name, initial_deposit)
        elif choice == "2":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            account = bank.get_account(acc_num)
            if account:
                account.deposit(amount)
            else:
                print("Account not found.")
        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            account = bank.get_account(acc_num)
            if account:
                account.withdraw(amount)
            else:
                print("Account not found.")
        elif choice == "4":
            from_acc = input("Enter FROM account number: ")
            to_acc = input("Enter TO account number: ")
            amount = float(input("Enter amount to transfer: "))
            bank.transfer(from_acc, to_acc, amount)
        elif choice == "5":
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                account.balance
            else:
                print("Account not found.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
                main()


