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

