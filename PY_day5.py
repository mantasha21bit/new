#Use Python's re module to find all occurrences of the word ""Python"" in a given text.
import re
text = "Python is an amazing language. Many developers love Python because Python is versatile."
pattern = "Python"
matches = re.findall(pattern, text)
print(f"Found {len(matches)} occurrences: {matches}")

#Create a list comprehension in Python to generate squares of even numbers between 1 to 10.
squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(squares)
