#Task 1: Write a function in Python that calculates and returns the factorial of a number provided as an argument.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

num = 5
print("Factorial of", num, "is", factorial(num))


#Task 2: Create a script using Python's range function to print all even numbers between 1 and 20.
for i in range(2, 21, 2):
    print(i)
