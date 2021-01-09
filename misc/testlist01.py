my_list = list()

# Check if a list is empty by its length
if len(my_list) == 0:
    pass  # the list is empty

# Check if a list is empty by direct comparison
if my_list == []:
    pass  # the list is empty

# Check if a list is empty by its type flexibility **preferred method**
if not my_list:
    pass  # the list is empty