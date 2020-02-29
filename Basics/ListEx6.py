"""
Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers
at the end when the user enters done. Write the program to store the numbers the user enters in a list and use the
 max() and min() function to compute the maximum and minimum numbers after the loop completes.

"""
num_lst = []

while True:
    inp = input('Enter numbers: ')
    if inp == 'done':
        break
    elif inp == '' or inp in num_lst:
        print('Enter a number or the number is already existing')
    else:
        num_lst.append(float(inp))

print(num_lst)
print('The maximum number is: ', max(num_lst))
print('The minimum number is: ', min(num_lst))
