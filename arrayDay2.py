""" Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes. Go to the editor
Sample Output:
1
3
5
7
9
Access first three items individually
1
3
5

"""
import array as arr

x = arr.array('i',(1,3,5,7,9))
y = x[0:3]
#print("first three elements of array",y)
############################################################
""" 
Write a Python program to append a new item to the end of the array. Go to the editor
Sample Output:
Original array: array('i', [1, 3, 5, 7, 9])
Append 11 at the end of the array:
New array: array('i', [1, 3, 5, 7, 9, 11])
"""
a = arr.array('i', [1, 3, 5, 7, 9])
b = 11
a.append(b) # using append we can add value at the very end of array
#a.insert(-1, b)    insert is adding value before the last number so append is better approch to add number at the very end of array
#print(a)
############################################################
"""
Write a Python program to reverse the order of the items in the array. Go to the editor
Sample Output
Original array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])
Reverse the order of the items:
array('i', [3, 9, 1, 7, 3, 5, 3, 1])
"""
#Approch 1
c = arr.array('i', [1, 3, 5, 3, 7, 1, 9, 3])
# d = c[::-1]
# print("printing reverse of given array",d)

#Approch 2 
c.reverse()
#print("using reverse method reversing array",c)

#Approch 3 
reversed(c) #using reversed method we can iterate the values as it create iterate wheras reverse only reverse the array & paste it back.

#print("reversing array using reversed method",c)

