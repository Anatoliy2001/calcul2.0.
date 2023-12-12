import tkinter as tk
import unittest
from tkinter import messagebox

# Класс для работы с дробями
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def to_decimal(self):
        return self.numerator / self.denominator

# Класс для математических операций с дробями
class FractionCalculator:
    def __init__(self, fraction1, fraction2):
        self.fraction1 = fraction1
        self.fraction2 = fraction2

    def add(self):
        result_numerator = self.fraction1.numerator * self.fraction2.denominator + self.fraction2.numerator * self.fraction1.denominator
        result_denominator = self.fraction1.denominator * self.fraction2.denominator
        return Fraction(result_numerator, result_denominator)

    def subtract(self):
        result_numerator = self.fraction1.numerator * self.fraction2.denominator - self.fraction2.numerator * self.fraction1.denominator
        result_denominator = self.fraction1.denominator * self.fraction2.denominator
        return Fraction(result_numerator, result_denominator)

    def multiply(self):
        result_numerator = self.fraction1.numerator * self.fraction2.numerator
        result_denominator = self.fraction1.denominator * self.fraction2.denominator
        return Fraction(result_numerator, result_denominator)

    def divide(self):
        result_numerator = self.fraction1.numerator * self.fraction2.denominator
        result_denominator = self.fraction1.denominator * self.fraction2.numerator
        return Fraction(result_numerator, result_denominator)
    
class FractionCalculatorApp(tk.Tk):
    @unittest.skip("Этот тест пропущен из-за определенной причины")
    def __init__(self):
        super().__init__()
        self.title("Калькулятор дробей")
        self.label_fraction1 = tk.Label(self, text="Введите первую дробь:")
        self.label_fraction1.grid(row=0, column=0)

        self.entry_fraction1_numerator = tk.Entry(self)
        self.entry_fraction1_numerator.grid(row=0, column=1)

        self.label_slash1 = tk.Label(self, text="/")
        self.label_slash1.grid(row=0, column=2)

        self.entry_fraction1_denominator = tk.Entry(self)
        self.entry_fraction1_denominator.grid(row=0, column=3)

        self.label_fraction2 = tk.Label(self, text="Введите вторую дробь:")
        self.label_fraction2.grid(row=1, column=0)

        self.entry_fraction2_numerator = tk.Entry(self)
        self.entry_fraction2_numerator.grid(row=1, column=1)

        self.label_slash2 = tk.Label(self, text="/")
        self.label_slash2.grid(row=1, column=2)

        self.entry_fraction2_denominator = tk.Entry(self)
        self.entry_fraction2_denominator.grid(row=1, column=3)

        self.button_add = tk.Button(self, text="Сложить", command=self.add_fractions)
        self.button_add.grid(row=2, column=0)

        self.button_subtract = tk.Button(self, text="Вычесть", command=self.subtract_fractions)
        self.button_subtract.grid(row=2, column=1)

        self.button_multiply = tk.Button(self, text="Умножить", command=self.multiply_fractions)
        self.button_multiply.grid(row=2, column=2)

        self.button_divide = tk.Button(self, text="Разделить", command=self.divide_fractions)
        self.button_divide.grid(row=2, column=3)

        self.button_convert_to_decimal = tk.Button(self, text="Перевести в десятичную", command=self.convert_to_decimal)
        self.button_convert_to_decimal.grid(row=3, columnspan=4)

    def add_fractions(self):
        try:
            fraction1_numerator = int(self.entry_fraction1_numerator.get())
            fraction1_denominator = int(self.entry_fraction1_denominator.get())
            fraction2_numerator = int(self.entry_fraction2_numerator.get())
            fraction2_denominator = int(self.entry_fraction2_denominator.get())

            fraction1 = Fraction(fraction1_numerator, fraction1_denominator)
            fraction2 = Fraction(fraction2_numerator, fraction2_denominator)

            calculator = FractionCalculator(fraction1, fraction2)

            sum_result = calculator.add()
            sum_result_decimal = sum_result.numerator / sum_result.denominator
            sum_result_str = f"Сумма: {sum_result.numerator}/{sum_result.denominator} ({sum_result_decimal})"
            #messagebox.showinfo("Результат", sum_result_str)

        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите целые числа для числителя и знаменателя дроби.")
    def subtract_fractions(self):
        try:
            fraction1_numerator = int(self.entry_fraction1_numerator.get())
            fraction1_denominator = int(self.entry_fraction1_denominator.get())
            fraction2_numerator = int(self.entry_fraction2_numerator.get())
            fraction2_denominator = int(self.entry_fraction2_denominator.get())

            fraction1 = Fraction(fraction1_numerator, fraction1_denominator)
            fraction2 = Fraction(fraction2_numerator, fraction2_denominator)

            calculator = FractionCalculator(fraction1, fraction2)

            difference_result = calculator.subtract()
            difference_result_decimal = difference_result.numerator / difference_result.denominator
            difference_result_str = f"Разность: {difference_result.numerator}/{difference_result.denominator} ({difference_result_decimal})"
            #messagebox.showinfo("Результат", difference_result_str)

        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите целые числа для числителя и знаменателя дроби.")

    def multiply_fractions(self):
        try:
            fraction1_numerator = int(self.entry_fraction1_numerator.get())
            fraction1_denominator = int(self.entry_fraction1_denominator.get())
            fraction2_numerator = int(self.entry_fraction2_numerator.get())
            fraction2_denominator = int(self.entry_fraction2_denominator.get())

            fraction1 = Fraction(fraction1_numerator, fraction1_denominator)
            fraction2 = Fraction(fraction2_numerator, fraction2_denominator)

            calculator = FractionCalculator(fraction1, fraction2)

            product_result = calculator.multiply()
            product_decimal = product_result.numerator / product_result.denominator
            product_result_str = f"Произведение: {product_result.numerator}/{product_result.denominator} ({product_decimal})"
            #messagebox.showinfo("Результат", product_result_str)

        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите целые числа для числителя и знаменателя дроби.")

    def divide_fractions(self):
        try:
            fraction1_numerator = int(self.entry_fraction1_numerator.get())
            fraction1_denominator = int(self.entry_fraction1_denominator.get())
            fraction2_numerator = int(self.entry_fraction2_numerator.get())
            fraction2_denominator = int(self.entry_fraction2_denominator.get())

            fraction1 = Fraction(fraction1_numerator, fraction1_denominator)
            fraction2 = Fraction(fraction2_numerator, fraction2_denominator)

            calculator = FractionCalculator(fraction1, fraction2)

            quotient_result = calculator.divide()
            quotient_decimal = quotient_result.numerator / quotient_result.denominator
            quotient_result_str = f"Частное: {quotient_result.numerator}/{quotient_result.denominator} ({quotient_decimal})"
            #messagebox.showinfo("Результат", quotient_result_str)

        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите целые числа для числителя и знаменателя дроби. Помните, что деление на ноль недопустимо.")

    def convert_to_decimal(self):
        try:
            fraction1_numerator = int(self.entry_fraction1_numerator.get())
            fraction1_denominator = int(self.entry_fraction1_denominator.get())
            fraction2_numerator = int(self.entry_fraction2_numerator.get())
            fraction2_denominator = int(self.entry_fraction2_denominator.get())

            fraction1 = Fraction(fraction1_numerator, fraction1_denominator)
            fraction2 = Fraction(fraction2_numerator, fraction2_denominator)

            decimal1 = fraction1.numerator / fraction1.denominator
            decimal2 = fraction2.numerator / fraction2.denominator

            #messagebox.showinfo("Десятичные значения", f"Первая дробь в десятичном виде: {decimal1}\nВторая дробь в десятичном виде: {decimal2}")

        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите целые числа для числителя и знаменателя дроби.")

if __name__ == "__main__":
    app = FractionCalculatorApp()
    app.mainloop()
