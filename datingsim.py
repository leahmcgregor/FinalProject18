import random
import time

class Character:
  def __init__(self, name, grade, pers, phys):
    self.name = name
    self.grade = grade
    self.pers = pers
    self.phys = phys

class Player(Character):
  def __init__(self, name, grade, pers, phys, luck, like):
    Character.__init__(self, name, grade, pers, phys)
    self.luck = luck
    self.like = like

print("DATING SIMULATOR V1.0")

yourname = input("what is the name of your character?")

you = Player(yourname, 8.0, 6, 4,5, 5)

crush = Character("Jordan", 9.1, 8, 7)

frendo = Character("Jonah", 8.9, 9, 7)

print(f"""{you.name} wakes to the unpleasant sound of their alarm clock buzzing. 6:00. it looks like it's time to get up.
""")
value = 0
while value != 1:
  wakeup = input("""OPTIONS:
  > get up
  > snooze""")
  if wakeup == "get up":
    value = 1
    print(f"doing the right thing and being a responsible student, {you.name} manages to drag themself out of their bed. they get ready for school, taking extra care to make sure their bag is properly packed. it would suck to forget those summer assignments on the first day, after all.")
  elif wakeup == "snooze":
   value = 1
   print(f"{you.name} knew it would be a terrible idea, but they slammed the snooze button and drifeted back to sleep.")
   time.sleep(2)
   print("...")
   time.sleep(2)
   print(f"6:40. 'shoot!' {you.name} leaps out of their bed in a hurry. they barely have time to get sort of ready")
  else:
    print("your input is not one of the 2 options listed above. try again.")