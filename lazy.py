# For easy (lazy) documenting of python scripts #

# Author: Pratiksha Jain
# Created On: 21.06.20

#-------------------------------#

## Imports required (Standard library) ##
import os
from shutil import copyfile

#-------------------------------#

## For Setting Up The Document And Giving Title ##

# Path of Python file to be read; put PATH without extension
name_of_file = 'sample'

# File copied and renamed to txt(readable)
# Edit as needed
copyfile('%s.py'%(name_of_file), '%s_copy.py'%(name_of_file))
os.rename('%s_copy.py'%(name_of_file), '%s.txt'%(name_of_file))

inputfile = open('%s.txt'%(name_of_file))

# Output Document: Edit as needed
outputfile = open('%s_document.txt'%(name_of_file),'a')

# Title of File
outputfile.write('# DOCUMENT FOR %s.py # \n\n'%(name_of_file))

#-------------------------------#

## Defining Some Functions ##

# To check if any of the strings in given list are in the line.
def StringsInLine(list_of_strings, line):
    
    String = ""

    for string in list_of_strings:
        if line.find(string) != -1:
            String = string
            break

    return String

#-------------------------------#

## The Actual Reading/Writing Of Input/Output Document ##

# For multiline comments as strings
IsMultilineComment = False

# Maintaining Line Count
i = 0

# For storing self defined functions
my_defined_functions =  []

for line in inputfile:
    i += 1
    line = line.strip()
    
    if line=='':
        outputfile.write('\n')
    
    elif line.startswith('for'):
        
        temp = line[line.index('in')+3:].strip(': ')
        outputfile.write('Line %d - For Loop: Iterating over *%s* \n'%(i,temp))
        
    elif line.startswith("while"):

        temp = line[5:].strip(': ')
        outputfile.write('Line %d - While Loop: Condition is **%s** \n'%(i,temp))
    
    
    elif line.startswith('def'):

        temp = line[3:].strip('(): ')
        my_defined_functions.append(temp)

        outputfile.write('Line %d - Defining FUNCTION: <%s>\n'%(i,temp))
    

    elif line.startswith("#"):

        outputfile.write(line.strip('# ')+'\n')

    
    elif line.startswith("try"):
        outputfile.write('Line %d - Try Block\n'%i)
    
    elif line.startswith("except"):
        if line.startswith("except:") or line.startswith("except :"):
            outputfile.write('Line %d - Except Block\n'%i)
        else:
            temp = line[7:].strip(': ')
            outputfile.write('Line %d - Except Block Exception: %s\n'%(i,temp))
    
    elif line.startswith("if"):
        
        temp = line[2:].strip(': ')
        outputfile.write('Line %d - If Condition: **%s**\n'%(i,temp))
    
    elif line.startswith("else"):
        
        outputfile.write('Line %d - Else block\n'%i)
    
    elif line.startswith("elif"):
        
        temp = line[4:].strip(': ')
        outputfile.write('Line %d - Elif Condition: **%s**\n'%(i,temp))
    
    elif line.startswith("\'\'\'") or line.startswith('\"\"\"'):
        
        if IsMultilineComment==False:
            outputfile.write('\n') #MultilineComment
            IsMultilineComment = True
        else:
            outputfile.write('\n\n') #IfMultilineComment End
            IsMultilineComment = False
    
    elif IsMultilineComment==True:
        outputfile.write(line+'\n')
    
    elif StringsInLine(my_defined_functions, line) != "":
        outputfile.write('Calling FUNCTION: <%s>\n'%(StringsInLine(my_defined_functions, line)))


    else:

        outputfile.write('\n')

#-------------------------------#

## Closing The Documents ##

outputfile.close()
inputfile.close()
os.remove('%s.txt'%(name_of_file))

#-------------------------------#
