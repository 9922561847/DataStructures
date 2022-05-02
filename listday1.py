""" Write a Python program to sum all the items in a list """
x = [1,2,3,4]


def add_values_in_list(x):
    result = 0
    for ele in x:
        result += ele
    return result

print("sum of all numbers in list",add_values_in_list(x))
x = [2,2]
res = 0
result2 = [res:= res+ele for ele in x]
print("Hi",result2)

total = 0
print('Checking',[ total :=total + x for x in [1, 2, 3, 4, 5]])
# total = 15
