Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def hello():
	print('Hello Akirachix')

	
>>> hello()
Hello Akirachix
>>> def hello(name):
	print('hello {}'.format(name))

	
>>> hello(name)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    hello(name)
NameError: name 'name' is not defined
>>> print hello(name)
SyntaxError: invalid syntax
>>> hello('james)
	  
SyntaxError: EOL while scanning string literal
>>> hello('james')
	  
hello james
>>> hhello('aishe')
	  
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    hhello('aishe')
NameError: name 'hhello' is not defined
>>> hello('aisha')
	  
hello aisha
>>> def sum(a,b):
	  answer=a+b
	  return answer

	  
>>> sum()
	  
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    sum()
TypeError: sum() missing 2 required positional arguments: 'a' and 'b'
>>> sum(10,15)
	  
25
>>> sum(45+98)
	  
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    sum(45+98)
TypeError: sum() missing 1 required positional argument: 'b'
>>> sum(98,45)
	  
143
>>> sum(67,90)
	  
157
>>> 
