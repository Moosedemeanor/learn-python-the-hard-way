# import the argument variable from the sys module
from sys import argv
# define the argv variables as the script name and filename, which the user inputs
script, filename = argv
# when the variable 'txt' is called, the script will open the file that the user inputs.
txt = open(filename)
# prints the file selected to the screen
print "Here's your file %r:" % filename
# instructs txt to read(print) the contents of the file to the screen
print txt.read()
txt.close()
# asks the user to input the filename again
print "Type the filename again:"
# establishes 'file_again' as whatever filename the user inputs
file_again = raw_input("> ")
# 'txt_again' will open 'file_again'
txt_again = open(file_again)
# instructs txt_again to print the contents of file to the screen
print txt_again.read()
txt_again.close()
