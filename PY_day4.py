#Task 1: Write a Python program to read a file and print its content line by line.
file = open("myfil.txt", "r")

for line in file:
    print(line)

file.close()

#Task 2: Create a Python class named Rectangle with attributes length and breadth and methods to calculate area and perimeter.
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

rect = Rectangle(5, 3)

print("Area of rectangle:", rect.area())
print("Perimeter of rectangle:", rect.perimeter())
