from tkinter import *

# Temperature converter function
def convert_temperature():
    try:
        temperature = float(temp_entry.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()

        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (temperature * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = temperature + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (temperature - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (temperature + 459.67) * 5/9
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = temperature - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (temperature * 9/5) - 459.67
        else:
            result = temperature

        result_label.config(text=f"{temperature}° {from_unit} = {result:.2f}° {to_unit}")
    except ValueError:
        result_label.config(text="Please enter a valid temperature.")
    except:
        result_label.config(text="An error occurred. Please try again.")

# Main window
root = Tk()
root.title("Temperature Converter")
root.configure(background="#007BFF")  # Setting background color to blue
root.geometry("500x350")  # Set window size

# Temperature Converter Section
temp_frame = Frame(root, bg="#007BFF")
temp_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

temp_label = Label(temp_frame, text="Temperature:", font=("Helvetica", 16), bg="#007BFF", fg="white")
temp_label.grid(row=0, column=0, padx=10, pady=10)
temp_entry = Entry(temp_frame, font=("Helvetica", 16))
temp_entry.grid(row=0, column=1, padx=10, pady=10)

from_unit_label = Label(temp_frame, text="From:", font=("Helvetica", 16), bg="#007BFF", fg="white")
from_unit_label.grid(row=1, column=0, padx=10, pady=10)

from_unit_var = StringVar()
from_unit_var.set("Celsius")  # Default unit
from_unit_options = ["Celsius", "Fahrenheit", "Kelvin"]
from_unit_dropdown = OptionMenu(temp_frame, from_unit_var, *from_unit_options)
from_unit_dropdown.config(font=("Helvetica", 16), bg="#33A1DE", fg="white")
from_unit_dropdown.grid(row=1, column=1, padx=10, pady=10)

to_unit_label = Label(temp_frame, text="To:", font=("Helvetica", 16), bg="#007BFF", fg="white")
to_unit_label.grid(row=2, column=0, padx=10, pady=10)

to_unit_var = StringVar()
to_unit_var.set("Fahrenheit")  # Default unit
to_unit_options = ["Celsius", "Fahrenheit", "Kelvin"]
to_unit_dropdown = OptionMenu(temp_frame, to_unit_var, *to_unit_options)
to_unit_dropdown.config(font=("Helvetica", 16), bg="#33A1DE", fg="white")
to_unit_dropdown.grid(row=2, column=1, padx=10, pady=10)

convert_button = Button(temp_frame, text="Convert", font=("Helvetica", 16), bg="#FF5733", fg="white", command=convert_temperature)  # Orange
convert_button.grid(row=3, columnspan=2, padx=10, pady=10)

result_label = Label(temp_frame, text="", font=("Helvetica", 16), bg="#007BFF", fg="white")
result_label.grid(row=4, columnspan=2, padx=10, pady=10)

root.mainloop()
