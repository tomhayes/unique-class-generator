import string
import random
import pyautogui
import os.path
from csv import writer

# Database CSV
db = './classes.csv'

# If database CSV doesn't exist, make it
if not (os.path.exists(db)):
    open(db, 'a').close()

# Classname generator function
def class_generator(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

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

pyautogui.write(classname)