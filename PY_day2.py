#Task 1: Create a Python list and demonstrate list slicing and appending new elements.
n = [10, 20, 30, 40, 50]

s1 = n[1:4]
s2 = n[:3]
s3 = n[2:]

n.append(60)
n.append(70)

print(n)
print(s1)
print(s2)
print(s3)


#Task 2: Write a Python script to create, update, and print a dictionary containing
#personal information (like name, age, city).

info = {"name": "Aman", "age": 22, "city": "Ranchi"}

info["age"] = 23
info["city"] = "Delhi"

print(info)

#QUESTIONS FROM SIR 
#Q1: check if the given string is balance. The string will have only {,},(,),[,} characters
s1 = "{{[]}(){}}"
s1 = "{{[]}(){}}"

stack = []
pairs = {')': '(', '}': '{', ']': '['}

balanced = True

for ch in s1:
    if ch in "({[":
        stack.append(ch)
    else:
        if not stack or stack.pop() != pairs[ch]:
            balanced = False
            break

if balanced and not stack:
    print("Balanced")
else:
    print("Not Balanced")


#Q2 :given a list of list with each inner list of equal size in sorted order. 
# Find minimum element that is present in all inner list. 
# For example given the list [[2,3,4,6,8],[1,2,4,6,9],[3,4,5,6,7],[2,5,6,8,9]]
#  the answer will be 6
lists = [[2,3,4,6,8],
         [1,2,4,6,9],
         [3,4,5,6,7],
         [2,5,6,8,9]]

common = set(lists[0])

for lst in lists[1:]:
    common = common.intersection(lst)

print(min(common))

