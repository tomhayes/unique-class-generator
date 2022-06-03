import string
import random
# import pyautogui # we don't need this as it's handled by Automator
import os.path
from csv import writer

# Database CSV
db = './classes.csv'

# If database CSV doesn't exist, make it
if not (os.path.exists(db)):
    open(db, 'a').close()

# Classname generator function

def class_generator(size=4, chars=string.ascii_lowercase):
    prefix = "ds-"
    randomString =  ''.join(random.choice(chars) for _ in range(size))

    return prefix + randomString


# Generate classname
classname = class_generator()

#  if classname is already in the csv, re-generate
while classname in open(db).read():
    classname = class_generator()

# Add classname to database CSV
with open(db, 'a', newline='') as f_object:
    # Put classname into a list (otherwise each letter becomes a value)
    classnamelist = [classname]
    # Pass the CSV  file object to the writer() function
    writer_object = writer(f_object)
    # Result - a writer object
    # Pass the classname as an argument into the writerow() function
    writer_object.writerow(classnamelist)
    # Close the file object
    f_object.close()

# pyautogui.write(classname) # this is handled by Automator now...
print(classname)
