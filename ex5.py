INCH_TO_CM = 2.54
POUND_TO_KG = 0.453592

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie

my_height = 74 # inches
my_height_cm = my_height * INCH_TO_CM # centimeters

my_weight = 180 # lbs
my_weight_kg = my_weight * POUND_TO_KG # kilograms

my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)

print "He's %d cm tall." % my_height_cm
print "He's %d kg heavy." % my_weight_kg
