Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a,b,c=2,3,4
print(a,b,c)
2 3 4
a,b,c=2,3,4,5,6,7,8
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a,b,c=2,3,4,5,6,7,8
ValueError: too many values to unpack (expected 3, got 7)
a,b,c=(3,4,5)
print(a,b,c)
3 4 5
first name="rama"
SyntaxError: invalid syntax
first_name="rama"
print(first_name)
rama
firstname="rama"
print(firstname)
rama
a=4,b=9
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=4;b=9
>>> print(a+b)
13
>>> a,b=2,3
>>> print(a+b)
5
>>> a,b,c=10
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
>>> a=b=c=10
>>> print(a,b,c)
10 10 10
>>> fname="rama"
>>> lname="devi"
>>> print(fname+lname)
ramadevi
>>> print(fname+" "+lname)
rama devi
>>> print(fname,lname)
rama devi
>>> name="rama"
>>> print(name)
rama
>>> NAME="rama"
>>> print(NAME)
rama
>>> Name="rama"
>>> print(Name)
rama
>>> a=4
>>> print(a)
4
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
