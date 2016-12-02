def mystery(n): # function definition
    # Pass parameters: n=20
    if n <= 0: # check is the number is negative
        return 0
    else:
        return mystery(n // 2) + 1
    # function returns sum of floor division of a number recursively
print(mystery(20))
# Call the function within a print
