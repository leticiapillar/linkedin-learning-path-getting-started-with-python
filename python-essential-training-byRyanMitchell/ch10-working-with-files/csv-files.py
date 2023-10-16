# 02 CSV
import csv

# Reading
print("Reading csv file")

# The csv file use tab \t instead of comma ,
print("Read all lines")
with open("adresses_us.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        print(row)

print("type reader:", type(reader))
print()

# First line is header, skip it
print("Skip first line, it is header")
with open("adresses_us.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    next(reader) # skip the first line
    for row in reader:
        print(row)

print("type reader:", type(reader))
print()

# First line is header, skip it
print("Skip first line, it is header. Convert reader as list")
with open("adresses_us.csv", "r") as f:
    reader = list(csv.reader(f, delimiter="\t"))
    for row in reader[1:]:
        print(row)

print("size o reader:", len(reader))
print()

# First line is header, skip it
print("Skip first line, it is header. Convert reader as DictReader")
with open("adresses_us.csv", "r") as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        print(row)

print()


# First line is header, skip it
print("Skip first line, it is header. Convert reader as DictReader and list")
with open("adresses_us.csv", "r") as f:
    reader = list(csv.DictReader(f, delimiter="\t"))
    for row in reader[1:]:
        print(row)
print("size o reader:", len(reader))
print()

# Filtering data
print("Filtering data")
with open("adresses_us.csv", "r") as f:
    data = list(csv.DictReader(f, delimiter="\t"))

primes = []
for number in range(2, 99999):
    for factor in range(2, int(number**0.5)):
        if number % factor == 0:
            break
    else:
        primes.append(number)

data = [row for row in data if int(row["postal code"]) in primes and row["state code"] == "MA"]
print("size of data:", len(data))

print()

# Writting
print("Writting file as a csv")
with open("ma_prime.csv", "w") as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow([row["place name"], row["country"]])
