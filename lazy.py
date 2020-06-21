# For easy (lazy) documenting of python scripts #

# Author: Pratiksha Jain
# Created On: 21.06.20

#-------------------------------#
# Import required: Standard library
import os
from shutil import copyfile

# Path of Python file to be read; put path without extension
name_of_file = 'ADAKNG'

# File copied and renamed to txt(readable)
copyfile('%s.py'%(name_of_file), '%s_copy.py'%(name_of_file))
os.rename('%s_copy.py'%(name_of_file), '%s.txt'%(name_of_file))

inputfile = open('%s.txt'%(name_of_file))

# File to be put in 
outputfile = open('Document.txt','a')
outputfile.write('DOCUMENT FOR %s.py\n\n'%(name_of_file))
# For multiline comments
stack = False

for line in inputfile:
    line = line.strip()
    if line=='':
        pass
    elif line.startswith('for'):
        outputfile.write('for loop\n')
    elif line.startswith("while"):
        outputfile.write('while loop\n')
    elif line.startswith('def'):
        outputfile.write('function\n')
    elif line.startswith("#"):
        outputfile.write(line+'\n')
    elif line.startswith("try"):
        outputfile.write('try block\n')
    elif line.startswith("except"):
        outputfile.write('except block\n')
    elif line.startswith("if"):
        outputfile.write('if block\n')
    elif line.startswith("else"):
        outputfile.write('else block\n')
    elif line.startswith("elif"):
        outputfile.write('elif block\n')
    elif line.startswith("\'\'\'"):
        if stack==False:
            outputfile.write('MultiLineComment:\n')
            stack = True
        else:
            outputfile.write('MultiLineComment End\n')
            stack = False
    elif stack==True:
        outputfile.write(line+'\n')
    else:
        pass

    


outputfile.close()
inputfile.close()