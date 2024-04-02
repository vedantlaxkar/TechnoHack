from tkinter import *
from forex_python.converter import CurrencyRates

# Currency converter function
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get().upper()
        to_currency = to_currency_var.get().upper()

        c = CurrencyRates()
        result = c.convert(from_currency, to_currency, amount)
        
        result_label.config(text=f"{amount} {from_currency} = {result:.2f} {to_currency}")
    except ValueError:
        result_label.config(text="Please enter a valid amount.")
    except:
        result_label.config(text="An error occurred. Please try again.")

# Main window
root = Tk()
root.title("Currency Converter")
root.configure(background="#007BFF")  # Setting background color to blue
root.geometry("500x350")  # Set window size

# Currency Converter Section
currency_frame = Frame(root, bg="#007BFF")
currency_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

amount_label = Label(currency_frame, text="Amount:", font=("Helvetica", 16), bg="#007BFF", fg="white")
amount_label.grid(row=0, column=0, padx=10, pady=10)
amount_entry = Entry(currency_frame, font=("Helvetica", 16))
amount_entry.grid(row=0, column=1, padx=10, pady=10)

from_currency_label = Label(currency_frame, text="From:", font=("Helvetica", 16), bg="#007BFF", fg="white")
from_currency_label.grid(row=1, column=0, padx=10, pady=10)

from_currency_var = StringVar()
from_currency_var.set("USD")  # Default currency
from_currency_options = ["USD", "EUR", "GBP", "INR", "AUD", "CAD", "SGD", "CHF", "MYR", "JPY", "CNY", "NZD", "THB", "HUF", "AED", "HKD", "MXN", "ZAR", "PHP", "SEK", "IDR", "SAR", "BRL", "TRY", "RUB", "NOK", "DKK", "PLN", "KRW"]
from_currency_dropdown = OptionMenu(currency_frame, from_currency_var, *from_currency_options)
from_currency_dropdown.config(font=("Helvetica", 16), bg="#33A1DE", fg="white")
from_currency_dropdown.grid(row=1, column=1, padx=10, pady=10)

to_currency_label = Label(currency_frame, text="To:", font=("Helvetica", 16), bg="#007BFF", fg="white")
to_currency_label.grid(row=2, column=0, padx=10, pady=10)

to_currency_var = StringVar()
to_currency_var.set("EUR")  # Default currency
to_currency_options = ["USD", "EUR", "GBP", "INR", "AUD", "CAD", "SGD", "CHF", "MYR", "JPY", "CNY", "NZD", "THB", "HUF", "AED", "HKD", "MXN", "ZAR", "PHP", "SEK", "IDR", "SAR", "BRL", "TRY", "RUB", "NOK", "DKK", "PLN", "KRW"]
to_currency_dropdown = OptionMenu(currency_frame, to_currency_var, *to_currency_options)
to_currency_dropdown.config(font=("Helvetica", 16), bg="#33A1DE", fg="white")
to_currency_dropdown.grid(row=2, column=1, padx=10, pady=10)

convert_button = Button(currency_frame, text="Convert", font=("Helvetica", 16), bg="#33FF57", fg="white", command=convert_currency)  # Green
convert_button.grid(row=3, columnspan=2, padx=10, pady=10)

result_label = Label(currency_frame, text="", font=("Helvetica", 16), bg="#007BFF", fg="white")
result_label.grid(row=4, columnspan=2, padx=10, pady=10)

root.mainloop()
