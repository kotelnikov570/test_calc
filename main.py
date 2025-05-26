from calculator import Calculator

def main():
    calc = Calculator()
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Модуль")
        print("7. Выход")

        choice = input("Введите номер операции (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Выход...")
            break

        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == '1':
            print(f"Результат: {calc.add(num1, num2)}")
        elif choice == '2':
            print(f"Результат: {calc.subtract(num1, num2)}")
        elif choice == '3':
            print(f"Результат: {calc.multiply(num1, num2)}")
        elif choice == '4':
            print(f"Результат: {calc.divide(num1, num2)}")
        elif choice == '5':
            print(f"Результат: {calc.exponentiate(num1, num2)}")
        elif choice == '6':
            print(f"Результат: {calc.modulus(num1, num2)}")
        else:
            print("Неверный ввод")

if __name__ == "__main__":
    main()
