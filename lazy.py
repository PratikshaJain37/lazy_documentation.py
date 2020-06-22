# For easy (lazy) documenting of python scripts #

# Author: Pratiksha Jain
# Created On: 21.06.20

#-------------------------------#

# Imports required (Standard library)
import os
from shutil import copyfile

#-------------------------------#

# Path of Python file to be read; put PATH without extension
name_of_file = 'ADAKNG'

# File copied and renamed to txt(readable)
copyfile('%s.py'%(name_of_file), '%s_copy.py'%(name_of_file))
os.rename('%s_copy.py'%(name_of_file), '%s.txt'%(name_of_file))

inputfile = open('%s.txt'%(name_of_file))

# File to be put in 
outputfile = open('%s_document.txt'%(name_of_file),'a')
outputfile.write('# DOCUMENT FOR %s.py # \n\n'%(name_of_file))

# For multiline comments as strings
stack = False

# Maintaining Line Count
i = -1

for line in inputfile:
    i += 1
    line = line.strip()
    
    if line=='':
        outputfile.write('\n')
    
    elif line.startswith('for'):
        
        
        temp = line[line.index('in')+3:line.index(':')]
        outputfile.write('Line %d - For Loop: Iterating in *%s* \n'%(i,temp))
        
    elif line.startswith("while"):

        temp = line[5:].strip(':')
        outputfile.write('Line %d - While Loop: Condition is *%s* \n'%(i,temp))
    
    
    elif line.startswith('def'):

        temp = line[3:].strip('():')
        outputfile.write('Line %d - Calling FUNCTION: %s\n'%(i,temp))
    

    elif line.startswith("#"):
        outputfile.write(line[1:]+'\n')
    
    elif line.startswith("try"):
        outputfile.write('Line %d - Try Block\n'%i)
    
    elif line.startswith("except"):
        outputfile.write('Line %d - Except Block\n'%i)
    
    elif line.startswith("if"):
        
        temp = line[2:len(line)-1]
        outputfile.write('Line %d - If Condition: %s\n'%(i,temp))
    
    elif line.startswith("else"):
        outputfile.write('Line %d - Else block\n'%i)
    
    elif line.startswith("elif"):
        
        temp = line[4:].strip(':')
        outputfile.write('Line %d - Elif Condition: %s\n'%(i,temp))
    
    elif line.startswith("\'\'\'") or line.startswith('\"\"\"'):
        if stack==False:
            outputfile.write('\n') #MultiLineComment
            stack = True
        else:
            outputfile.write('\n\n') #MultiLineComment End
            stack = False
    
    elif stack==True:
        outputfile.write(line+'\n')
    
    else:
        outputfile.write('\n')

    

outputfile.close()
inputfile.close()