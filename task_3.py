try:
    revolutions = float(input("Введіть кількість обертів Марсу: "))
    earthRevolutions = round(686 * revolutions / 365, 1)
    if revolutions <= 0:
        raise ValueError
    print(f'{revolutions} обертів Марсу = {earthRevolutions} обертів Землі')
except ValueError:
    print('\nПомилка! Введіть додатнє число!')