#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: March 2025
# This program calculates the sum of the first n terms of the harmonic series
# where n is a positive integer entered by the user.


# Function to calculate the sum of the harmonic series
def main():
    # Display greeting message
    print(
        "Hello, welcome to the program that calculates the sum of the harmonic series."
    )
    print("Please enter an n value.")

    # Start with n = 0 (invalid) so the loop runs at least once
    n = 0

    # Loop until the user enters a valid positive integer
    while n <= 0:
        user_input = input("Enter a positive integer n: ")

        try:
            # Try to convert the input to a float (handles decimals too)
            user_number = float(user_input)

            # Convert the float to an integer (truncates decimal part)
            n = int(user_number)

            # If the user entered a decimal, tell them it was rounded down
            if user_number != n:
                print("You entered a decimal. It has been rounded down to:", n)

            # If the number is less than or equal to 0, ask again
            if n <= 0:
                print("Please enter a positive integer greater than 0.")

        except:
            # If the input can't be converted to a float, show error message
            print("Invalid input. Please enter a real number.")

    # Now calculate the harmonic sum
    sum = 0
    i = 1

    # Loop from 1 to n and add 1 / i to the sum each time
    while i <= n:
        sum = sum + 1 / i
        i = i + 1

    # Display the final result
    print("The sum of the harmonic series is:", sum)


# Call the main function to run the program
main()
