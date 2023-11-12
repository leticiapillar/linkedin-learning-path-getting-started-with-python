# 04 Files and File Writing

# Open a file
# w --> write
# r --> read
# r+ --> read and write
# a --> append

fileToWrite = open("scores.txt", "w")

# Show attributes and properties of that file
print(f"file name: {fileToWrite.name}")
print(f"file mode: {fileToWrite.mode}")

# Write to a file
fileToWrite.write("anna:123\nmaria:321\nbia:231")
fileToWrite.close()

# Read the file
print("Reading file...")

fileToRead = open("scores.txt", "r")
print("read all file:", fileToRead.read())

print("Reading file again, set seek 0...")
fileToRead.seek(0)
print("read 10 chars of file:", fileToRead.read(10))

fileToRead.seek(0)
print("read 10 chars of file:", fileToRead.read(10))
fileToRead.close()
