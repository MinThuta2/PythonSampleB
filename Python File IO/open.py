# f = open('test.txt','r')

# print(f.name)

# f.close()
# with open('test.txt','a') as g:

# 	g.write('This is line number 6'+"\n")

# 	print(g,end='')

with open('test.txt','r') as f:

	

	size_to_read = 500
	f_text = f.read(size_to_read)

	while len(f_text) > 0:
		print(f_text,end='')


	# for line in f:

	# 	print(line,end='')
	

	#f_text = f.readline() soloution for reading line
	#print(f_text,end='')
		
	# for i in f:
	# 	print(i,end='')

	# f_text = f.read(500)
	# print(f_text,end='')

	# f.write('This is line number 6'+"\n")
	# for line in f:
	# 	print(line,end='')

	# g = open('test.txt','a') 
	# i = g.write("\n"+'6.This is line number 6'+"\n")		
	# print(i,end='')

