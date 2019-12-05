from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CRTL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# 'w' to open as writeable - 'r' as readable - 'a' for append
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# truncating the file is unnecessary since opening the file in write-mode will overwrite the file
#target.truncate()

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# replaced the following 6 lines with the below 'out' command
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

out = "%s\n%s\n%s\n" % (line1, line2, line3); target.write(out)

print "And finally, we close it."
target.close()
