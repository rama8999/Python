Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list
a=[2,5,6,"python",6+9j,True,False]
print(a)
[2, 5, 6, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=5
type(b)
<class 'int'>
c=[5]
type(c)
<class 'list'>
a=["python","java","c","c++"]
a.append("DSA")
a
['python', 'java', 'c', 'c++', 'DSA']
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
a
['python', 'java', 'c', 'c++', 'DSA', ['ml', 'ai']]
#extend
a=["ml","ai","ds"]
a.extend(["c","c++","python"])
a
['ml', 'ai', 'ds', 'c', 'c++', 'python']
#insert
b.insert(1,"vzg")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    b.insert(1,"vzg")
AttributeError: 'int' object has no attribute 'insert'
b=["vja","hyd"]
b.insert(1,"vzg")
b
['vja', 'vzg', 'hyd']
#index
a=["black","red","pink","white"]
a.index["white"]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.index["white"]
TypeError: 'builtin_function_or_method' object is not subscriptable
a.index("white")
3
a.copy()
['black', 'red', 'pink', 'white']
#copy
b=a.copy()
b
['black', 'red', 'pink', 'white']
b.count("pink")
1
#sort
a=["grapes","apple","mango","banana"]
a.sort()
a
['apple', 'banana', 'grapes', 'mango']
b=[8,6,0,3,6,1,2,20]
b.sort()
b
[0, 1, 2, 3, 6, 6, 8, 20]
#reverse
a=[7,8,9,10,20,30,40,50]
a.reverse()
a
[50, 40, 30, 20, 10, 9, 8, 7]
b=["java","html","css"]
b.reverse()
b
['css', 'html', 'java']
#pop
a=["c","c++","ml","ai"]
a.pop()
'ai'
a
['c', 'c++', 'ml']
a.pop("c++")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.pop("c++")
TypeError: 'str' object cannot be interpreted as an integer
>>> a.pop(1)
'c++'
>>> a
['c', 'ml']
>>> #remove()
>>> a.remove("ml")
>>> a
['c']
>>> a=["pooja","priya","prince","sweety']
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> a=["pooja","priya","prince","sweety"]
...    
>>> len(a)
...    
4
>>> b="pooja"
...    
>>> len(b)
...    
5
>>> c=["pooja"]
...    
>>> len(c)
...    
1
>>> a.clear()
...    
>>> a
...    
[]
>>> b=[]
...    
>>> b.append("hi")
...    
>>> b
...    
['hi']
