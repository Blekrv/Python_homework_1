class NoMoney(Exception):
    pass

try:
    startMoney = int(input('Введіть суму в грн.')) 
    while True:    
        if startMoney <= 0:
            raise NoMoney()
            break
        print(startMoney)
        choset  = int(input('\n1.Американські гірки - 15 грн.\n 2.Кімната страху - 30 грн \n 3.Акваленд - 55 грн\n 0.Вихід \n Виберіть атракціон :'))

        if choset == 1:
            if startMoney >= 15:
                startMoney -= 15
        elif choset == 2:
            if startMoney >= 30:
                startMoney -= 30
        elif choset == 3:
            if startMoney >= 45:
                startMoney -= 55
        elif choset == 0:
            print('Exit')
            break
    
except ValueError as e:
    print(e)
except NoMoney as e:
    print('No money no honey')

