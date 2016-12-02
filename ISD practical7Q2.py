def main() :
	a = 5
	b = 7
	print(mystery(a, b))# Call the function within a print

def mystery(x, y) : # function definition
       # Pass parameters : x = 5, y = 7
	z = x + y
	z = z / 2.0
	return z # the function returns the average of x and y

main()# calling a function embedded into a main function
