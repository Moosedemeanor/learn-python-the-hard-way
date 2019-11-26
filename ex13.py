# import the argument variable from the sys module
from sys import argv

script, first, second, third = argv

script = raw_input ("Please rename the script: ")
first = raw_input ("Please provide a fruit: ")
second = raw_input ("Please provide an animal: ")
third = raw_input ("Plese provide a body part: ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
