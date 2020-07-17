import random
random_x=random.randint(1,20)
nambe=int(input("Введіть шукане число   "))
while nambe!=random_x:
    if nambe==random_x:
       
        break
    elif nambe>random_x:
        print("Ви ввели завелике число спробуйте ще")
        nambe=int(input("Введіть шукане число   "))
        
    else:
        print("Ви ввели замале число спробуйте ще")
        nambe=int(input("Введіть шукане число   "))
       
print("Вітаю Ви перемогли")