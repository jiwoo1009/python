Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================================== RESTART: Shell ==================================
>>> candies=["딸기맛" , "레몬맛" , "수박맛" , "우유맛"]
>>> print(candies)
['딸기맛', '레몬맛', '수박맛', '우유맛']
>>> print(candies[1])
레몬맛
>>> print(candies[10])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(candies[10])
IndexError: list index out of range
>>> print(candies[-1])
우유맛
>>> print(candies[1:3])
['레몬맛', '수박맛']
>>> candies.append("유자맛")
>>> print(candies)
['딸기맛', '레몬맛', '수박맛', '우유맛', '유자맛']
>>> candies.insert(1. "자두맛" )
SyntaxError: invalid syntax
>>> candies.insert(1, "자두맛" )
>>> print(candies)
['딸기맛', '자두맛', '레몬맛', '수박맛', '우유맛', '유자맛']
>>> candies.remove("우유맛")
>>> print(candies)
['딸기맛', '자두맛', '레몬맛', '수박맛', '유자맛']
>>> del candies[1]
>>> print(candies)
['딸기맛', '레몬맛', '수박맛', '유자맛']
>>> del candies[1:3]
>>> print(candies)
['딸기맛', '유자맛']
>>> candies.sort( )
>>> print(candies)
['딸기맛', '유자맛']
>>> candies.sort(reserve=true)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    candies.sort(reserve=true)
NameError: name 'true' is not defined
>>> candies.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    candies.sort(reverse=true)
NameError: name 'true' is not defined
>>> candies.reverse( )
>>> print (candies)
['유자맛', '딸기맛']
>>> a=[1,2,3,4,5,6,7,8,9,10]
>>> sum(a)
55
>>> max(a)
10
>>> min(a)
1
>>> 