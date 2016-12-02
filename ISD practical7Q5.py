def count_spaces(userinput): # function definition
    spaces = 0
    for char in userinput :
        if char == " " :
            spaces = spaces + 1 # increment
    return spaces # the function returns the space between words
userinput = input("Enter a string: ")
print(count_spaces(userinput))
  # Call the function within a print
