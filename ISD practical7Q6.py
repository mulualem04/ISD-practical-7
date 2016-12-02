def mystery(n): # function definition
    if n <= 0: # check is the number is negative
        return 0
    else:
        return n + mystery(n - 1)
        # Function to return the sum of natural numbers
        # using recursion    
print(mystery(4))# Call the function within a print
