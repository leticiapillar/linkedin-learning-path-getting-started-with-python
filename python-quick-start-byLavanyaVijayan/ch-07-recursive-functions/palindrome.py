def isPalindrome(s):
    """Return whether strings is a palindrome"""
    if len(s) <= 1:
        # return s
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])

def main():
    strings  = ["k", "5", "121", "1221", "Anna", "-5", "1212"]
    for s in strings:
        p = isPalindrome(s)
        print(f"{s} is palindrome? {p}")

if __name__ == "__main__":
    main()
