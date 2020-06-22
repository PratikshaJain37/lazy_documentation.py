# Sample python script for lazy.py (Document_This)

# Author: Pratiksha Jain
# Created On: 21.06.20

#-------------------------------#


# This is a For Loop:
bar = [x for x in range(10)] 
for x in bar:
    print(x)

# This is a While Loop:
i = 0
while i<5:
    print(i)
    i += 1

# I am defining functions:
def FooBar():
    print("function1")
def foo_bar():
    print('function2')

# I am calling a function here:
FooBar()

# This is a Try/Except/Else Block:
try:
    print(bar)
except:
    print('Hello')
else:
    print('World')

# This is a If/Elif/Else Block:
string = "Hello World"
if string == "Hello World":
    print(string)
elif string == "FooBar":
    print(string)
else:
    pass

# This is a Multiline Comment:
'''
Hello 
World
'''
# This is another Multiline Comment:
""" 
Foo
Bar
"""

#-------------------------------#
