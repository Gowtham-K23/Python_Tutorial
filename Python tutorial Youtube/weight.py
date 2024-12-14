weight = input("Weight:")
unit = input("L(bs) or K(g)")

if unit == 'L' or unit == 'l':
    print(int(weight)*0.45)
if unit == 'K' or unit == 'k':
    print(int(weight)//0.45)
