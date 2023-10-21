
def collatz(number):
 while number != 1:
    if number % 2 == 0:
        number = number // 2
        print(number)
    else:
        number = 3 * number + 1
        print(number)

try:
    collatz(number=int(input("Enter the number: \n")))
except ValueError:
    print('Error: Invalid argument \nPlease enter a number')
