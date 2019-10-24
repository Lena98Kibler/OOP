'''

Program Description:
The following program will demonstrate how to generate a Pascal's triangle and output it in the same
style as described in the exam brief.

Date: 24/10/2019
Author: Lena Kibler
Student Number: C18499016
Compiler: PyCharm

'''
#Welcome message for user information
print ("Welcome to the Pascal's Triangle Program \n")
print ("This program allows you to build your own Triangle based on your own input \n")
print ("Lets Begin !\n")

#Asking user to input the desired height of the triangle
print ("Please enter the height of your triangle (only use whole numbers larger than 0): ")
Height = int(input())

#Using an if and else statment to prevent user input of 0 and below
if Height <=0:
    print("Invalid value, please try again")

else:
    #defining top of triangle (never changes therefore using a tuple)
    top = 1

    #defining second row (never changes therefore using a tuple instead of a list)
    second_row = (1, 1)

    #defining old_row
    old_row = [1, 1]

    i = 0

    #Creating a function called make_new_row
    def make_new_row(old_row):

        print(top)
        print(second_row)

        #Taking 2 away from the height of the triangle as the first two rows are reserved for 1 and 1,1
        for i in range(Height - 2):

            i = 0

            old_row = [1, old_row[i] + old_row[i + 1], 1]

            print(old_row)

            i = i + 1


    make_new_row(old_row)
