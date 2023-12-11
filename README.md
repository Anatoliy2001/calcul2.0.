План тестирования
TestFraction класс:
 
setUp(self): Метод инициализации, который создает экземпляры дробей fraction1 (1/2) и fraction2 (3/4) для использования во всех тестах.
test_to_decimal(self): Проверяет правильность преобразования дробей в десятичные числа с использованием метода to_decimal.
TestFractionCalculator класс:

setUp(self): Метод инициализации, который создает экземпляр calculator класса FractionCalculator с двумя исходными дробями.
test_add(self): Проверяет правильность операции сложения дробей с использованием метода add.
test_subtract(self): Проверяет правильность операции вычитания дробей с использованием метода subtract.
test_multiply(self): Проверяет правильность операции умножения дробей с использованием метода multiply.
test_divide(self): Проверяет правильность операции деления дробей с использованием метода divide.

Модульное тестирование класса Fraction:

Тест кейс 1: Проверка правильности преобразования дроби в десятичное число с использованием метода to_decimal.
Ожидаемый результат: Результат преобразования дроби в десятичное число равен 0.5.

Тест кейс 2: Подтверждение корректной инициализации и установки экземпляров класса Fraction.
Модульное тестирование класса FractionCalculator:

Тест кейс 1: Проверка точности операции сложения дробей.
Ожидаемый результат: Результатом сложения дробей будет Fraction(10, 8).

Тест кейс 2: Проверка правильности операции вычитания дробей.
Ожидаемый результат: Результатом вычитания дробей будет Fraction(-2, 8).

Тест кейс 3: Подтверждение точности операции умножения дробей.
Ожидаемый результат: Результатом умножения дробей будет Fraction(3, 8).

Тест кейс 4: Проверка правильности операции деления дробей.
Ожидаемый результат: Результатом деления дробей будет Fraction(4, 6).
