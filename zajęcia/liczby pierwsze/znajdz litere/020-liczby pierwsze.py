def is_prime(n):
    for i in range(2,n):
        if n %i==0:
            return False
        return  True

try:
    number = int(input('podaj liczbę:'))
    if is_prime(number):
        print(f'{number} liczba pierwsza')
    else:
        print(f'{number} nie liczba pierwsza')
except:
    print('BŁĄD')
