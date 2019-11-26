my_name = 'Moosedemeanor'
my_age = 30
my_height_in = 69.0 # inches
my_height_cm = my_height_in * 2.54
my_weight_lbs = 175 # lbs
my_weight_kg = my_weight_lbs * 0.453592
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %r inches tall." % my_height_in
print "He's %r centimeters tall." % my_height_cm
print "He's %r pounds heavy." % my_weight_lbs
print "He's %r kilograms heavy." % my_weight_kg
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height_in, my_weight_lbs, my_age + my_height_in + my_weight_lbs)

# reference - https://docs.python.org/2.7/library/stdtypes.html#string-formatting
