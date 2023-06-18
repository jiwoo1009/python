Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> rainbow='빨주노초파남보'
>>> a=7
>>> print(rainbow)
빨주노초파남보
>>> print(rainbow,a,"가지색")
빨주노초파남보 7 가지색
>>> print( rainbow , "무지개"")
       
SyntaxError: EOL while scanning string literal
>>> print( rainbow , "무지개")
빨주노초파남보 무지개
>>> print(rainbow[2])
노
>>> print( rainbow [1 : 3])
주노
>>> print(rainbow[2 : ])
노초파남보
>>> print(rainbow[[4])
      
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> print(rainbow[4: ])
파남보
>>> print(rainbow[-1])
보
>>> print(rainbow[-2])
남
>>> print("노" in rainbow)
True
>>> a="빨강"
>>> a
'빨강'
>>> b="파랑"
>>> b
'파랑'
>>>  c="노랑"
 
SyntaxError: unexpected indent
>>> c="노랑"
>>> c
'노랑'
>>> print(a,b,c, sep="-")
빨강-파랑-노랑
>>> print(a,b,c sep="/n")
SyntaxError: invalid syntax
>>> print( a, b, c, sep="\n")
빨강
파랑
노랑
>>> 