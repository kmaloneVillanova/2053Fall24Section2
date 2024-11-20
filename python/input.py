# num = int(input("Enter a number"))
# print(num)
# num += 1

# try:
#     num = int(input("Enter a number"))
#     print(num)
#     num += 1
# except:
#     print("you must enter a number")

name="kat"
greeting="How are you?"
print("hello", name, greeting)
print(f"Hello, {name} {greeting}")
age=14
print(f"{name} in {18-age} years you can vote!")

vals = [1,2,2,3]
for val in vals:
    print(f"{val},", end="")

with open("movies.txt") as file:
    for line in file:
        print(line.strip())

with open("heights.txt") as file:
    for line in file:
        print(line.strip())
        fname, lname, height = line.split()
        height = int(height)
        print(fname,lname,height)

