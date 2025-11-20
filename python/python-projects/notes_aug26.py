print ("hello world!")

# Comments
# Single line comment
'''
Multi line comment
'''

# x=10
# y=1
# z=9 ('command /' or 'ctrl /' will auto comment)

# Variables (no data types or semi colons)
x = 10
y = 10.1
x = "hello"
print(x)

# Math Operators
x = 100
y = 10
z = x / y # division converts the number into a float
z = int(z) # cast into integer
# z = x // y double forward slash uses floor division and removes decimals
print(z)

min_val = min(10,1)
print(min_val)

raised = 2**4 # Powers
print(raised)
raised = pow(2,4)
print(raised)

# Conditional Statements
if x < 0:
    print("negative")

else:
    print("positive")

if x < 0 and y < 0:
    print("both negative")

if x < 0 or y < 0:
    print("one is negative")

if x<0:
    print("negative")
elif y < 0: # else if python version
    print("negative")
else:
    print("positive")