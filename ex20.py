# import argument variables from system
from sys import argv

# unpacks argv into script and input_file variables
script, input_file = argv

# create a function named print_all with variable f as argument
def print_all(f):
# read the file which has been specified and stored in f
    print f.read()

# create another function called rewind with variable f as the argument
def rewind(f):
# seek the first character in the file that has been specified and stored in f
    f.seek(0)

# create a third function called print_a_line and give it two arguments:
# line_count and f
# print the line_count variable
# and call the readline function on f variable
def print_a_line(line_count, f):
    print line_count, f.readline()

# Open the file and store it to current_file
current_file = open(input_file)

# Let the user know whats happening
print "First let's print the whole file:\n"

# Call print_all function with current_file as its argument variable
print_all(current_file)

# Let the suer know whats happening
print "Now let's rewind, kind of like a tape."

# Call rewind function with the current_fiel as its argument variable
rewind(current_file)

# Let the user see the lines
print "Let's print three lines:"

# addds 1 o the variable current_line
current_line = 1
# Call print_a_line function as current_line serving as line_count
# and current_file serving as f
print_a_line(current_line, current_file)

# add 1 more to current line (total: 2)
current_line = current_line + 1
# One last time, call function. Same variables serve as function's arguments.
print_a_line(current_line, current_file)

# Add 1 more to current line (total: 3)
current_line = current_line + 1
# One last time, call function. Same variables serve as function's arguments.
print_a_line(current_line, current_file)
