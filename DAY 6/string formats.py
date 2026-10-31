Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # concatination
>>> s = "Python "
>>> s
'Python '
>>> t = "Programming"
>>> t
'Programming'
>>> s+t
'Python Programming'
>>> s*#
SyntaxError: invalid syntax
>>> s*3
'Python Python Python '
>>> t*3
'ProgrammingProgrammingProgramming'
>>> 
>>> s+t*3
'Python ProgrammingProgrammingProgramming'
>>> s*3 + t*3
'Python Python Python ProgrammingProgrammingProgramming'
>>> '*'*3
'***'
>>> "0"*100
'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
>>> "*"*2000
'********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************'
>>> # indexing
>>> s = "Python java flask fastapi mysql"
>>> s
'Python java flask fastapi mysql'
>>> s[0]
'P'
\
>>> s[-1]
'l'
>>> s[-12]
'a'
>>> s[6]
' '
>>> s[6]
' '
>>> s[7]
'j'
>>> s[3,4]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s[3,4]
TypeError: string indices must be integers
>>> # slicing
>>> s
'Python java flask fastapi mysql'
>>> s[0: 6:1]
'Python'
>>> s[7:11:1]
'java'
>>> s[7:11:2]
'jv'
>>> s[7:11:-1]
''
>>> s[24:]
'i mysql'
>>> s[s:23]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s[s:23]
TypeError: slice indices must be integers or None or have an __index__ method
>>> s[:24]
'Python java flask fastap'
>>> s[::-1]
'lqsym ipatsaf ksalf avaj nohtyP'
>>> s[18:23]
'fasta'
>>> s[18:25]
'fastapi'
>>> s[::2]
'Pto aafakfsaimsl'
>>> s[3::1]
'hon java flask fastapi mysql'
>>> s[::1]
'Python java flask fastapi mysql'
>>> s[::-1]
'lqsym ipatsaf ksalf avaj nohtyP'
>>> s[5::-1]
'nohtyP'
>>> s
'Python java flask fastapi mysql'
>>> # membership
>>> s
'Python java flask fastapi mysql'
>>> 'java' in s
True
>>> 'c++' in s
False
>>> 'c++' not in s
True
>>> 'Python' in s
True
>>> 'python' in s
False
>>> # string methods
>>> chr(41)
')'
>>> s
'Python java flask fastapi mysql'
>>> len(s)
31
>>> ord('a')
97
>>> ord('b')
98
>>> ord('|')
124
>>> max(s)
'y'
>>> min(s)
' '
>>> sorted(s)
[' ', ' ', ' ', ' ', 'P', 'a', 'a', 'a', 'a', 'a', 'f', 'f', 'h', 'i', 'j', 'k', 'l', 'l', 'm', 'n', 'o', 'p', 'q', 's', 's', 's', 't', 't', 'v', 'y', 'y']
>>> ## the main methods we have are len,ord,chr,max,min,sorted
>>> s.title()
'Python Java Flask Fastapi Mysql'
>>> s.capitalize
<built-in method capitalize of str object at 0x000002276BD19300>
>>> s.capitalize()
'Python java flask fastapi mysql'
>>> s.swapcase()
'pYTHON JAVA FLASK FASTAPI MYSQL'
>>> s.lower()
'python java flask fastapi mysql'
>>> s.upper()
'PYTHON JAVA FLASK FASTAPI MYSQL'
>>> # string formating
>>> s ='python'
>>> s
'python'
>>> s.center()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s.center()
TypeError: center expected at least 1 argument, got 0
>>> s.center(20,'*')
'*******python*******'
>>> s.center(100,'#')
'###############################################python###############################################'
>>> s.center(40,' ')
'                 python                 '
>>> s.ljust(20,'*')
'python**************'
>>> s.rjust(20,'*')
'**************python'
>>> 1
1
>>> 0001
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> '1'.zfill(5)
'00001'
>>> '124'.zfill(5)
'00124'
>>> # finding methods
>>> s
'python'
>>> s = 'python java flask fastapi mysql'
>>> s
'python java flask fastapi mysql'
>>> s.find('y')
1
>>> s.rfind('y')
27
>>> s.index('a')
8
>>> s.index('f')
12
>>> s.rindex('v')
9
>>> s.count()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    s.count()
TypeError: count() takes at least 1 argument (0 given)
>>> s.count('a')
5
>>> s.count('z')
0
>>> s.index('z')
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> s = '             python      coding               '
>>> s
'             python      coding               '
>>> s.strip()
'python      coding'
>>> s.rstrip()
'             python      coding'
>>> s.lstrip()
'python      coding               '
>>> s = 'python java flask fastapi mysql'
>>> s
'python java flask fastapi mysql'
>>> s.replace('a','*')
'python j*v* fl*sk f*st*pi mysql'
>>> s.maketrans('apks','12345')
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    s.maketrans('apks','12345')
ValueError: the first two maketrans arguments must have equal length
>>> s.maketrans('apkqs','12345')
{97: 49, 112: 50, 107: 51, 113: 52, 115: 53}
>>> s.translate(s.maketrans('apkqs','12345'))
'2ython j1v1 fl153 f15t12i my54l'
>>> s.translate(s.maketrans('aeiou','*****'))
'pyth*n j*v* fl*sk f*st*p* mysql'
>>> 