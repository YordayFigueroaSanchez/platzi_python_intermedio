def divisors(num):
    divisors = []
    for i in range(1,num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input('Ingrese un numero : '))
        if num < 0:
            raise ValueError('El numero debe ser positivo.')
        print(divisors(num))
        print("End program")
    except ValueError as ve:
        print(ve)
    
if __name__ == '__main__':
    run()