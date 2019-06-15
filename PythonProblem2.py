# write a code using  that will take user input from and search on google 
# and store top 10 url in the list.
# conditions : 
#    i )   URL must be stored permanently as well
#    ii)   user can give input using keyboard and  voice both


from googlesearch import search
choice = int(input("Enter your choice\n1. For Keyboard Entry\n2. For Voice option\n"))
if choice == 1:
    searchTerm = input("Enter the search term you want to search ")
    urlList = []
    
    for result in search(searchTerm,num=10,stop=10):
        urlList.append(result)
    
    for links in urlList:
        print(links)
if choice == 2:
    print("Voice Search is Under Development ")