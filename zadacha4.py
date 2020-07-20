n=int(input("Введіть початкове значення факторіала    "))

k=int(input("Введіть крок факторіала  "))

m=int(input("Введіть кінцеве значення факторіала    "))

if n>=0 and m>=0 and n<m and k>0:
    print("Ви ввели коректні дані")
    factorial = n
    for i in range(n+1,m+1,k):
        factorial *= i
        print(factorial)

else:
    print('Ви ввели не  коректні дані')

        
 

 



