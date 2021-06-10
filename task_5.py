""" 5. Написати повноцінний калькулятор. 
    Введення цифр та вибір математичної операції виконати в діалоговому стилі 
    (запитати у користувача, вивести меню). 
    У програмі передбачити уникнення помилок (ділення на нуль і т.д.)."""

try:
    exit = False
    while not exit:
        choice = int(input(
            "Оберіть дію:\n1. додавання\n2. віднімання\n3. множення\n4. ділення\n5. вихід\n:>> "))
        if choice == 1:
            num1 = int(input("Введіть перше число: "))
            num2 = int(input("Введіть друге число: "))
            rez = num1 + num2
            print(f'{num1} + {num2} = {rez}\n')
        elif choice == 2:
            num1 = int(input("Введіть перше число: "))
            num2 = int(input("Введіть друге число: "))
            rez = num1 - num2
            print(f'{num1} - {num2} = {rez}\n')
        elif choice == 3:
            num1 = int(input("Введіть перше число: "))
            num2 = int(input("Введіть друге число: "))
            rez = num1 * num2
            print(f'{num1} * {num2} = {rez}\n')
        elif choice == 4:
            num1 = int(input("Введіть перше число: "))
            num2 = int(input("Введіть друге число: "))
            if num2 != 0:
                rez = num1 / num2
                print(f'{num1} / {num2} = {rez}\n')
            else:
                raise ZeroDivisionError
        elif choice == 5:
            print("Bye!")
            exit = True
        else:
            print('Помилка! Не правильний вибір.')

except ValueError:
    print("\nПомилка! Введіть числа!.")
except ZeroDivisionError:
    print("\nПомилка! Ділення на 0.")