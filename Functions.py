def gcd(biggest, smallest):
    r = biggest % smallest

    while r > 0:
        biggest = smallest
        smallest = r
        r = biggest % smallest

    print("The gcd of the two numbers is: ", smallest)

print ("Please enter two numbers starting with the highest one")
values = int(input()), int(input())

gcd(values[0], values[1])

