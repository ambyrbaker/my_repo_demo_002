name=input("Ambyr")
print(name)

try:
    num=int(input("Enter a number: "))
    print(num)
    num=num*2
    print(num)
except:
    print("You did not enter a number.")


with open("movies.txt") as file:
    for line in file: # for line adds a line in between
        print(line.strip()) #string method strips

with open("heights.txt") as file:
    for line in file:
        print(line.strip())
        info=line.strip().split()
        print(info)
        print(info[0], info[1], "is", info[2], "inches tall")
        