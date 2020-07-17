f1 = 1
f2 = 1

fib=[f1,f2]

n=100



i=0


while i < n - 2:      
    fib_sum = f1 + f2
    f1 = f2
    f2 = fib_sum
    
    fib.append(f2) 
    
    i = i + 1
   
 

print(fib)
fibnam=int(input("Введіть число для оцінки   "))

x=fibnam in fib

print(x)

if x == False:

    print("Введіть повторно число для перевірки")
  
else:

    print("Дане число має оцінку 100")



    



