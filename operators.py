Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #arthematic
>>> a=2
>>> b=4
>>> print(a+b)
6
>>> print(a-b)
-2
>>> print(a*b)
8
>>> print(a//b)
0
>>> print(a/b)
0.5
>>> print(a**b)
16
>>> print(a%b)
2
>>> #assignmennt
>>> a=3
>>> b=6
>>> print(a+=b)
SyntaxError: invalid syntax
>>> a+b
9
>>> a+=b
>>> b
6
>>> a
9
>>> b+=a
>>> b
15
>>> print(b)
15
>>> b-=10
>>> b
5
>>> b*=a
>>> b
45
#comparision
a=4
b=9
a<b
True
b>a
True
a>b
False
b<a
False
a!=b
True
a==b
False
a<=b
True
b>=a
True
a>=b
False
b<=a
False
#logical operators
a=3
b=6
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a!=b or a==b
True
a<=b or b<=a
True
not True
False
not False
True
#identity
a=4
type(a) is int
True
type(a) is not int
False
b=6.7
type(b) is float
True
type(b) is str
False
c="python"
type(c) is str
True
type(c) is float
False
type(c) is not str
False
d=7+3j
type(d) is complex
True
type(d) is str
False
#membershio
a=3,4,5,6,7,8,9
8 in a
True
20 in a
False
20 not in a
True
9 in a
True
