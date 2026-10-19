
# we want to store something in a local file
'''
notesFile = open("notes.txt","a")

notesFile.write("Bootcamp notes\n")
notesFile.write("Loving this session...\n")
notesFile.close()


# read the file
notesFile2 = open("notes.txt","r")
contents = notesFile2.read()
print(contents)
notesFile2.close()
'''
# without needing close()
# print the file line by line, before each line, i will print a line#
'''
with open("notes.txt","r") as notesFile3:
    lineNumber = 0
    for l in notesFile3:
        print(lineNumber)
        print(l)
        lineNumber = lineNumber + 1
   ''' 

# how to read csv file
# comma seperated values
# excel, googole.. csv files 

# write to csv file, read it and print
# no homework.. 



# file called diary.txt
# write 3 lines in that file
# first 2 lines - what do you like about these sessions
# 3rd line - what you hate this session

# read the contents of diary.txt
# print the contents

#12:25

import csv

with open("students.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks"])
    writer.writerow(["Asha1", 78])
   # writer.writerow(["Rohit1", 92])


with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    print(type(reader))
    
    for row in reader:
        print(row)
      #  print(row["Name"], ",Score:", row["Marks"])
    
items = {
 "Apple": 10,
"Banana": 20,
"orange": 15,
"Kiwi": 5
}
print(items)

