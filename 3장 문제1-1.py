Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=6
>>> b-2
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    b-2
NameError: name 'b' is not defined
>>> a=6
>>> b=2
>>> print("a=" a)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("a=" a)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("a=",a)
a= 6
>>> print("b=",b)
b= 2
>>> print("몫= ", a/b)
몫=  3.0
>>> print("나머지=", a%b )
나머지= 0
