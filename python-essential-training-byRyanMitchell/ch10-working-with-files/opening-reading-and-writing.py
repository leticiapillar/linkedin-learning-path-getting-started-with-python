# 01 Files

# Reading Files
print("Reading Files")

f = open("file.txt", "r")
print(f)
print("Real line 1:", f.readline())
print("Real line 2:", f.readline())
print("Real all lines:", f.readlines())

print("\n--- Read line by line ---")
f = open("file.txt", "r")
for line in f.readlines():
    print(line)

print("\n--- Read line by line ---")
f = open("file.txt", "r")
for line in f.readlines():
    print(line.strip())

print()
# Writing Files
print("Writing Files")
f = open("file_output.txt", "w")
print(f)
f.write("Line 1\n")
f.write("Line 2\n")
f.close()

print()
# Appending Files
print("Appending Files")
f = open("file_output.txt", "a")
print(f)
f.write("Line 3\n")
f.write("Line 4\n")
f.close()

# Using with to close file in the end
with open("file_output.txt", "a") as f:
    f.write("one more line one\n")
    f.write("one more line two\n")
print(f)

# When using with you cannot write the file after
# the filse closed
f.write("PS. I forgot this line.")
# ValueError: I/O operation on closed file.
