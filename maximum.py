my_list = [1,2,5,3,7,4,9,3]

def my_max(lst):
    max = lst[0]
    for item in lst: 
        if item > max: max = item
    return max

print(my_max(my_list))