a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(a)
a.append(b)
print(a)
a.pop(0)
print(a)
print(a[1:3])
for i in range(51):
    if i == 20:
        print("uid -> 20 good boy")
        continue
    print("uid ->", i)
rows = 4
for i in range(1, rows + 1):
    print("*" * i)
dict1 = {1: "dipa", 2: "dipanshu", 3: "shardul",2:"dipa"}
print(dict1[2])
c = [9, 2, 5, 1, 2, 6, 4]
for i in range(len(c)):
    for j in range(len(c) - i - 1):
        if c[j] > c[j + 1]:
            temp = c[j]
            c[j] = c[j + 1]
            c[j + 1] = temp
print(c)
x = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{x} * {i} = {x * i}")
