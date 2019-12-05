# import the argument variable from the sys module
from sys import argv
# import the exists variable from the os.path module
# this variable returns 'True' if a file exists; 'False' if not
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CRTL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alight, all done."

out_file.close()
in_file.close()
