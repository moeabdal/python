print ("This is a madlibs game.")

name = input("Please enter a name: ").capitalize()
item = input("Please enter an item: ")
time = input("Please enter a number between 1 and 12: ")
scream = input("Please enter a random sentence: ").upper()
action = input("Please enter a verb: ")

print ("It was %s o'clock when I heard a knock on the door. I opened the door and and there was a box full of %s, with a note saying 'From %s'. Just as I closed the door, someone screamed, '%s'. I froze in place and all I could do was %s.") % (time, item, name, scream, action)
