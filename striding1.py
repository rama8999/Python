Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#striding
a="Data Science"
a[::]
'Data Science'
a[::1]
'Data Science'
 a[::2]
 
SyntaxError: unexpected indent
a[::2]
'Dt cec'
>>> b="cloud computing"
>>> b[::5]
'c u'
>>> b[::4]
'cdmi'
>>> b[::8]
'cm'
>>> b[2:]
'oud computing'
>>> b[:9]
'cloud com'
>>> b[3:11]
'ud compu'
>>> b[::2]
'codcmuig'
>>> b[::6]
'cci'
>>> c="machine learning"
>>> c[1:9:2]
'ahn '
>>> c[3:14:2]
'hn eri'
>>> c[5:15:4]
'nei'
>>> a[2:12:3]
'tSee'
>>> c[2:12:3]
'cnlr'
>>> a[0:10:1]
'Data Scien'
>>> c[0:10:1]
'machine le'
>>> #negative striding
>>> d="python course"
>>> d[-1:-10:-2]
'ero o'
>>> d[-5:-11:-3]
'on'
>>> d[-3:-13:-4]
'r t'
