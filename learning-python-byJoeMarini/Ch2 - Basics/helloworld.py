#
# Example file for HelloWorld
# LinkedIn Learning Python course by Joe Marini
#

def main():
    print("Hello World")
    name = input("What is your name? ")
    print("Nice to meet you", name)

# In Short: It Allows You to Execute Code When the File Runs as a Script,
# but Not When It’s Imported as a Module.  --  Real Python
if __name__ == "__main__":
    main()
