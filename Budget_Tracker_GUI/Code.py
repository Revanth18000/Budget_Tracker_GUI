import tkinter as tk
from tkinter import messagebox
import json

expenses = []
initial_budget = 0

def add_expense():
    desc = desc_entry.get()
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount.")
        return

    expenses.append({'description': desc, 'amount': amount})
    desc_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    update_summary()

def update_summary():
    total = sum(e['amount'] for e in expenses)
    remaining = initial_budget - total

    expense_list.delete(0, tk.END)
    for e in expenses:
        expense_list.insert(tk.END, f"{e['description']}: ₹{e['amount']}")

    total_label.config(text=f"Total Spent: ₹{total}")
    balance_label.config(text=f"Remaining Budget: ₹{remaining}")

def set_budget():
    global initial_budget
    try:
        initial_budget = float(budget_entry.get())
        update_summary()
        budget_entry.config(state='disabled')
        set_button.config(state='disabled')
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid budget.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Budget Tracker")

# Budget Input
tk.Label(root, text="Enter Initial Budget:").pack()
budget_entry = tk.Entry(root)
budget_entry.pack()
set_button = tk.Button(root, text="Set Budget", command=set_budget)
set_button.pack()

# Expense Input
tk.Label(root, text="\nExpense Description:").pack()
desc_entry = tk.Entry(root)
desc_entry.pack()

tk.Label(root, text="Expense Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack()

# Summary and Expense List
expense_list = tk.Listbox(root, width=50)
expense_list.pack(pady=10)

total_label = tk.Label(root, text="Total Spent: ₹0")
total_label.pack()

balance_label = tk.Label(root, text="Remaining Budget: ₹0")
balance_label.pack()

root.mainloop()
