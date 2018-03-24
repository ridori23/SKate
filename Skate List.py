# I need there to a new list generated after
# No I don't, I just need ONE new list where I can generate the list I want
# Must I list each trick one at a time? Considering the formating i want to do I think it's acceptable.
# I need a Welcome interface.  I need to prompt user to print out the lists.  Also
# User can add to list and remove from list
basic = ["FS Shuvit", "BS Ollie", "FS Ollie", "Heelflip", "Kickflip", "Fakie BS Bigspin","Fakie FS Bigspin", "Nollie", "BS Nollie", "FS 360", "BS Halfcab", "BS Cab", "FS Cab"]
core = ["Tre Flip", "Nollie Heel", "BS Bigspin", "BS Flip", "FS Flip", "BS 360", "Varial Heel", "Switch Flip"]
goofy = ["Ollie", "FS Ollie", "BS Ollie", "FS Shuvit", "BS Shuvit", "Heelflip", "Back Heel", "Kickflip", "Varial Heel"]
new = ["Hardflip", "Inward Heel", "Nollie Laser", "Nollie Back Heel", "Helicopter Flip", "Late Shuv", "3 Shuv", "Front Heel", "Nollie Bigspin", "Nollie Big Heel"]


print ("Welcome to the Skateboard Trick List Management App!")
prompt = input ("Would you like to print your session list? (yes/no):       ")


import random

random.shuffle(basic)
random.shuffle(new)
random.shuffle(core)
random.shuffle(goofy)
def print_all():
    print ("Outline of Today's Skate Session!!\n\n")
    print ("\t Warm up (x5):  \n\n\t", basic[0],"\n\t", basic[1],"\n\t", basic[2],"\n\t", basic[3], "\n\t", basic[4])
    print ("\t Core Tricks (x5-30):\n\n\t", core[0], "\n\t", core[1], "\n\t", core[2], "\n\t")
    print ("\t Try these new tricks:\n\n\t", new[0], "\n\t", new[1])
    print ("\t If you don't have time for a full goofy session:\n\n\t", goofy[0], "\n\t", goofy[1], "\n\t", goofy[2])

if prompt == "yes":
    print_all()
elif prompt == "no":
    print ("Auf Wiedersehen")
else:
    print ("I said enter yes or no...dumbass")
