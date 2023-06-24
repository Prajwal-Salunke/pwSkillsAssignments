"""
# Q1.create one variable for different dataTypes

a="this is a string"    #String dataType

b=[10,12,15]            #List dataType

c=22.22                 #Float dataType

d=("apple",22,33.33)    #Tuple dataType



# Q2.Data types of variable

var1='' --> String

var2='[DS,ML,Python]'  --> String

var3=['DS','ML','Python']  -->List

var4= 1  --> Integer



# Q3.Use of following with Example

1.  /  --> Use to get exact division of two numbers.
        Ex. 15/4 = 3.75
            25/2 = 12.5

2.  %  --> Use to calculate remainder/quotient of a division
        Ex. 4 % 2 = 0
            15 % 4 = 3

3.  // --> Use to calculate floor division of numbers
        Ex. 33//6 = 5  (as 33/6 = 5.5 and base/floor of  5.5 is 5)
            13//5 = 2  (as 13/5 = 2.6 and base/floor of  2.6 is 2)

4.  ** --> Use to calculate nth power of a given number or multiply the number with given times
        Ex. 2**3 = 2*2*2 = 27
            4**2 = 4*4 = 16


"""

# Q4.List of len(10)

list1 = ["Google", 2, 55.5, '78', "DSA", 1, "&", 0, "asa", 99]
print("The length of the list1 is ", len(list1))
for items in list1:
    print(items, type(items))

# Q5.if A is purely divisible by B

A = int(input("Enter the number A:- "))
B = int(input("Enter the number B:- "))
if A % B == 0:
    print(f"{A} is purely divisible by {B} ")
    while A % B == 0:
        print(f"{A} is {int(A / B)} times divisible by {B}")
        break
else:
    print(f"{A} is NOT purely divisible by {B} ")

# Q6. Divisible by 3

list2 = []
for i in range(25, 51):
    list2.append(i)

for j in list2:
    if j % 3 == 0:
        print(f"{j} is divisible by 3 ")
    else:
        print(f"{j} is NOT divisible by 3 ")

# Q7. MUTABLE & IMMUTABLE Data types
"""
Mutable Data types :- LIST , SET , Dictionary
    
    In these data types ,we can change(add/delete) the value.
    Example :- 
"""
list3 = ["apple", "rose", 2, 5]
print("Original List :- ", list3)
list3[1] = "banana"  # "rose" is changed with "banana"
print("Mutable List:- ", list3)

"""
Immutable data types :- String , Tuple

    The value associated with these data types can not be changed  once set. We can not add/delete or update the values
    Example:-

string1="Python"
string1[2]= "l"    # NOT POSSIBLE ...Error will occurred at this line

tuple1=(5,8,66,0)
tuple1.append(1)    # NOT POSSIBLE ...Error will occurred at this line
"""
