# Prompt the user to input an integer greater than or equal to 2.
while True :
    n = int(input("Enter an integer greater than or equal to 2: "))
    if n >= 2 :
        break

# Initialize the first two Fibonacci sequence values
a = 0    # The first Fibonacci term 
b = 1    # The second Fibonacci term

# Generate and print Fibonacci numbers until reaching n.
while a <= n :
    print(a)
    # Calculate the next Fibonacci number and update a and b.
    c = b + a     # The next Fibonacci term
    a = b         # Update the first term  
    b = c         # Update the second term
