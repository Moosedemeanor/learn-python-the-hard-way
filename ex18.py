# functions do three things
	# they name pieces of code the way variables name strings and numbers
	# they take arguments the way your scripts take 'argv'
	# using 1 and 2 they let you make your own "mini-scripts" or "tiny cmds"
# 'def' - defines a function
# We also tell it we want *args which is a lot like the argv parameter
#			 This HAS to go inside of the ()
# The * in *args tells Python to take all the arguments to the function and put them in args.
def print_two(*args):
    # Make sure to end the 'def' with a ':' and then being indenting
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# '*args' is actually pointless, just do
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Moose","Demeanor")
print_two_again("Moose","Demeanor")
print_one("First!")
print_none()
