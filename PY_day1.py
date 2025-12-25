#Write a Python script to display "Hello, Python!" and also demonstrate the use of comments.

#this is a comment
print("Hello, Python!")


#Create a Python program that uses different variable types (integer, float, string, boolean) and prints their types.
var1 = 10
var2 = 25.5
var3 = "Hello Python"
var4 = True

print(var1, type(var1))
print(var2, type(var2))
print(var3, type(var3))
print(var4, type(var4))



#QUESTIONS FROM SIR 


#Write a function that returns True if two arrays,when combined, form a consecutive sequence.
#A consecutive sequence is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a
#consecutive sequence, but 1, 2, 4, 5 is not.

def is_consecutive(arr1, arr2):
    combined = arr1 + arr2
    if not combined:
        return False

    uniqueARR = sorted(set(combined))

    for i in range(len(uniqueARR) - 1):
        if uniqueARR[i + 1] != uniqueARR[i] + 1:
            return False

    return True

array1 = [1, 2, 3]
array2 = [4, 5]

result = is_consecutive(array1, array2)
print(result)   


#Find the highest sum of adjacent numbers in the below list list1 = [8,-6,9,3,12,7,4]

def highest_adjacent_sum(numbers):
    if len(numbers) < 2:
        return None

    max_sum = numbers[0] + numbers[1]

    for i in range(len(numbers) - 1):
        current_sum = numbers[i] + numbers[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

list1 = [8, -6, 9, 3, 12, 7, 4]
result = highest_adjacent_sum(list1)
print("Highest sum of adjacent numbers:", result)


#Write a script tp take a number as input and print either "perfect" or "not perfect"
#A number is perfect if all the digits of the number are its divisors.
#Example 144 can be divided by 1,4 and 4 but 142 can only be divided by 2.

num = int(input("Enter a number: "))

digits = str(num)
is_perfect = True

for d in digits:
    digit = int(d)
    if digit == 0 or num % digit != 0:
        is_perfect = False
        break

if is_perfect:
    print("perfect")
else:
    print("not perfect")

