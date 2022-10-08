# 1. Вычислить число c заданной точностью d
#  in Enter a real number: 9
#     Enter the required accuracy '0.0001': 0.000001
#  out   9.000000

#  in Enter a real number: 8.98785
#    Enter the required accuracy '0.0001': 0.001
#  out   8.988

from decimal import Decimal

def num(number: str): 
    number = Decimal(number)
    accuracy = (str(input("Выбирите заданную точность (1.00 или 1.000 или 1...): "))) 
    number = number.quantize(Decimal(accuracy))
    print(number)

num(input("Введите число: "))

 
#number = Decimal("0.555678")
#print(number.quantize(Decimal("1.00")))       # 0.56
 
#number = Decimal("0.999")
#print(number.quantize(Decimal("1.00")))       # 1.00

############################################

#from decimal import Decimal


#def accuracy(num, acc):
#    number = Decimal(f"{num}")
#    return number.quantize(Decimal(f"{acc}"))


#print(accuracy(float(input("Enter a real number: ")), float(input("Enter the required accuracy 0.0001: "))))


# --------------------------------------- 2 вариант

#num = float(input('Enter a real number: '))

#_, accu = input("Enter the required accuracy '0.0001': ").split(".")
#print(f"{num:.{len(accu)}f}")