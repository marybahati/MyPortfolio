Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def subtraction(a,b)
SyntaxError: invalid syntax
>>> def hello():
	print('hello james, you are 19 years old')

	
>>> hello()
hello james, you are 19 years old
>>> def age('james',2000):
	answer=('hello {} you are {} old'.format('james',2019-2000))
	
SyntaxError: invalid syntax
>>> def age("james",2000):
	answer=('hello {} you are {} old'.format("james",2019-2000))
	
SyntaxError: invalid syntax
>>> def age(james,2000):
	answer=('hello {} you are {} old'.format('james',2019-2000))
	
SyntaxError: invalid syntax
>>> def age(noon,yob):
	age=2019-2000
	print('Hello {},you are {} years old.'.format(noon,age))

	
>>> age
<function age at 0x02EDC618>
>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

9
>>> print(age)
<function age at 0x02EDC618>
>>> print()

>>> def age(name,yob):
	x=2019-2000
	print('Hello {},you are {} years old.'.format(noon,age))

	
>>> def age(name,yob):
	x=2019-yob
	print('Hello {},you are {} years old.'.format(noon,x))

	
>>> age(noon,x)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    age(noon,x)
NameError: name 'noon' is not defined
>>> age(noon,2000)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    age(noon,2000)
NameError: name 'noon' is not defined
>>> age(noon,2000)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    age(noon,2000)
NameError: name 'noon' is not defined
>>> def squares(numbers):
	for number in numbers:
		print(number*number)

		
>>> def squares(numbers):
	for number in numbers:
		print(number*number)
		x=[1,2,3,4,5]
		y=[100,200,300,400]

		
>>> squares(x)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    squares(x)
NameError: name 'x' is not defined
>>> def squares(numbers):
	for number in numbers:
		print(number*number)

		
>>> x=[1,2,3,4,5]
>>> y=[100,200,300,400]
>>> squares(x)
1
4
9
16
25
>>> squares(y)
10000
40000
90000
160000
>>> age('noon',2000)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    age('noon',2000)
  File "<pyshell#31>", line 3, in age
    print('Hello {},you are {} years old.'.format(noon,x))
NameError: name 'noon' is not defined
>>> def age(name,yob):
	x=2019-yob
	print('Hello {},you are {} years old.'.format(name,x))

	
>>> age('noon',2000)
Hello noon,you are 19 years old.
>>> def squares(numbers):
	a=[]
	for number in numbers:
		s=number*number
		a.append(s)

		
>>> return a
SyntaxError: 'return' outside function
>>> def squares(numbers):
	a=[]
	for number in numbers:
		x=number*number
		a.append(x)

		
>>> return a
SyntaxError: 'return' outside function
>>> def squares(numbers):
	a=[]
	for number in numbers:
		s=number*number
		a.append(s)

		
>>> def squares(numbers):
	a=[]
	for number in numbers:
		s=number*number
		a.append(s)
	return a

>>> s=[1,2,3,4,5]
>>> a
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> def squares(numbers):
	a=[]
	for number in numbers:
		s=number*number
		a.append(s)
	return a

>>> x=[1,2,3,4,5]
>>> y=[100,200,300,400]
>>> squares(x)
[1, 4, 9, 16, 25]
>>> squares(y)
[10000, 40000, 90000, 160000]
>>> def squares(numbers):
	a=[]
	for number in numbers:
		s=number*10
		a.append(s)
	return a

>>> x=[1,2,3,4,5]
>>> y=[100,200,300,400]
>>> squares(x)
[10, 20, 30, 40, 50]
>>> squares(y)
[1000, 2000, 3000, 4000]
>>> def tens(numbers):
	a=[]
	for number in numbers:
		s=number*10
		a.append(s)
	return a

>>> x=[1,2,3,4,5]
>>> y=[100,200,300,400]
>>> tens(x)
[10, 20, 30, 40, 50]
>>> tens(y)
[1000, 2000, 3000, 4000]
>>>  
