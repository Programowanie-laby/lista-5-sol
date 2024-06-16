import tkinter as tk
from tkinter import messagebox, ttk

from src.get_data import get_currencies_data
from src.utils import convert_currency


class GUI(tk.Tk):
    "Class implementing GUI for currency converter."

    def __init__(self):
        super().__init__()

        self.title("My GUI")
        self.geometry("280x300")
        self.currencies = get_currencies_data()

        self.label = ttk.Label(self, text="Currency Converter", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, columnspan=3, pady=(10, 20), sticky="n")

        # curreny from
        self.from_label = ttk.Label(self, text="From:")
        self.from_label.grid(row=1, column=0)
        self.from_combobox = ttk.Combobox(self, values=list(self.currencies.keys()))
        self.from_combobox.grid(row=1, column=1, pady=10)

        # currency info button
        currency_info = "".join(
            [
                f"{code}: {currency['name']}\n"
                for code, currency in self.currencies.items()
            ]
        )

        self.info_button = ttk.Button(
            self,
            text="Currency info",
            command=lambda: messagebox.showinfo("Currency Info", currency_info),
        )
        self.info_button.grid(row=1, column=2, pady=10)

        # currency to
        self.to_label = ttk.Label(self, text="To:")
        self.to_label.grid(row=2, column=0)
        self.to_combobox = ttk.Combobox(self, values=list(self.currencies.keys()))
        self.to_combobox.grid(row=2, column=1)

        # Amount Entry
        self.entry_frame = ttk.Frame(self)
        self.entry_frame.grid(row=3, column=0, columnspan=3, pady=10, padx=10)
        self.entry_label = ttk.Label(self.entry_frame, text="Amount:")
        self.entry_label.pack(side=tk.LEFT, padx=(0, 10))

        self.entry = ttk.Entry(self.entry_frame)
        self.entry.pack(side=tk.LEFT, expand=True, fill=tk.X)

        # Result Label
        self.result_frame = ttk.Frame(self, relief=tk.RAISED, borderwidth=2)
        self.result_frame.grid(
            row=4, column=0, columnspan=3, pady=10, padx=10, sticky="ew"
        )
        self.result_label = ttk.Label(
            self.result_frame, text="Converted amount", font=("Helvetica", 12)
        )
        self.result_label.pack(pady=10, padx=10)

        # Button for converting currency
        self.convert_button = ttk.Button(
            self, text="Convert", command=self.convert_currency
        )
        self.convert_button.grid(row=5, column=0, columnspan=3, pady=10)

    def convert_currency(self):
        from_currency = self.from_combobox.get()
        to_currency = self.to_combobox.get()
        try:
            from_rate = self.currencies[from_currency]["rate"]
            to_rate = self.currencies[to_currency]["rate"]
            amount = float(self.entry.get())
            result = convert_currency(amount, from_rate, to_rate)
            self.result_label.config(text=f"{result:.2f}")
        except Exception:
            self.result_label.config(text="Invalid input")
