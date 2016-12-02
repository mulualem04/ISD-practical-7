def isRightSidePage(page): # function definition
    page=int(input("Plz type in a page number: "))
    if page % 2 == 0:
        print(page)
        return True # the function returns True if page is even number
    else :          # and put the page number on the left side
        print("%60s%d" % (" ", page))
        return False # the function returns False if page is odd number 
                     # and put the page number on the right side
print(isRightSidePage(1))# Call the function within a print    
