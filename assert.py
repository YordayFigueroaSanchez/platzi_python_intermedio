def divisors(num):
    divisors = []
    for i in range(1,num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        str = input('Ingrese un numero : ')
        assert str.isnumeric(), 'entrada tiene que ser un numero'
        num = int(str)
        assert num >= 0, 'El numero debe ser positivo.'
        print(divisors(num))
        print("End program")
    except ValueError as ve:
        print('no pasa por aca')
    
if __name__ == '__main__':
    run()