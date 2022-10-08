# 3. Задайте последовательность чисел.
#    Напишите программу, которая выведет список
#    неповторяющихся элементов исходной последовательности
#    в том же порядке.
# in 7   >>  out [4, 5, 3, 3, 4, 1, 2] [5, 1, 2]
# in -1  >>  out  Negative value of the number of numbers! []
# in 10  >>  out [4, 4, 5, 5, 6, 2, 3, 0, 9, 4] [6, 2, 3, 0, 9]

from random import randrange

def list_nums(count: int):
    if count < 0:
        print("Ввели отрцатльное число")
        return []

    list_nums = [randrange(1, 10) for i in range(count)]
    return list_nums

def nonrepeating_elements(all_list: list): 
    
    list_of_unique_numbers = []
    for i in range(len(all_list)):
        flag = 1
        for j in range(len(all_list)):
            if all_list[i] == all_list[j] and i != j:
                flag = 0
                break
        if flag:
            list_of_unique_numbers.append(all_list[i])       
    print(list_of_unique_numbers)


all_list = list_nums(int(input("Введите колличество чисел: ")))
#all_list = [4, 5, 3, 3, 4, 1, 2]
print(all_list)
nonrepeating_elements(all_list)
#all_list = [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
#print(all_list)
#nonrepeating_elements(all_list)

#################################################

from random import randrange


def list_rand_nums(count: int):
    if count < 0:
        print("Negative value of the number of numbers!")
        return []

    list_nums = []
    for i in range(count):
        list_nums.append(randrange(count))

    return list_nums


def uniq_el(list_nums: list):
    result = []
    my_dict = {}.fromkeys(list_nums, 0)

    for i in list_nums:
        my_dict[i] += 1

    for k in my_dict:
        if my_dict[k] == 1:
            result.append(k)

    return result


all_list = list_rand_nums(int(input("Number of numbers: ")))
print(all_list)
print(uniq_el(all_list))