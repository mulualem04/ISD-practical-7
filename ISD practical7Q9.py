def f(a): # function definition
    # Pass parameters: a=-1,0,1,2,10,100
    if a < 0: # check is the number is negative
        return -1
    n = a
    while n > 0:
        if n % 2 == 0: # n is even
            n = n // 2
        elif n == 1:
            return 1
        else:
            n = 3 * n + 1
        return 0
       # the function returns
def main():
    print(f(-1))
    print(f(0))
    print(f(1))
    print(f(2))
    print(f(10))
    print(f(100))
    print(f(17))

main()
