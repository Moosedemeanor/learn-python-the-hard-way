from sys import argv
# sets the argv variables as the script name and a file name the user inputs
script, input_file = argv
# defines a function called 'print_all' with the argument 'f'
def print_all(f):
    # reads the contents of the 'f' argument and then prints it
    print f.read()
# defines a function called 'rewind' which takes the argument 'f'
def rewind(f):
    # 'f' is the file you're working with
    # 0 means your reference point is the beginning of the file
    # 1 means your reference point is the current files position
    # 2 means your reference point is the end of the file
    # I think this line brings the file pointer back to the beginning of the file
    f.seek(0)
# defines a function called 'print_a_line' which takes two arguments: line_count and f
def print_a_line(line_count, f):
    # prints the line count then 1 line from file 'f'
    # f.readline() will read one line from f -
    # - after that the file pointer will be at the start of the next line
    print line_count, f.readline()
# set current_file variable to a file pointer to input_file
current_file = open(input_file)

print "\nFirst, let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape.\n"
rewind(current_file)

print "Let's print three lines:\n"

current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
