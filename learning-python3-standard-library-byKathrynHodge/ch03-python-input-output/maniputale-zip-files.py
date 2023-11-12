# Zipfile Module
import zipfile

# Open and List
print("Open and List")
zip = zipfile.ZipFile('archive-files.zip', 'r')
print("zip files names:", zip.namelist())

# Metadata in the zip folder
print("Metadata in the zip folder")
for meta in zip.infolist():
    print(meta)

infoNamesfile = zip.getinfo("names.txt")
print("metainfo of names.txt file:", infoNamesfile)

# Access to files in zip folder
print("Access to files in zip folder")
print("read data of fuits file:",zip.read("fruits.txt"))

print("read names of names file:")
with zip.open("names.txt") as f:
    print(f.read())

# Extracting files
print("Extracting files")
namesFile = zip.extract("names.txt")
print("extract names file:", namesFile)
print("extract all files:", zip.extractall())

# Closing the zip
print("Closing the zip")
zip.close()


