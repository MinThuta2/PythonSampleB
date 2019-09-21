#x = int(input("Please enter an integer: "))
#Please enter an integer: 
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

#x = int(input("Please enter an integer"))
#if x < 0:
#	x = 50
#	print('x is 50')
#elif x == 40;
#	print('x is 40')
#elif x == 30;
#	print('x is 30')
#else:
#	print('More')
#if x < 60:
#	print('x is greater than 50')
#	print('x is greater than 40')
#elif x == 30:
#	print('x is greater than 30')
#else:
#	print('More')

#x = int(input("Please enter an integer: "))
#if x > 40 and x < 75 :
#	print('Aged go to Bagan')
#elif x < 40 :
#	print('Young go to Beach')
#elif x < 10 :
#	print('Go to playground')
#else:
#	print('Unlisted')
x = int(input("Please enter a mark: "))
if x == 100 :
	print('Scholar')
elif x >= 70 and x < 100 :
	print('Distinction')
elif x >= 50 and x < 70 :
	print('Excellent')
elif x >= 40 and x < 50 :
	print('Pass Fail')
elif x < 40 and x >= 35 :
	j = 40 - x
	print('Mordation mark: ',j)
elif x <= 10 :
	print('Warnning')
words = ['cat', 'window', 'defenestrate', 'world']
for w in words[:] :
    if len(w) > 4 :
            words.insert(0,w)

words
['world', 'defenestrate', 'window', 'cat', 'window', 'defenestrate', 'world']
