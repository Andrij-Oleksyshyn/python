def type_num(num):
    if type(num)== int or type(num)== float:
        return abs(num)
    else:
        return "Nope"

a=type_num("ЩО це таке")

print(a)