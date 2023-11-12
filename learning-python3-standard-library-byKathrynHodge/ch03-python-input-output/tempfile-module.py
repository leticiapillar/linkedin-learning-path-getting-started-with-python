# 06 Tempfile Module
import tempfile

# Create a temporary file
print("Create a temporary file")
tempfile = tempfile.TemporaryFile()

# Write to a temporary file
print("Write to a temporary file")
tempfile.write(b"Writing in temporary file, the magic number is 458621")

# Read the temporary file
print("Read the temporary file")
tempfile.seek(0)
print(tempfile.read())

# Close the temporary file
print("Close the temporary file")
tempfile.close()