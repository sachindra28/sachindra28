name = input("What is your name? ")
print("Hello " + name + " welcom to the game!")

should_we_play = input("Do you want to play? ").lower()


if should_we_play == "y" or should_we_play =="yes":
  print("Let's play!")

  direction = input("Which direction do you want to go? (left/right) ").lower()
  if direction == "left":
    print("You are in the forest")
    forest = input("Do you want to go to the cave or the river? (cave/river) ").lower()
    if forest == "cave":
      print("You are in the cave")
    elif forest == "river":
      print("You are in the river")
    else:
      print("You are lost")

  elif direction == "right":
    print("You are in the desert")
    desert = input("Do you want to go to the mountain or the beach? (mountain/beach) ").lower()
    if desert == "mountain":
      print("You are in the mountain")

    elif desert == "beach":
      print("You are in the beach")

    else:
      print("You are lost")

else:
  print("Goodbye! We are not playing.")
  
