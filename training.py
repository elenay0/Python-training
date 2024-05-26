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

# fruits= ['apple', 'banana', 'cherry','date']

# for i in range(len(fruits)):
#     print(fruits[i])

# # def fun()
# #     print('welcome to GFG')

# # fun()

# def fun():
#     print('welcome to GFG')

# fun()


# def add(num1: int, num2: int) -> int:
#     '''Add two numbers'''
#     num3= num1+num2
#     return num3
# num1, num2= 5, 15
# ans= add(num1, num2)
# print(f'The addition of {num1} and {num2} is {ans}.')


# def is_prime(n):
#     if n in [2,3]:
#         return True
#     if (n==1) or (n%2==0):
#         return False
#     r=3
#     while r*r<=n:
#         if n%r==0:
#             return False
#         r+=2
#     return True
# print(is_prime(78), is_prime(79))

# def evenOdd(x):
#     if (x%2==0):
#         print('even')
#     else:
#         print('odd')

# evenOdd(2)
# evenOdd(5)

# def myFun(x, y=50):
#     print("x: ", x)
#     print("y: ", y)

# myFun(10)

# def student(firstname, lastname):
#     print(firstname, lastname)

# student(firstname='Elena', lastname='yordanova')
# student(lastname='yordanova', firstname='Elena')


# def nameAge(name, age):
#     print('Hi, I am ', name)
#     print('I am', age , 'years old')

# print('Case 1:')
# nameAge('Elena', 18)

# print('\nCase 2:')
# nameAge(18,'Elena')

# def myFun(*argv):
#     for arg in argv:
#         print(arg)

# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print('%s==%s' % (key, value))

# myFun(first='Geeks', mid='for', last='Geeks')


# def evenOdd(x):
#     """Function to check if the number is even or odd"""
#     if (x%2==0):
#         print('even')
#     else:
#         print('odd')
# print(evenOdd.__doc__)

# def f1():
#     s= 'I love Geeks for Geeks '
#     def f2():
#         print(s)
#     f2()

# f1()

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(4))

# def square_value(num):
#     '''This function returns the square value of the entered number'''
#     return num**2

# print(square_value(5))
# print(square_value(-4))

# def myFun(x):
#     x[0]=20

# list=[10, 11, 12, 13, 14, 15]
# myFun(list)
# print(list)

# def myFun(x):
#     x= [20,30,40]

# list=[10, 11, 12, 13, 14, 15]
# myFun(list)
# print(list)

# def myFun(x):
#     x=20

# x=10
# myFun(x)
# print(x)

# def swap(x, y):
#     temp = x
#     x=y
#     y=temp

# x=2
# y=3
# swap(x,y)
# print(x)
# print(y)


#Syntax: Class Definition

# class classname:
    #statement

#Syntax: Object Definition

# obj= classname()
# print(obj.atrr)

# Demonstation of instantiation:


# class Dog:

#     attr1='mammal'
#     attr2='dog'

#     def fun(self):
#         print("I'm a", self.attr1)
#         print("I'm a", self.attr2)

# Roger=Dog()

# print(Roger.attr1)
# Roger.fun()


# class GFG:
#     def __init__(self, name, company):
#         self.name=name
#         self.company = company
    
#     def show(self):
#         print("Hello my name is" + self.name + "and I" + "work in" + self.company +".")

# obj= GFG ( "John", "GeeksforGeeks")
# obj.show()


# class GFG:
#     def __init__(somename, name, company):
#         somename.name = name
#         somename.company = company

#     def show(somename):
#         print("Hello my name is " + somename.name + " and I work in " + somename.company+ ".")

# obj = GFG ("John", "GeeksforGeeks")
# obj.show()


# class Person:
#     def __init__(self, name):
#         self.name= name
    
#     def say_hi(self):
#         print('Hello, my name is', self.name)
        
# p= Person('Nikhil')
# p.say_hi()


# class GFG:
#     def __init__(self, name, company):
#         self.name=name
#         self.company=company

#     def __str__ (self):
#         return f"My name is {self.name} and I work in {self.company}."
    
# my_obj= GFG ("John", "GeeksforGeeks")
# print(my_obj)


# class Dog:

#     animal= "dog"

#     def __init__(self, breed, color):
#         self.breed = breed
#         self.color = color

# Rodger = Dog("Pug", "brown")
# Buzo = Dog("Vulldog", "black")

# print("Rodger details:")
# print("Rodger is a", Rodger.animal)
# print("Breed:", Rodger.breed)
# print("Color:", Rodger.color)

# print("\nBuzo details:")
# print("Buzo is a", Buzo.animal)
# print("Breed:", Buzo.breed)
# print("Color", Buzo.color)


# class Dog:
#     animal ='Dog'
#     def __init__(self, breed):
       
#         self.breed = breed
   
#     def setColor(self, color):
#         self.color= color
   
#     def getColor(self):
#         return self.color


# Rodger= Dog ("pug")
# Rodger.setColor("brown")
# print(Rodger.getColor())

    
# class Person:
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age
# person1 = Person("Maria Popova", 25)
# person2 = Person("Ivan Petrov", 30)

# print(person1.name)
# print(person1.age)
# print(person2.name)
# print(person2.age)


# class Person:
#     name = "Anonymous"
#     age = 100

# maria = Person()
# petar = Person()

# print(maria.name, maria.age)
# print(petar.name, petar.age)
# print(Person.name, Person.age)

# class Person:
#     count=0

#     def __init__(self, name):
#         self.name = name
#         Person.count += 1

# maria = Person("Maria Popova")
# petar = Person("Petar Ivanov")
# ivan = Person("Ivan Petrov")

# print(Person.count)


# class Person:
#     count=0

#     def __init__(self, name):
#         self.name =  name
#         Person.count += 1

# maria = Person("Maria Popova")

# print(maria.__dict__)

