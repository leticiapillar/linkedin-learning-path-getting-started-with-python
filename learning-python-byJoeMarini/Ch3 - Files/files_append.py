#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():  
    # Open a file for writing and create it if it doesn't exist
    # myfile = open("textfile.txt", "w+")

    
    # Open the file for appending text to the end
    myfile = open("textfile.txt", "a+")


    # write some lines of data to the file
    for i in range(10):
        myfile.write(f"Writing NEW line number {i}\n")

    
    # close the file when done
    myfile.close()

    
    # Open the file back up and read the contents

    
if __name__ == "__main__":
    main()
