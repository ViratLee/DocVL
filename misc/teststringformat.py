str1 = 'C9999'
width = 10
border = '-'
print('{}'.format(str1))#C9999
print(f'{str1}')#C9999
print(f'{str1}'.center(width, border))#--C9999---
#print('{},{}'.format(str1))#IndexError: tuple index out of range