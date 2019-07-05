Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> customer1={"name":"sharon","balance":400}
>>> customer2={"name":"eva","balance":2500}
>>> customer3={"name":"mercy","balance":300}
>>> customer4={"name":"mary","balance":5500}
>>> customer5={"name":"noon","balance":4400}
>>> customers
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    customers
NameError: name 'customers' is not defined
>>> customer
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    customer
NameError: name 'customer' is not defined
>>> customers=[customer1,customer2,customer3,customer4,customer5]
>>> customers
[{'name': 'sharon', 'balance': 400}, {'name': 'eva', 'balance': 2500}, {'name': 'mercy', 'balance': 300}, {'name': 'mary', 'balance': 5500}, {'name': 'noon', 'balance': 4400}]
>>> for customer in customers:
	sms="Hi{},your balance is {}".format(customer["name"],customer["balance"])

	
>>> print(sms)
Hinoon,your balance is 4400
>>> >>> for customer in customers:
	sms="Hi {},your balance is {}".format(customer["name"],customer["balance"])
	
SyntaxError: invalid syntax
>>> for customer in customers:
	sms="Hi {},your balance is {}".format(customer["name"],customer["balance"])

	
>>> print(sms)
Hi noon,your balance is 4400
>>> >>> for customer in customers:
	sms="Hi{},your balance is {}".format(customer["name"],customer["balance"])
	
SyntaxError: invalid syntax
>>> for customer in customers:
	sms="Hi{},your balance is {}".format(customer["name"],customer["balance"])
	print(sms)

	
Hisharon,your balance is 400
Hieva,your balance is 2500
Himercy,your balance is 300
Himary,your balance is 5500
Hinoon,your balance is 4400
>>> >>> for customer in customers:
	sms="Hi{},your balance is {}".format(customer["name"],customer["balance"])
	
SyntaxError: invalid syntax
>>> for customer in customers:
	sms="Hi {},your balance is {}".format(customer["name"],customer["balance"])
	print(sms)

	
Hi sharon,your balance is 400
Hi eva,your balance is 2500
Hi mercy,your balance is 300
Hi mary,your balance is 5500
Hi noon,your balance is 4400
>>> 
