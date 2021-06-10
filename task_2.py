class Wrong(Exception):
    pass
try:
    price = float(input('Enter call price (hrn): '))
    if price <= 0:
        raise Wrong()
    duration = float(input('Enter call duration (minutes): '))
    if duration <=0:
        raise Wrong()
    cost = price * duration
    print(cost)
except ValueError :
    print("Error! Enter number")
except Wrong:
    print("Введіть додатнє число!")