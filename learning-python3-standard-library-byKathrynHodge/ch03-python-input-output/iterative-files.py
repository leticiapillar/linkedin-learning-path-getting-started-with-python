# 05 Iterative Files
myFile = open("scores.txt", "r")

# Read one line at a time
print("Read one line at a time")
print("read line one:", myFile.readline())
print("read line two:", myFile.readline())
myFile.seek(0)

# Iterate through each line of a file
print("Iterate through each line of a file")
for line in myFile.readlines():
    name, score = line.split(":")
    print(f"The score of {name} is {score}")

myFile.close()