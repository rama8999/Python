Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatypes
>>> a=10
>>> type(a)
<class 'int'>
>>> b=4.5
>>> type(b)
<class 'float'>
>>> c='code'
>>> type(c)
<class 'str'>
>>> d="codegnan"
>>> type(d)
<class 'str'>
>>> e='''course'''
>>> type(e)
<class 'str'>
>>> f=4+9j
>>> type(f)
<class 'complex'>
>>> g=9j
>>> type(g)
<class 'complex'>
>>> h=6j+7
>>> type(h)
<class 'complex'>
>>> i=7+9i
SyntaxError: invalid decimal literal
>>> j=True
>>> type(j)
<class 'bool'>
>>> k=False
>>> type(k)
<class 'bool'>
>>> l=true
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    l=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> m="True"
>>> type(m)
<class 'str'>
