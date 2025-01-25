#1.
numbers=[1,2,3,4,5]
list1=[]
def square():
	for i in numbers:  
		x=i**2
		list1.append(x)
	print(f"The square of list is : {list1}")
square()
print()
#or
def square(a):
	return a**2
obj=map(square,[1,2,3,4,5])
print("The square of list is : ",list(obj))
print()
#or
obj=map(lambda a:a**2,[1,2,3,4,5])
print("The square of list is : ",list(obj))
print()
#2
Numbers=[1,-1,2,-2,3,-3,4,-4,5,-5]
List1=[]
def filter_positive():
	for i in Numbers:
		if i>=0:
			List1.append(i)
	print(f"Positive numbers are : {List1}")
filter_positive()
print()
#or
Numbers=[1,-1,2,-2,3,-3,4,-4,5,-5]
def filter_positive(a):
	return a>=0
obj=filter(filter_positive,Numbers)
print("Positive numbers are : ",list(obj))
print()
#or
obj=filter(lambda a:a>=0,[1,-1,2,-2,3,-3,4,-4,5,-5])
print("Postive numbers are : ",list(obj))
print()
#3.
def factorial_number(n):
	if n<0:
		return "Enter a valid number"
	elif (n==0 or n==1):
		return 1
	else:
		return (n*factorial_number(n-1))
num=int(input("Enter a number : "))
b=factorial_number(num)
print(f"{num} factorial number is: {b}")
print()
#or
from functools import reduce
num=int(input("enter number:"))
obj=reduce(lambda i,j:i*j,range(1,num+1))
print(f"{num} factorial number is : {obj}")
print()
#4.
def count_vowels(name):
	count=0
	vowels ='aeiou'
	for i in name:
		if i in vowels:
			count+=1
	print(count)
name=input("Enter your name : ").lower()
count_vowels(name)
print()
#or
from functools import reduce
name=input("Enter your name : ").lower()
vowels='aeiou'
obj=reduce(lambda i,j:i+(1 if j in vowels else 0),name,0)
print(obj)