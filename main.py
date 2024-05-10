import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green


# increase
def button_callback_multiple():
    result = entryPercentMultiple.getdouble(entryPercentMultiple.get()) * (
            1 + percentPercentMultiple.getdouble(percentPercentMultiple.get()) / 100)
    buttonPercentMultiple.configure(text=result)


def button_callback_reduce():
    result = entryPercentReduce.getdouble(entryPercentReduce.get()) * (
            1 - percentPercentReduce.getdouble(percentPercentReduce.get()) / 100)
    buttonPercentReduce.configure(text=result)


def button_callback_average():
    result = (number1Average.getdouble(number1Average.get()) + number2Average.getdouble(
        number2Average.get()) + number3Average.getdouble(number3Average.get())) / numbersAverage.getint(
        numbersAverage.get())
    buttonAverage.configure(text=result)


app = customtkinter.CTk()
app.title("Percent Calculator")
app.geometry("1000x500")

labelPercentMultiple = customtkinter.CTkLabel(app, text="Прибавить процент к числу")
entryPercentMultiple = customtkinter.CTkEntry(app, placeholder_text="Число")
percentPercentMultiple = customtkinter.CTkEntry(app, placeholder_text="Процент(без %)")
buttonPercentMultiple = customtkinter.CTkButton(app, text="Результат", command=button_callback_multiple)

labelPercentMultiple.grid(row=0, column=1, padx=20, pady=20)
entryPercentMultiple.grid(row=1, column=0, padx=60, pady=20)
percentPercentMultiple.grid(row=1, column=1, padx=60, pady=20)
buttonPercentMultiple.grid(row=1, column=2, padx=60, pady=20)

# reduce
labelPercentReduce = customtkinter.CTkLabel(app, text="Отнять процент от числа")
entryPercentReduce = customtkinter.CTkEntry(app, placeholder_text="Число")
percentPercentReduce = customtkinter.CTkEntry(app, placeholder_text="Процент(без %)")
buttonPercentReduce = customtkinter.CTkButton(app, text="Результат", command=button_callback_reduce)

labelPercentReduce.grid(row=2, column=1, padx=20, pady=20)
entryPercentReduce.grid(row=3, column=0, padx=60, pady=20)
percentPercentReduce.grid(row=3, column=1, padx=60, pady=20)
buttonPercentReduce.grid(row=3, column=2, padx=60, pady=20)

# average
labelAverage = customtkinter.CTkLabel(app, text="Среднее арифм.")
number1Average = customtkinter.CTkEntry(app, placeholder_text="1 Число")
number2Average = customtkinter.CTkEntry(app, placeholder_text="2 Число")
number3Average = customtkinter.CTkEntry(app, placeholder_text="3 Число")
numbersAverage = customtkinter.CTkEntry(app, placeholder_text="Количество чисел")
buttonAverage = customtkinter.CTkButton(app, text="Результат", command=button_callback_average)

labelAverage.grid(row=4, column=1, padx=20, pady=20)
number1Average.grid(row=5, column=0, padx=40, pady=20)
number2Average.grid(row=5, column=1, padx=40, pady=20)
number3Average.grid(row=5, column=2, padx=40, pady=20)
numbersAverage.grid(row=5, column=4, padx=40, pady=20)
buttonAverage.grid(row=6, column=1, padx=40, pady=20)

app.mainloop()