import tkinter as tk
from tkinter import messagebox

class ATMSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM System")
        self.master.geometry("300x400")

        self.user_id_label = tk.Label(master, text="User ID")
        self.user_id_label.pack()
        self.user_id_entry = tk.Entry(master, width=20)
        self.user_id_entry.pack()

        self.pin_label = tk.Label(master, text="PIN")
        self.pin_label.pack()
        self.pin_entry = tk.Entry(master, width=20, show="*")
        self.pin_entry.pack()

        # Login button
        self.login_button = tk.Button(master, text="Login", command=self.check_credentials)
        self.login_button.pack()

        # ATM functionality (hidden initially)
        self.atm_frame = tk.Frame(master)
        self.atm_frame.pack_forget()

        # Initialize account balance and transaction history
        self.balance = 1000
        self.transaction_history = []

    def check_credentials(self):
        user_id = self.user_id_entry.get()
        pin = self.pin_entry.get()
        if user_id == "1234" and pin == "1234":  
            self.user_id_label.pack_forget()
            self.user_id_entry.pack_forget()
            self.pin_label.pack_forget()
            self.pin_entry.pack_forget()
            self.login_button.pack_forget()
            self.atm_frame.pack()
            self.create_atm_widgets()
        else:
            messagebox.showerror("Error", "Invalid user ID or PIN")

    def create_atm_widgets(self):
        # Transaction history button
        self.history_button = tk.Button(self.atm_frame, text="Transaction History", command=self.show_history)
        self.history_button.pack()

        # Withdraw button
        self.withdraw_button = tk.Button(self.atm_frame, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()

        # Deposit button
        self.deposit_button = tk.Button(self.atm_frame, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        # Transfer button
        self.transfer_button = tk.Button(self.atm_frame, text="Transfer", command=self.transfer)
        self.transfer_button.pack()

        # Quit button
        self.quit_button = tk.Button(self.atm_frame, text="Quit", command=self.master.destroy)
        self.quit_button.pack()

    def show_history(self):
        self.clear_atm_frame()
        history_text = tk.Text(self.atm_frame, width=40, height=10)
        history_text.pack()
        for transaction in self.transaction_history:
            history_text.insert(tk.END, transaction + "\n")
        back_button = tk.Button(self.atm_frame, text="Back", command=lambda: self.back_to_menu(history_text, back_button))
        back_button.pack()

    def withdraw(self):
        self.clear_atm_frame()
        amount_label = tk.Label(self.atm_frame, text="Enter amount:")
        amount_label.pack()
        amount_entry = tk.Entry(self.atm_frame, width=20)
        amount_entry.pack()
        
        def withdraw_amount():
            amount = int(amount_entry.get())
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Withdrawal: -{amount}")
                messagebox.showinfo("Success", "Withdrawal successful")
            else:
                messagebox.showerror("Error", "Insufficient balance")
        
        withdraw_button = tk.Button(self.atm_frame, text="Withdraw", command=withdraw_amount)
        withdraw_button.pack()
        back_button = tk.Button(self.atm_frame, text="Back", command=lambda: self.back_to_menu(amount_label, amount_entry, withdraw_button, back_button))
        back_button.pack()

    def deposit(self):
        self.clear_atm_frame()
        amount_label = tk.Label(self.atm_frame, text="Enter amount:")
        amount_label.pack()
        amount_entry = tk.Entry(self.atm_frame, width=20)
        amount_entry.pack()

        def deposit_amount():
            amount = int(amount_entry.get())
            self.balance += amount
            self.transaction_history.append(f"Deposit: +{amount}")
            messagebox.showinfo("Success", "Deposit successful")
        
        deposit_button = tk.Button(self.atm_frame, text="Deposit", command=deposit_amount)
        deposit_button.pack()
        back_button = tk.Button(self.atm_frame, text="Back", command=lambda: self.back_to_menu(amount_label, amount_entry, deposit_button, back_button))
        back_button.pack()

    def transfer(self):
        self.clear_atm_frame()
        recipient_label = tk.Label(self.atm_frame, text="Enter recipient's account number:")
        recipient_label.pack()
        recipient_entry = tk.Entry(self.atm_frame, width=20)
        recipient_entry.pack()
        amount_label = tk.Label(self.atm_frame, text="Enter amount:")
        amount_label.pack()
        amount_entry = tk.Entry(self.atm_frame, width=20)
        amount_entry.pack()

        def transfer_amount():
            recipient = recipient_entry.get()
            amount = int(amount_entry.get())
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Transfer to {recipient}: -{amount}")
                messagebox.showinfo("Success", "Transfer successful")
            else:
                messagebox.showerror("Error", "Insufficient balance")
        
        transfer_button = tk.Button(self.atm_frame, text="Transfer", command=transfer_amount)
        transfer_button.pack()
        back_button = tk.Button(self.atm_frame, text="Back", command=lambda: self.back_to_menu(recipient_label, recipient_entry, amount_label, amount_entry, transfer_button, back_button))
        back_button.pack()

    def clear_atm_frame(self):
        for widget in self.atm_frame.winfo_children():
            widget.pack_forget()

    def back_to_menu(self, *widgets_to_remove):
        for widget in widgets_to_remove:
            widget.pack_forget()
        self.create_atm_widgets()

if __name__ == "__main__":
    root = tk.Tk()
    atm = ATMSystem(root)
    root.mainloop()
