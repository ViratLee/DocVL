user_input = input('Please key number:')
number = int(user_input)
prime = True
for i in range(2, number+1):
   n = number/2
   p = number % i
   prime = False if p == 0 else True
   if prime == False:
       break
   m = True if i<n  else False
   #print(f'{i}, {n}, {p}, {m}, {prime}')
   if m == False:
       break
       prime = False if p == 0 else True
       if prime == False:
           break
print(f'{number} is prime ? {prime}')