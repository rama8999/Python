Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a='vijayawada'
a[0]
'v'
>>> a[1]
'i'
>>> a[2]
'j'
>>> a[3]
'a'
>>> a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'vijaya'
>>> a="I am learning python course"
>>> a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
>>> a[5]+a[6]+a[7]+a[8]+a[9]
'learn'
>>> a[21]+a[22]+a[23]+a[24]+a[25]+a[26]
'course'
>>> b="Time is very precious"
>>> b[13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]+b[20]
'precious'
>>> b[8]+b[9]+b[10]+b[11]
'very'
>>> b[0]+b[1]+b[2]+b[3]
'Time'
>>> c="simple is better than complex "
>>> c[29]+c[28]+c[27]+c[26]+c[25]+c[24]
' xelpm'
>>> c[-29]+c[-28]+c[-27]+c[-26]+c[-25]+c[-24]
'imple '
>>> c="simple is better than complex"
>>> c[-29]+c[-28]+c[-27]+c[-26]+c[-25]+c[-24]
'simple'
>>> c[-12]+c[-11]+c[-10]+c[-9]
'than'
>>> c[-7]+c[-6]+c[-5]+c[-4]+c[-3]+c[-2]+c[-1]
'complex'
>>> c[-19]+c[-18]+c[-17]+c[-16]+c[-15]+c[-14]
'better'
>>> d="i love python"
>>> d[-11]+d[-10]+d[-9]+d[-8]
'love'
>>> d[-6]+d[-5]+d[-4]+d[-3]+d[-2]+d[-1]
'python'
