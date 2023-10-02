import string

def is_palindrome(teststr):
    # Your code goes here.
    str1 = str(teststr).translate(str.maketrans('', '', string.punctuation)).translate(str.maketrans('', '', string.whitespace)).strip().lower()
    # str2 = str1[::-1]
    return str1 == str1[::-1]

def main():
    words = ["Hello World!","Radar","Mama?","Madam, I'm Adam.", "Race car!"]
    for word in words:
        print(word, "is palindrome?", is_palindrome(word))


if __name__ == "__main__":
    main()