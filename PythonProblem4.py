# take all input from user .

# i)   check that all character are string
# ii)  if all char are string then create user in your linux based OS
# iii) also create password for same user , password will
#      password will be  ===>>     hello{username}

import os
data = input("Enter an input ")
charArray = [char for  char in data]

for i in charArray:
    if(i.isdigit()):
        print("Please make sure dont enter any digit in the names\n Please try again..")
        exit()

for i in charArray:
    os.system("sudo useradd "+i+" -p hello"+i) 