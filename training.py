# print("Hello world!\nHello world!")

# print ("Hello Elena")

# input("What is your name?")
# print("Hello "+ input("What is your name?"))

# print( 3/2 )

# x = 5
# int(x)
# type(x)

# a=5
# print(type(a))

# b= 5.0
# print(type(b))

# c= 2+4j
# print("Type of c:", type(c))

# string1= 'Welcome to the Geeks World'
# print("String with the use of Single Quotes:")
# print(string1)
# string1= "I'm a Geek"
# print("\nString with the use of Double Quotes:")
# print(string1)
# print(type(string1))
# string1='''I'm a Geek and I live in a world of "Geeks"'''
# print("String with the use of Triple Quotes:")
# print(string1)
# print(type(string1))

# string1 = '''Geeks
# For
# Life'''
# print("\nCreating a multiline String:")
# print(string1)

# string1= "GeeksForGeeks"
# print("Initial String:")
# print(string1)
# print("\nFirst character of string is:")
# print(string1[0])
# print("\nLast character of String is:")
# print(string1[-1])


# list= []
# print("Initial blank list: ")
# print(list)
# list= ['GeeksForGeeks']
# print("\nList with the use of string: ")
# print(list)
# list= ["Geeks", "For", "Geeks"]
# print("\nList containing multiple values: ")
# print(list [0])
# print(list[2])
# list= [['Geeks', 'For', 'Geeks']]
# print("\nMulti-Dimensional List: ")
# print(list)

# a=9
# b=5
# c=9

# print(a==b)
# print(a==c)

# a=9
# b=5
# c=9

# print(a!=b)
# print(a!=c)

# a=9
# b=5

# print(a>b)
# print(b>a)

# a=9
# b=5

# print(a<b)
# print(b<a)

# a=9
# b=5
# c=9

# print(a>=b)
# print(a>=c)
# print(b>=a)

# a=9
# b=5
# c=9

# print(a<=b)
# print(a<=c)
# print(b<=a)

# a=5

# print(1<a<10)
# print(10>a<=9)
# print(5!=a>4)
# print(a<10<a*10==50)


# a=10
# b=10
# c=-10

# if a>0 and b>0:
#     print("The numbers are greater than 0")
# if a>0 and b>0 and c>0:
#     print("The numbers are greater than 0")
# else:
#     print("Atleast one number is not greater than 0")

# a=10
# b=12
# c=0
# if a and b and c:
#     print("All the numbers have boolean values as True")
# else:
#     print("Atleast one number has boolean values as False")

# a=10
# b=-10
# c=0
# if a>0 or b>0:
#     print("Either of the number is greater than 0")
# else:
#     print("No number is greater than 0")
# if b>0 or c>0:
#     print("Either of the number is greater than 0")
# else:
#     print("No number is greater than 0")

# a=10
# b=12
# c=0
# if a or b or c:
#     print("Atleast one number has boolean value as True")
# else:
#     print("All the numbers have boolean value as False")

# a=10
# if not a:
#     print("Boolean value of a is True")
# if not (a%3==0 or a%5==0):
#     print("10 is not divisible by either 3 or 5")
# else:
#     print("10 is divisible by either 3 or 5")

# def order(x):
#     print("Method called for value:", x)
#     return True if x>0 else False
# a=order
# b=order
# c=order
# if a(-1) or b(5) or c(10):
#     print("Atleast one of the numbers is positive")

# user_name=""
# user_age=15
# user_country= "BG" 

# print(user_age>18 and user_country=="BG")
# print(user_age>18 or user_country=="BG")

# print(user_name and "Anonymous")
# print(user_name or "***Anonymous***")


# x=42
# if x%2==0:
#     print("{} is an even number!".format(x))

# if False:
#     print("1")
#     print("2")
# print("3")

# x=41

# if x%2==0:
#     print('{} is an even number!'.format(x))
# else:
#     print('{} is an odd number!'.format(x))


# print(5/5)
# print(10/2)
# print(-10/2)
# print(20.0/2)

# print(10//3)
# print(-5//2)
# print(5.0//2)
# print(-5.0//2)

# i=10

# if(i>15):
#     print('10 is less than 15')
# print('I am Not in if')

# i=20
# if (i<15):
#     print('i is smaller than 15')
#     print('i am in if Block') 
# else:
#     print('i is greater than 15')
#     print('i am in else Block')
# print('i am not in if and not in else Block')

# def digitSum(n):
#     dsum=0
#     for ele in str(n):
#         dsum+=int(ele)
#     return dsum

# list=[367,111,562,945,6726,873]

# newlist=[digitSum(i) for i in list if i &1]

# print(newlist)

# count=0
# while(count<3):
#     count=count+1
#     print('Hello Geek')

# i=1
# while i<6:
#     print(i)
#     i+=1

#print the numbers from 10 to 1
# i=10
# while i>=1:
#     print(i)

# user_name=input("Enter a name, please:")
# user_name_lenght=len(user_name)

# while user_name_lenght<3:
#     user_name=input('Enter a name(atleast 3 symbols):')
#     user_name_lenght=len(user_name)

# print('Thank you, {}!'.format(user_name))

# i=1
# total_sum=0
# while i<=100:
#     total_sum+=i
#     i+=1
# print('total_sum=', total_sum)

# count=0
# while (count<3):
#     count=count+1
#     print('Hello Geek')
# else:
#     print('In Else Block')

# count=0
# while(count==0):
#     print()

# total_sum= sum(range(1,101))
# print('total_sum=', total_sum)

# for s in "ada":
#     print(s.capitalize())

###loop on list items:
# for item in [1,2,3]:
#     print(item, end=',')

###loop on tuple items:
# for item in(10, 'December', 1985):
#     print(item, end=',')

###loop on string items:
# for item in 'byron':
#     print(item, end=',')

###loop on range items:
# for item in range(1,3):
#     print(item,end=',')


# for n in range(1,6):
#     print(n, end=',')

# total_sum=0
# for n in range(1,11):
#     total_sum+=n

# print(f'total_sum={total_sum}')

### FOR loop with Dictionary
# person={'name': 'John', 'age':'30', 'country': 'UK'}
# for key, value in person.items():
#     print(f'{key}: {value}')

# val='Geeks'
# print(f'{val}for{val} is a portal for {val}')

# name= 'Tushar'
# age= 23
# print(f'Hello, My name is {name} and I am {age} years old.')

##### Print today's date with help of datetime library

# import datetime

# today=datetime.datetime.today()
# print(f'{today:%B %d, %Y}')

# english=78
# maths=56
# hindi=85

# print(f'Ram got total marks {english+maths+hindi} out of 300')

# colors=['red', 'green', 'blue']
# for index, color in enumerate(colors):
#     print(f'{index}:{color}')

# for i in [1,2,3]:
#     for j in 'abv':
#         print(f'{i}:{j}', end=',')
#     print()

# matrix= [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in matrix:
#     for element in row:
#         print(element, end='')
#     print()

# n=4
# for i in range(0,n):
#     print(i)

# print('List iteration')
# l= ['geeks', 'for', 'geeks']
# for i in l:
#     print(i)
# print('\nTuple iteration')
# t=('geeks', 'for','geeks')
# for i in t:
#     print(i)
# print('\nString iteration')
# s= 'Geeks'
# for i in s:
#     print(i)
# print('\nDictionary iteration')
# d=dict()
# d['xyz']=123
# d['abc']=345
# for i in d:
#     print('%s %d' %(i,d[i]))
# print('\nSet iteration')
# set1= {1,2,3,4,5,6}
# for i in set1:
#     print(i)

# list= ['geeks', 'for', 'geeks']
# for index in range(len(list)):
#     print(list[index])

# list=['geeks','for','geeks']
# for index in range(len(list)):
#     print(list[index])
# else:
#     print('Inside else block')

# from __future__ import print_function
# for i in range(1,5):
#     for j in range(i):
#         print(i, end='')
#     print() 


###Example of Python range (stop)
# for i in range(6):
#     print(i, end='')
# print()

####Example of Python range (start, stop)

# for i in range(5,20):
#     print(i, end='')

####Example of Python range (start, stop, step)
# for i in range(0,10,2):
#     print(i, end='')
#     print()

# for i in range(0, 30, 4):
#     print(i, end='')
# print()

# for i in range (25,2,-2):
#     print(i, end='')

# for in range(3.3):
#     print(i)

####Python range() with More Examples
###Concatenation of two range() functions using itertools chain() method

# from itertools import chain

# print('Concatenating the result')
# res=chain(range(5), range(10,20,2))

# for i in res:
#     print(i, end='')

# ele= range(10)[0]
# print('First element:', ele)

# ele= range(10)[-1]
# print('\nLast element', ele)

# ele= range(10)[4]
# print('\nFifth element', ele)

fruits= ['apple', 'banana', 'cherry','date']

for i in range(len(fruits)):
    print(fruits[i])