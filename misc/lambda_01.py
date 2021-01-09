add_one = lambda x: x + 1
result = add_one(2)
print(result) # 3

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
your_name = full_name('john', 'legend')
print(your_name) # Full name: John Legend

#use lambda in higher-order function
high_ord_func = lambda x, func: x + func(x)
result3 = high_ord_func(2, lambda x: x * x)
print(result3)# 6
result4 = high_ord_func(2, lambda x: x + 3)
print(result4)# 7

##############################################
# In mathematics and computer science, a higher-order function is a function that does at least one of the following:
# takes one or more functions as arguments (i.e. procedural parameters),
# returns a function as its result.