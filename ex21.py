def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(25, 5)
height = subtract(89, 20)
weight = multiply(43, 4)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
# A puzzle for extra credit, type it in anyway.
print "Here is a puzzle."
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# divide 50 by 2 = 25
# multiply 172 by 25 = 4,300
# subtract 69 by 4,300 = 4,231
# add 30 to -4,231 = -4,201
print "That becomes: ", what, "Can you do it by hand?"
# I did it by hand in the comments above
