fib1=int(input("Введіть перше число фібоначчі   "))

fib2=int(input("Введіть друге число фібоначчі   "))

fibmax=int(input("Введіть максимальне допустиме число   "))

fib=[fib1,fib2]

fibnext=fib1+fib2


while fibnext <= fibmax:

    fib.append(fibnext)
    
    fib1=fib2

    fib2=fibnext

    fibnext=fib1+fib2
print("Заданий проміжок значень-",fib)


