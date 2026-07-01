Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
c=" "
len(c)
1
#count
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("t")
5
a.count("k")
2
a.count(" ")
3
count(a)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
#find a string
a="code"
a[1]
'o'
a.find("d")
2
a.find("e")
3
b="hello"
b.find("l")
2
b[2:4]
'll'
#escape sequences
#\n->new line
#\t->tab space
a="name\nmobile\tmailid\nclg"
print(a)
name
mobile	mailid
clg
b="name:rama\nmobileno:97036922979\tmailid:rama@gmail.com\nclg:SCET"
print(b)
name:rama
mobileno:97036922979	mailid:rama@gmail.com
clg:SCET
#replace()
a="eait until you suceed"
a.replace("eait","work")
'work until you suceed'
a
'eait until you suceed'
b="wait wait until you suceed"
b.replace("wait","work")
'work work until you suceed'
b.replace("wait","work",1)
'work wait until you suceed'
#lower()
b="HI"
b.lower()
'hi'
c="python"
c.upper(0)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    c.upper(0)
TypeError: str.upper() takes no arguments (1 given)
c[0].upper()
'P'
c.capitalize()
'Python'
a="python course"
a.title()
'Python Course'
c="i am in class"
c.title()
'I Am In Class'
#some cases
a="java"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
b="python course"
b.isalpha()
False
c="pythoncourse"
a.isalpha()
True
d=1234
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
d="1234"
d.isdigit()
True
e="pooja1234"
e.isalnum()
True
f="pooja@1234"
f.isalnum()
False
#
a="hello python"
a.startswith("h")
True
a.startswith("n")
False
#strip()
#strip(),rstrip()
a="                  pooja                 "
a.strip()
'pooja'
a.lstrip()
'pooja                 '
a.rstrip()
'                  pooja'
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am in vja"
b.split()
['i', 'am', 'in', 'vja']
c="codegnan"
c.split()
['codegnan']
#join()
a="vja hyd vzg"
"".join(a)
'vja hyd vzg'
b="vja","hyd","vzg"
"".join(b)
'vjahydvzg'
" ".join(b)
'vja hyd vzg'
"k".join(b)
'vjakhydkvzg'
#concatenationa
a="hello"
b="world"
print(a+b)
helloworld
helloworld
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    helloworld
NameError: name 'helloworld' is not defined
>>> print(a+" "+b)
hello world
>>> fname="rama"
>>> lname="velagala"
>>> print(fname+lname)
ramavelagala
>>> print(fname+" "+lname)
rama velagala
>>> print(fname.title()+" "+lname.title())
Rama Velagala
>>> print((fname+" "+lname).title())
Rama Velagala
>>> #formatting
>>> a=4
>>> b=8
>>> print(a+b)
12
>>> print("the sum is",a+b)
the sum is 12
>>> x="vja"
>>> print("city is",x)
city is vja
>>> #format method
>>> a='motu"
SyntaxError: unterminated string literal (detected at line 1)
>>> a="motu"
>>> b="patlu"
>>> print(hello",a+b)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> a="motu"
... b="patlu"
... print("hello",a+b)
...       
SyntaxError: multiple statements found while compiling a single statement
>>> print("hello",a+b)
...       
hello motupatlu
>>> print("hello {} {}".format(a,b))
...       
hello motu patlu
>>> print("hello {} hello {}".format(a,b))
      
hello motu hello patlu
#fstring
      
a="sita"
      
b="ram"
      
print(f"hello {a} {b}")
      
hello sita ram
print(f"hello {a}{b}")
      
hello sitaram
