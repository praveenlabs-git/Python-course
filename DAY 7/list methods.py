Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> # string methods
>>> s = 'Python programming'
>>> s
'Python programming'
>>> s.startswith('Python')
True
>>> s.endswith('mming')
True
>>> 's'.islower()
True
>>> 'S'.isupper()
True
>>> s.startswith('python')
False
>>> 'code'.isalpha()
True
>>> 'code23'.isalpha()
False
>>> 'code123'.isalnum
<built-in method isalnum of str object at 0x000001EF064E2770>
>>> 'code13'.isalnum()
True
>>> 'code'.isalnum()
True
>>> 'gaming '.isalnum()
False
>>> s
'Python programming'
>>> s.istitle()
False
>>> s.istitle()
False
>>> 'myvar'.isidentifier()
True
\
>>> '   '.isspace()
True
>>> '        praveen'.isspace()
False
>>> '   '.isspace()
True
>>> '1234i'.issecial
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    '1234i'.issecial
AttributeError: 'str' object has no attribute 'issecial'
>>> '123'.isdecimal()
True
>>> '1234'.isdigit()
True
>>> '12334'.isnumeric
<built-in method isnumeric of str object at 0x000001EF064EE470>
>>> '123334'.isnumeric()
True
>>> '''
hello
world welcome
s
'''
'\nhello\nworld welcome\ns\n'
>>> s
'Python programming'
>>> s = '''
hello world
welcome
'''
4
>>> 
>>> 'a,b,c,d'.split('-')
['a,b,c,d']
>>> 'a,b,c,d'.split()
['a,b,c,d']
>>> 'a,b,c,d'.split('--')
['a,b,c,d']
>>> 'a-b-c-d'.split()
['a-b-c-d']
>>> 'a-b-c-d'.rsplit('-')
['a', 'b', 'c', 'd']
>>> 'a-b-c-d'.rsplit('-',2)
['a-b', 'c', 'd']
>>> s.splitlines()
['', 'hello world', 'welcome']
>>> l = ['a','b','c','d']
\
>>> '-'.join(l)
'a-b-c-d'
>>> '@'.join(l)
'a@b@c@d'
>>> '*'.join(l)
'a*b*c*d'
>>> '_'.join(l)
'a_b_c_d'
>>> 'Python.py'.partition('.')
('Python', '.', 'py')
>>> 'Python.py.jio'.partition('.')
('Python', '.', 'py.jio')
>>> 'Python.py.jio'.rpartition('.')
('Python.py', '.', 'jio')
>>> # encode and decode
>>>  s = 'Hello World'
 
SyntaxError: unexpected indent
>>> s
'\nhello world\nwelcome\n'
>>> s = "Hello World"
>>> s
'Hello World'
>>> s.endode()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s.endode()
AttributeError: 'str' object has no attribute 'endode'
>>> s.encode()
b'Hello World'
>>> t.encode
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    t.encode
NameError: name 't' is not defined
>>> b'Hello World'.decode()
'Hello World'
>>> l = [1,2,3,4,4,3]
>>> l
[1, 2, 3, 4, 4, 3]
>>> type(l)
<class 'list'>
>>> # list is represented in the square braces
>>> #it is muttable
>>> # it is ordered
>>> # it allows duplicates
>>> # it is hetrogenous'
>>> # it is dynamic
>>> l = [1,1,1,1,1,1,1]
>>> l
[1, 1, 1, 1, 1, 1, 1]
>>> l = [1,13.234,2+1j,'str',[1,2,4],(1,1,3),{13,12,42},{1:2,2:3},True,None]
>>> l
[1, 13.234, (2+1j), 'str', [1, 2, 4], (1, 1, 3), {42, 12, 13}, {1: 2, 2: 3}, True, None]
>>> # cancantination,repeation,indexing,slicing,membership
>>> [1,2,4,4] + [4,5,8,9]
[1, 2, 4, 4, 4, 5, 8, 9]
>>> [1,2,3,4,5]*3
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> l = ['Python', 'mysql', 'java','c','aws','fastapi','flask']
>>> l
['Python', 'mysql', 'java', 'c', 'aws', 'fastapi', 'flask']
>>> l[2]
'java'
>>> l[:3]
['Python', 'mysql', 'java']
>>> l[::-1]
['flask', 'fastapi', 'aws', 'c', 'java', 'mysql', 'Python']
>>> l[1:4]
['mysql', 'java', 'c']
>>> l[1:5]
['mysql', 'java', 'c', 'aws']
>>> l[:-1:-4]
[]
>>> l
['Python', 'mysql', 'java', 'c', 'aws', 'fastapi', 'flask']
>>> 'Python' in l
True
>>> 'css' not in l
True
>>> 'node.js' in l
False
>>> 'c' in l
True
>>> [1,2,4,4] + [4,5,8,9]
[1, 2, 4, 4, 4, 5, 8, 9]
>>> 
>>> 
>>> 
>>> 
>>> l
['Python', 'mysql', 'java', 'c', 'aws', 'fastapi', 'flask']
>>> # method
>>> # len,sorted,min,max
>>> len(l)
7
>>> sorted(l)
['Python', 'aws', 'c', 'fastapi', 'flask', 'java', 'mysql']
>>> min(l)
'Python'
>>> max(l)
'mysql'
>>> l
['Python', 'mysql', 'java', 'c', 'aws', 'fastapi', 'flask']
>>> sorted(l)
['Python', 'aws', 'c', 'fastapi', 'flask', 'java', 'mysql']
>>> l = ['python','c','fastapi','flask','aws','myaql']
>>> l
['python', 'c', 'fastapi', 'flask', 'aws', 'myaql']
>>> sorted(l)
['aws', 'c', 'fastapi', 'flask', 'myaql', 'python']
>>> l[1]
'c'
>>> l[1] = 'html'
>>> l
['python', 'html', 'fastapi', 'flask', 'aws', 'myaql']
>>> l[2] = 'css'
\
>>> l
['python', 'html', 'css', 'flask', 'aws', 'myaql']
>>> id(l)
2126114778496
>>> l.append('java')
>>> l
['python', 'html', 'css', 'flask', 'aws', 'myaql', 'java']
>>> l.append('c++')
>>> l
['python', 'html', 'css', 'flask', 'aws', 'myaql', 'java', 'c++']
>>> l.extend([1,2,3,4,a,,b,c])
SyntaxError: invalid syntax
>>> l.extend([1,2,3,a,b,c])
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    l.extend([1,2,3,a,b,c])
NameError: name 'a' is not defined
>>> l.extend('[1,2,3,a,b,c]')
>>> l
['python', 'html', 'css', 'flask', 'aws', 'myaql', 'java', 'c++', '[', '1', ',', '2', ',', '3', ',', 'a', ',', 'b', ',', 'c', ']']
>>> l.pop(1,2,3,a,b,c)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    l.pop(1,2,3,a,b,c)
NameError: name 'a' is not defined
>>> l.pop('[1,2,3,a,b,c]')
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    l.pop('[1,2,3,a,b,c]')
TypeError: 'str' object cannot be interpreted as an integer
>>> l = 'python', 'html', 'css', 'flask', 'aws', 'myaql', 'java', 'c++'
\
>>> l
('python', 'html', 'css', 'flask', 'aws', 'myaql', 'java', 'c++')
>>> l.append('a')
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    l.append('a')
AttributeError: 'tuple' object has no attribute 'append'
>>> l
('python', 'html', 'css', 'flask', 'aws', 'myaql', 'java', 'c++')
>>> l.append('a')
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    l.append('a')
AttributeError: 'tuple' object has no attribute 'append'
>>> l = ['python', 'html', 'css', 'flask', 'aws', 'myaql', 'java', 'c++']
>>> l
['python', 'html', 'css', 'flask', 'aws', 'myaql', 'java', 'c++']
>>> l.append('a')
>>> l
['python', 'html', 'css', 'flask', 'aws', 'myaql', 'java', 'c++', 'a']
>>> l.insert(2,c)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    l.insert(2,c)
NameError: name 'c' is not defined
>>> l.insert(2,'c')
>>> l
['python', 'html', 'c', 'css', 'flask', 'aws', 'myaql', 'java', 'c++', 'a']
>>> id(l)
2126114596928
>>> 