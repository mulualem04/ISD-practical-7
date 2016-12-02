def main(): 
    a = 4
    print(mystery(a + 1)) # Call the function within a print 

def mystery(x): # function definition
    # Pass parameters : x = 5
    y = x * x
    return y # the function returns square of x

main() # calling a function embedded into a main function
