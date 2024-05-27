import tkinter as tk
from tkinter import messagebox
from bank import Bank

class BankingApp:
    def __init__(self, root):
        self.bank = Bank()
        self.root = root
        self.root.title("Banking App")

        # Create frames
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        # Account creation
        self.lbl_account_number = tk.Label(self.frame, text="Account Number")
        self.lbl_account_number.grid(row=0, column=0, padx=10, pady=5)
        self.entry_account_number = tk.Entry(self.frame)
        self.entry_account_number.grid(row=0, column=1, padx=10, pady=5)

        self.lbl_owner = tk.Label(self.frame, text="Owner")
        self.lbl_owner.grid(row=1, column=0, padx=10, pady=5)
        self.entry_owner = tk.Entry(self.frame)
        self.entry_owner.grid(row=1, column=1, padx=10, pady=5)

        self.lbl_initial_deposit = tk.Label(self.frame, text="Initial Deposit")
        self.lbl_initial_deposit.grid(row=2, column=0, padx=10, pady=5)
        self.entry_initial_deposit = tk.Entry(self.frame)
        self.entry_initial_deposit.grid(row=2, column=1, padx=10, pady=5)

        self.btn_create_account = tk.Button(self.frame, text="Create Account", command=self.create_account)
        self.btn_create_account.grid(row=3, columnspan=2, pady=10)

        # Operations
        self.lbl_account_number_op = tk.Label(self.frame, text="Account Number")
        self.lbl_account_number_op.grid(row=4, column=0, padx=10, pady=5)
        self.entry_account_number_op = tk.Entry(self.frame)
        self.entry_account_number_op.grid(row=4, column=1, padx=10, pady=5)

        self.lbl_amount = tk.Label(self.frame, text="Amount")
        self.lbl_amount.grid(row=5, column=0, padx=10, pady=5)
        self.entry_amount = tk.Entry(self.frame)
        self.entry_amount.grid(row=5, column=1, padx=10, pady=5)

        self.btn_deposit = tk.Button(self.frame, text="Deposit", command=self.deposit)
        self.btn_deposit.grid(row=6, column=0, pady=10)

        self.btn_withdraw = tk.Button(self.frame, text="Withdraw", command=self.withdraw)
        self.btn_withdraw.grid(row=6, column=1, pady=10)

        self.btn_check_balance = tk.Button(self.frame, text="Check Balance", command=self.check_balance)
        self.btn_check_balance.grid(row=7, columnspan=2, pady=10)

    def create_account(self):
        account_number = self.entry_account_number.get()
        owner = self.entry_owner.get()
        try:
            initial_deposit = float(self.entry_initial_deposit.get())
        except ValueError:
            initial_deposit = 0

        result = self.bank.create_account(account_number, owner, initial_deposit)
        messagebox.showinfo("Create Account", result)

    def deposit(self):
        account_number = self.entry_account_number_op.get()
        account = self.bank.get_account(account_number)
        if account:
            try:
                amount = float(self.entry_amount.get())
                result = account.deposit(amount)
                messagebox.showinfo("Deposit", result)
            except ValueError:
                messagebox.showerror("Error", "Invalid amount")
        else:
            messagebox.showerror("Error", "Account not found")

    def withdraw(self):
        account_number = self.entry_account_number_op.get()
        account = self.bank.get_account(account_number)
        if account:
            try:
                amount = float(self.entry_amount.get())
                result = account.withdraw(amount)
                messagebox.showinfo("Withdraw", result)
            except ValueError:
                messagebox.showerror("Error", "Invalid amount")
        else:
            messagebox.showerror("Error", "Account not found")

    def check_balance(self):
        account_number = self.entry_account_number_op.get()
        account = self.bank.get_account(account_number)
        if account:
            result = account.check_balance()
            messagebox.showinfo("Check Balance", result)
        else:
            messagebox.showerror("Error", "Account not found")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()
