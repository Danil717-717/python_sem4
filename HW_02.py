# 2. Задайте натуральное число N. Напишите программу,
#    которая составит список простых множителей числа N
# in 54   >> out  [2, 3, 3, 3]
# in 9990 >> out  [2, 3, 3, 3, 5, 37]
# in 650  >> out  [2, 5, 5, 13]

#def prime_factors(n):
#    i = 2
#    while n > 1:
#        while n % i == 0:
#            print(i, end=' ')
#            n //= i
#        i += 1

#prime_factors(int(input("Введите натуральное число: ")))        

#####################################

def find_prime_nums(num):
    pr_fact = []
    di = 2
    while num > 1:
        if num % di == 0:
            pr_fact.append(di)
            num //= di
        else:
            di += 1
    return pr_fact


# 650, 9990, 364, 54
print(find_prime_nums(int(input())))