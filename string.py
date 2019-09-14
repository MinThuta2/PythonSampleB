>>> 5 * 'Hello' + 'Wold'
'HelloHelloHelloHelloHelloWold'
>>> "Hello" + str(3)
'Hello3'
>>> int("3") + 3
6
>>> x = "Programming"
>>> x[6]
'm'
>>> x[0]
'P'
>>> x[0:6]
'Progra'
>>> x[1:5]
'rogr'
>>> x[:7]
'Program'
>>> x[8:]
'ing'
>>> x[:]
'Programming'
>>> x[]
  File "<stdin>", line 1
    x[]
      ^
SyntaxError: invalid syntax
 x[-4]
'm'
 x[5:-4]
'am'
 x[-5:0]
''
 x = "programming"
 x[:3]
'pro'
 x[:3]+x[4:]
'proramming'
 x[:3] * 5
'propropropropro'
 x[:3] + " " * 5
'pro     '
 (x[:3] + " ") * 5
'pro pro pro pro pro '
 x[:3] *5 + " " *5
'propropropropro     '
 x = "programming"
 x[0]
'p'
 x[0] = 'Q'
x = "Programming"
x[0:4] + 'ram'
'Program'
x[0:5] + 'Python'
'ProgrPython'
x
'Programming'
len(x) + 4
15
len(x[5]) + 4
5
len(x[5:9]) + 4
8
word = [ 1, 3, 7, 9, 11, 13, 15 ]
word
[1, 3, 7, 9, 11, 13, 15]
word[5]
13
word = [1, , 5,7, 9, 11, 13, 15]
  File "<stdin>", line 1
    word = [1, , 5,7, 9, 11, 13, 15]
               ^
SyntaxError: invalid syntax
word = [1, 3, 5, 7, 9, 13, 15]
word
[1, 3, 5, 7, 9, 13, 15]
word[5:7]
[13, 15]
[1, 3, 5, 7, 9, 13, 15]
[1, 3, 5, 7, 9, 13, 15]
[13, 15]
[13, 15]
 word[4] = 10
word
[1, 3, 5, 7, 10, 13, 15]
 word = ['P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
 word[0] = Q
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Q' is not defined
 word[0] = 'Q'
 word
['Q', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
 word[:] = "Good"
 word
['G', 'o', 'o', 'd']
 word[2]
'o'
 word = [1, 3, 5, 7, 9, 11, 13, 15]
 word + word
[1, 3, 5, 7, 9, 11, 13, 15, 1, 3, 5, 7, 9, 11, 13, 15]
word[:] + [2, 4, 6, 8, 10]
[1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10]
a = a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]
c = ["A", "B", "C", "D", "E"]
x = [a,b,c]
