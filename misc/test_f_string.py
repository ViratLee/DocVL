#f-strings are faster than both %-formatting and str.format().
print(f'{8+1}') #74
print(f"{2 * 37}") #74

def to_lowercase(input):
    return input.lower()

name = "John Doe"
print(f"{to_lowercase(name)} is funny.") #john doe is funny.
print(f"{name.lower()} is funny.")#john doe is funny.

from comedian import Comedian
new_comedian = Comedian("Eric", "Idle", "74")
print(f"{new_comedian}")#Eric Idle is 74.
# use conversion flag !r:
print(f"{new_comedian!r}")#Eric Idle is 74. Surprise!

name = "Eric"
profession = "comedian"
affiliation = "Monty Python"
message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"You were in {affiliation}."
)

print(message) #'Hi Eric. You are a comedian. You were in Monty Python.'

message = f"Hi {name}. " \
          f"You are a {profession}. " \
          f"You were in {affiliation}."
print(message) #'Hi Eric. You are a comedian. You were in Monty Python.'

message = f"""
    Hi {name}. 
    You are a {profession}. 
    You were in {affiliation}.
"""
print(message)
    # Hi Eric.
    # You are a comedian.
    # You were in Monty Python.

print(f"{'Eric Idle'}")#Eric Idle
print(f'{"Eric Idle"}')#Eric Idle
print(f"""Eric Idle""")#Eric Idle
print(f'''Eric Idle''')#Eric Idle
name = "Eric"
age = 40
print(f"The \"comedian\" is {name}, aged {age}.")#The "comedian" is Eric, aged 40.

eric_comedian = {'name': 'Eric Idle', 'age': 74}
print(f"The comedian is {eric_comedian['name']}, aged {eric_comedian['age']}.")#The comedian is Eric Idle, aged 74.
#f'The comedian is {comedian['name']}, aged {comedian['age']}.'  #SyntaxError: invalid syntax

print(f"{{74}}")#{74}
print(f"{{{74}}}")#{74}
print(f"{{{{74}}}}")#{{74}}
#you can’t use backslashes to escape in the expression part of an f-string:
#f"{\"Eric Idle\"}"#SyntaxError: invalid syntax, 

#not include comments using the # symbol. 
#f"Eric is {2 * 37 #Oh my!}."  f-string expression part cannot include '#'