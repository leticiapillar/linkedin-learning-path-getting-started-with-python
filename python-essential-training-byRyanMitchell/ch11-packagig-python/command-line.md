## Command line arguments

```bash
# Passsing two arguments
❯ python command-line-arguments.py --output command_line_file.txt --text "Wrote line number one"
Wrote Wrote line number one to file command_line_file.txt

# Passsing two arguments, abreviate
❯ python command-line-arguments.py -o command_line_file.txt -t "Wrote line number two"          
Wrote Wrote line number two to file command_line_file.txt

# Passsing one argument
❯ python command-line-arguments.py -o command_line_file.txt
usage: command-line-arguments.py [-h] --output OUTPUT --text TEXT
command-line-arguments.py: error: the following arguments are required: --text/-t

# Describing help text of arguments
❯ python command-line-arguments.py -h                      
usage: command-line-arguments.py [-h] --output OUTPUT --text TEXT

options:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        The destination file for the output of this program
  --text TEXT, -t TEXT  The text to write to the file
```