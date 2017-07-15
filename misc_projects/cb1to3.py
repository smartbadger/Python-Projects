Python 2.7.1 (r271:86832, Nov 27 2010, 18:30:46) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 3 + 4
7
>>> 3
3
>>> 
>>> "Python is really cool!"
'Python is really cool!'
>>>  name = "Connor Bailes"
 
  File "<pyshell#4>", line 1
    name = "Connor Bailes"
   ^
IndentationError: unexpected indent
>>> name

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> name = "Connor Bailes"
>>> name
'Connor Bailes'
>>> "Hi there" + name
'Hi thereConnor Bailes'
>>> "Hi there " + name
'Hi there Connor Bailes'
>>> print "Hi there"
Hi there
>>> print "Hi there", name
Hi there Connor Bailes
>>> name = input("Enter your name: ")
Enter your name: connor

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    name = input("Enter your name: ")
  File "<string>", line 1, in <module>
NameError: name 'connor' is not defined
>>> name = raw_input("Enter your Name: ")
Enter your Name: Connor
>>> name
'Connor'
>>> print name
Connor
>>> first = input("Enter the first number: ")
Enter the first number: 12
>>> second = input("Enter the second number: ")
Enter the second number: 3
>>> print "The sum is", first + second
The sum is 15


