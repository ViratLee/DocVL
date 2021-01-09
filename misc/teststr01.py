some_string = None

if not some_string:
	print('some_string is None.')
some_string = ''
if not some_string:
	print('some_string is empty.')
some_number = 0
if not some_number:
	print('some_number is 0.')

some_string = 'string 1'
if some_string:
	print('some_string is {}'.format(some_string))

some_number = 1
if some_number:
	print('some_number is {}'.format(some_number))	

flag = True
if flag:
	print("PEP 8 Style Guide prefers this pattern")

if flag is True:
    print("PEP 8 Style Guide abhors this pattern")

not_specific_type = 1
if not_specific_type is True: # this will also check not_specific_type is Boolean type and True.
	print("not_specific_type is Boolean and True") #  so it will not show this print if not_specific_type is not Boolean
else:
    print("not_specific_type is not Boolean") # it will show this print

boolean_type = True
if boolean_type is True: # this will also check boolean_type is Boolean type and True,
	print("boolean_type is Boolean and True") # it will show this print 
else:
    print("boolean_type is not Boolean or not True") 