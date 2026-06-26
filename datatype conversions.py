Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype conversions
#int
int(6)
6
int(4.5)
4
int("python")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("python")
ValueError: invalid literal for int() with base 10: 'python'
int(3+9j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(3+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(6)
6.0
float(6.66)
6.66
float("python")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("python")
ValueError: could not convert string to float: 'python'
float(3+9j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(3+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#string
str(7)
'7'
str(3.07)
'3.07'
str("python")
'python'
>>> str(3+8j)
'(3+8j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(56)
(56+0j)
>>> complex(3.66)
(3.66+0j)
>>> complex("python")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    complex("python")
ValueError: complex() arg is a malformed string
>>> complex(6i+7j)
SyntaxError: invalid decimal literal
>>> complex(7+3j)
(7+3j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #boolean
>>> bool(56)
True
>>> bool(8.99)
True
>>> bool("python")
True
>>> bool(7+9j)
True
>>> bool(True)
True
>>> bool(False)
False
>>> bool(1)
True
>>> bool(0)
False
