import array as arr
""" simple array creation"""
a = arr.array('i',[1,2,3,4])

for i in range(0,4):
    print(a[i],end="")

""" Adding elements to array """
a = arr.array('i',[1,2,3])
a.insert(0,4)
print("a",a)

#array with float

b = arr.array('d',[2.4,3.2,4.3])

b.insert(3, 3.3)
c = arr.array('d',[2.4,3.2,4.3])
c.append(4.4)
print(b)
print(c)
#difference between append & insert when we do append it will add value at the end. when we do insert we can add that value in desired position by passing index value.a
""" Accessing elements of array """
print("accessing elements from array",b[0])

""" Removing elements from Array """
print("removing element using pop",a.pop(2))
print("after removing",a)
