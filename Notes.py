## with open ("notes.txt", "w") as f:
##    f.write("Buy groceries \n")
##    f.write("Finish Python Lesson\n")

## with open("notes.txt", "r") as f:
##    contents = f.readlines();
## print (contents)

with open("notes.txt", "a") as f:
    f.write("Call the dentist\n")

with open("notes.txt", "r") as f:
    print (f.read())