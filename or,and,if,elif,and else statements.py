Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for x in range(0,10):
	if x%3==0:
		print(x)

		
0
3
6
9
>>> for x in range(0,10):
	if x%3!=0:
		print(x)

		
1
2
4
5
7
8
>>> for x in range(0,10):
	if x%3==0:
		print("{} is divisible by 3".format(x))
	else:
		print("{} is not divisible by 3".format(x))

		
0 is divisible by 3
1 is not divisible by 3
2 is not divisible by 3
3 is divisible by 3
4 is not divisible by 3
5 is not divisible by 3
6 is divisible by 3
7 is not divisible by 3
8 is not divisible by 3
9 is divisible by 3
>>> for x in range(0,20):
	if x%3==0:
		print("{} is divisible by 3".format(x))
	elif x%5==0:
		print("{} is divisible by 5".format(x))
	else:
		print("{} is divisible by 3 or 5".format(x))

		
0 is divisible by 3
1 is divisible by 3 or 5
2 is divisible by 3 or 5
3 is divisible by 3
4 is divisible by 3 or 5
5 is divisible by 5
6 is divisible by 3
7 is divisible by 3 or 5
8 is divisible by 3 or 5
9 is divisible by 3
10 is divisible by 5
11 is divisible by 3 or 5
12 is divisible by 3
13 is divisible by 3 or 5
14 is divisible by 3 or 5
15 is divisible by 3
16 is divisible by 3 or 5
17 is divisible by 3 or 5
18 is divisible by 3
19 is divisible by 3 or 5
>>> for x in range(0,100):
	if x%7==0:
		print(x)

		
0
7
14
21
28
35
42
49
56
63
70
77
84
91
98
>>> for x in range(0,100):
	if x%7==0:
		print("{} is divisible 7".format(x))

		
0 is divisible 7
7 is divisible 7
14 is divisible 7
21 is divisible 7
28 is divisible 7
35 is divisible 7
42 is divisible 7
49 is divisible 7
56 is divisible 7
63 is divisible 7
70 is divisible 7
77 is divisible 7
84 is divisible 7
91 is divisible 7
98 is divisible 7
>>> for x in range(0,20):
	if x%3==0 and x%5==0:
		print(x)

		
0
15
>>> for x in range(0,20):
	if x%3==0 or x%5==0:
		print(x)

		
0
3
5
6
9
10
12
15
18
>>> true and true
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    true and true
NameError: name 'true' is not defined
>>> true and false
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    true and false
NameError: name 'true' is not defined
>>> True and True
True
>>> True and False
False
>>> False and False
False
>>> False and True
False
>>> True or False
True
>>> True or True
True
>>> False or False
False
>>> False or True
True
>>> 
