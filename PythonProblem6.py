#!/usr/bin/python3
# use file handling to create a linux command  similar to cat .
# test at least  4 cases and options of cat command
# compare the difference of cat command and post the result
# --help
# -n Number
# --version
# ./PythonProblem6.py filedata -n
# ./PythonProblem6.py filedata --version
# ./PythonProblem6.py filedata --help
# ./PythonProblem6.py filedata 
import os,sys
size = len(sys.argv)

if size == 1 :
    arg = sys.argv[0]
    if arg == '--help':
        # Show Help
    elif arg == '--version':
        # Show Version
    else:
        # Run The program without any arguments   

if size == 2 : # argument exist
    # Read argument and use it
    arg = sys.argv[1]
    if arg == '-n':

arg1 = sys.argv[]

print(arg1)


