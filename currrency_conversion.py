from tkinter import *
import requests

# Window Details
current = Tk()
current.title("Currency Converter")
current.geometry("500x500")
current.config(bg="skyblue")

info = requests.get("https://v6.exchangerate-api.com/v6/5f809448d8e0bf0ba369b44d/latest/USD")
info_json = info.json()

variable1 = StringVar()
StringVar = IntVar()

conversion_rates = info_json['conversion_rates']
# print(conversion_rates)

convert_list = Listbox(current, width=20, height=5, bg="blue")
for i in conversion_rates.keys():
    convert_list.insert(END, str(i))
convert_list.place(x=250, y=225)

def conversion():
    num = float(amount_entry.get())
    print(info_json['conversion_rates'][convert_list.get(ACTIVE)])
    ans = num * info_json['conversion_rates'][convert_list.get(ACTIVE)]
    converted_amount.insert(END, ans)

def clear():
    amount_entry.delete(0, END)
    converted_amount.delete(0, END)

def exit_program():
    return current.destroy()

# Creating Labels
program = Label(current, text="Currency Conversion Program", bg="skyblue")
amount = Label(current, text="Amount", bg="skyblue")
currency_from = Label(current, text="Currency From USD", bg="skyblue")
currency_to = Label(current, text="Currency To", bg="skyblue")
converted = Label(current, text="Converted Amount", bg="skyblue")

# Creating Entries
amount_entry = Entry(current, text="", bg="blue")
converted_amount = Entry(current, bg="blue")

# Creating Buttons
convert = Button(current, text="Convert", command=conversion, bg="white")
clear = Button(current, text="Clear", command=clear, bg="white")
exit = Button(current, text="Exit", command=exit_program, bg="white")

# Placing Labels
program.place(x=150, y=50)
amount.place(x=50, y=100)
currency_from.place(x=175, y=175)
currency_to.place(x=50, y=225)
converted.place(x=50, y=400)

# Placing Entries
amount_entry.place(x=250, y=100)
converted_amount.place(x=250, y=400)

# Placing Buttons
convert.place(x=250, y=350)
clear.place(x=150, y=450)
exit.place(x=250, y=450)

# To keep program running
current.mainloop()
