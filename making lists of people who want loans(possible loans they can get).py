Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> >>> customer1={"name":"sharon","balance":400}
>>> customer2={"name":"eva","balance":2500}
>>> customer3={"name":"mercy","balance":300}
>>> customer4={"name":"mary","balance":5500}
>>> customer5={"name":"noon","balance":4400}
SyntaxError: invalid syntax
>>> customer1={"name":"sharon","balance":400}
>>> customer2={"name":"eva","balance":2500}
>>> customer3={"name":"mercy","balance":300}
>>> customer4={"name":"mary","balance":5500}
>>> customer5={"name":"noon","balance":4400}
SyntaxError: multiple statements found while compiling a single statement
>>> customer1={"name":"sharon","balance":400}
>>>  customer2={"name":"eva","balance":2500}
SyntaxError: unexpected indent
>>> customer2={"name":"eva","balance":2500}
>>> customer3={"name":"mercy","balance":300}
>>> customer4={"name":"mary","balance":5500}
>>> customer5={"name":"noon","balance":4400}
>>> customers=[customer1,customer2,customer3,customer4,customer5]
>>> customers
[{'name': 'sharon', 'balance': 400}, {'name': 'eva', 'balance': 2500}, {'name': 'mercy', 'balance': 300}, {'name': 'mary', 'balance': 5500}, {'name': 'noon', 'balance': 4400}]
>>> for customer in customers:
	sms="Hi {},your balance is {}".format(customer["name"],customer["balance"])
	print(sms)

	
Hi sharon,your balance is 400
Hi eva,your balance is 2500
Hi mercy,your balance is 300
Hi mary,your balance is 5500
Hi noon,your balance is 4400
>>> for customer in customers:
	loan=customer["balance"]/2.9
	sms=" hello {}  your loan balance is {}".format(customer{"name"],customer[loan])
	
SyntaxError: invalid syntax
>>> for customer in customers:
	loan=customer["balance"]/2.9
	sms=" hello {}  your loan balance is {}".format(customer["name"],customer[loan])

	
Traceback (most recent call last):
  File "<pyshell#16>", line 3, in <module>
    sms=" hello {}  your loan balance is {}".format(customer["name"],customer[loan])
KeyError: 137.93103448275863
>>> for customer in customers:
	loan=customer["balance"]/2.9
	sms=" hello {}  your loan balance is {}".format(customer{"name"],[loan])
	
SyntaxError: invalid syntax
>>> for customer in customers:
	loan=customer["balance"]/2.9
	sms=" hello {}  your loan balance is {}".format(customer["name"],[loan])

	
>>> for customer in customers:
	loan=customer["balance"]/2.9
	sms=" hello {}  your loan balance is {}".format(customer["name"],[loan])
	print(sms)

	
 hello sharon  your loan balance is [137.93103448275863]
 hello eva  your loan balance is [862.0689655172414]
 hello mercy  your loan balance is [103.44827586206897]
 hello mary  your loan balance is [1896.5517241379312]
 hello noon  your loan balance is [1517.2413793103449]
>>> for customer in customers:
	loan=customer["balance"]/2.9
	sms=" hello {}  your loan balance is {}".format(customer["name"],loan)
	print(sms)

	
 hello sharon  your loan balance is 137.93103448275863
 hello eva  your loan balance is 862.0689655172414
 hello mercy  your loan balance is 103.44827586206897
 hello mary  your loan balance is 1896.5517241379312
 hello noon  your loan balance is 1517.2413793103449
>>> for customer in customers:
	loan=customer["balance"]//2.9
	sms=" hello {}  your loan balance is {}".format(customer["name"],loan)
	print(sms)

	
 hello sharon  your loan balance is 137.0
 hello eva  your loan balance is 862.0
 hello mercy  your loan balance is 103.0
 hello mary  your loan balance is 1896.0
 hello noon  your loan balance is 1517.0
>>> for x in range(0,10):
	if x%3==0:
		print(x)

		
0
3
6
9
>>> 
