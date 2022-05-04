""" python code to find largest number in list"""
sample_list = [1,2,3]
# max = 0
# for i in sample_list:
#     if i > max:
#         max = i
   
# print("This is largest number:",max)

def find_largest_num(sample_list):
    max_num = 0
    for i in sample_list:
        if i > max_num:
            max_num = i
    return ("This is max Number in list",max_num)

a = find_largest_num(sample_list)
# print(a)

""" python code to find smallest number in list"""

sample_list1= [1,2,3,-1,0]
# min = 0
# for i in sample_list1:
#     if i < min:
#         min = i
# print("min value in list",min)

# def find_smallest_num(sample_list1):
#     min = 0
#     for num in sample_list1:
#         if num < min:
#             min = num
#     return ("Smallest number in list is : ",min)

# a = find_smallest_num(sample_list1)
# print(a)

""" Write a Python program to count the number of strings
 where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2 """

testList = ['abc', 'xyz', 'aba', '1221','aa','aa']
# n = len(testList)
# count =0
# for i in testList:
#     if len(i) > 2:
#         if i[0]==i[-1]:
#             count +=1
# print(count)

def find_string_length(testList):
    count = 0
    for string in testList:
        if len(string) > 2:
            if string[0] == string[-1]:
                count +=1

    return "count of string is : ",count

# a = find_string_length(testList)
# print(a)

""" 
Write a Python program to get a list, 
sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] 

"""
sort_list1= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# print(sort_list[0][1])

def last(n):
    return n[-1]

def sort_list(tuples):
    return sorted(tuples,key=last)

a = sort_list(sort_list1)
# print(a)

""" Write a Python program to remove duplicates from a list.  """

x = [1,2,4,3,4,4]
c = set(x)
# print(list(c))

""" how to reverse list """

x = [1,2,4]

# y = x[::-1]
# print(y)
