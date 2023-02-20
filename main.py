import time

# Text Based Adventure Game

# Title Sequence 
print("You step through the now normal size door and find yourself in a dark room")
time.sleep(1)
print("you see the faint glow of a candle.")
print("what will you do? grab the candle / leave it alond")
candle = input(">>")
  if "grab" in candle:
  print("you reach out for the candle, it burns very hot and you singe your lil fingies")
    elif "leave" in candle:
  print("you pass by the candle and notice the ladder and trapdoor at the end of the room")
----------------------------------------------------------
      Its a dark and stormy night, you live in a farm house in the woods isolated except your neighbors house. Your parents are out and the weather is terrible. You decide to do something to pass time until your parents come home.
----------------------------------------------------------

""")
time.sleep(3)

#first Scene
print("""

Your on ground floor in your 3 story house

Go to your room to play video games on your PC

Go to the basement and find some old pictures and valuables	

Which door do you pick?

""")

#first choice for the player to make
first_door = input(">>") # stores input as the variable "first door"

if first_door == "left": # Checks to see if first door is queal to "left"
  print("""
you touch the handle of the left door. You hear a great whooshing sound as the door inexplicably grows in size. 

But wait It's not the door that's growing. It's you shrinking!
  """)

elif first_door == "right": # checks to see if first door is equal to "right"
  print("""

You reach up for the massive door handle.

as you touch it, you feel a great pain as your bones start to rapidly expand, followed quickly by the rest of you as the door starts to look more like a reqular sized door.

  """)
  print("""

When you are a giant! (wow) you pass through the door as you see a giant snail!

It looks at you and somehow you know that it hungers for flesh. Your options are limited.

Do you run or fight?

  """)

snail_encounter = input (">>") # Player chooses to run or fight the snail

 if snail_encounter =="run":
  print("""You have a stand-off with the snail. You stare into it's stalked beady eyes and you know that it knows you are going to run.
  
You try anyway.

It chases you down. You are no match for the hungry snail. You perish")

  """)

  elif snail_encounter == "fight":
  print("""

You stare into the snails eyes. You decide to fight this creature!

the snail pulls out a gun and shoots you dead. Sucks to suck.

  """)