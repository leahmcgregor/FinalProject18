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

time.sleep(2)

yourname = input("what is the name of your character? ")

you = Player(yourname, 8.0, 6, 4,5, 5)

crush = Character("Jordan", 9.1, 8, 7)

frendo = Character("Jonah", 8.9, 9, 7)

print(f"""{you.name} wakes to the unpleasant sound of their alarm clock buzzing. 6:00. it looks like it's time to get up.
""")
value = 0
while value != 1:
  wakeup = input("""OPTIONS:
  > get up
  > snooze """)
  if wakeup == "get up":
    value = 1
    print(f"doing the right thing and being a responsible student, {you.name} manages to drag themself out of their bed. they get ready for school, taking extra care to make sure their bag is properly packed. it would suck to forget those summer assignments on the first day, after all.")
  elif wakeup == "snooze":
   value = 1
   print(f"{you.name} knew it would be a terrible idea, but they slam the snooze button and drift back to sleep.")
   time.sleep(2)
   print("...")
   time.sleep(2)
   print(f"6:40. 'shoot!' {you.name} leaps out of their bed in a hurry. they barely have time to get sort of ready, haphazardly tossing their school supplies into their bag as they rush out the door. what a way to start the first day of school.")
  else:
    print("your input is not one of the 2 options listed above. try again.")
time.sleep(2)
print(f"on the bus, {you.name} sits next to your best friend, jonah. even though it's only 7:00 in the morning, he seems alert and chipper. it's probably because of the quart of iced coffee he always carries around.")
time.sleep(2)
print(f"""jonah: {you.name}, my good sir! how was your summer?
{you.name}: it was pretty good, i did absolutely nothing which was pretty cool. how about you?
jonah: i spent the entire time writing college essays. not my definition of a fun time.
{you.name}: oof. oh wait! you're taking calculus ab and ap mech this year, right?
jonah: yeah, why?
{you.name}: we might have the same class for once!""")
time.sleep(2)
print("both of you rustle through your bag and pull out your new schedules.")
time.sleep(2)
print(f"""jonah: ... yes! look! both of us have calculus last period on b days!
{you.name}: and we have physics last period on a days! wild!""")
time.sleep(2)
print(f"the duo falls into a comfortable silence, and {you.name} pulls out their earbuds and play music as the bus starts to move. roughly thirty minutes later, the bus stops and drops its passengers at school. oh, did i say school? sorry, i meant hell.")
time.sleep(2)
print("as you walk into school, security guards are passing out new ids and lanyards to the students. after acquiring your id, you head to the auditorium.")
time.sleep(2)
print("the auditorium is a zoo. friends reunite after the 2 month long summer hibernation, catching up and comparing schedules. it's easy to spot who the freshmen are, because they're the only people not talking to anyone and sitting alone. helen and isaac jump from their seats and greet you enthusiastically. you wave goodbye to jonah as he leaves to hang out with his other senior buddies.")
time.sleep(2)
print(f"""issac: {you.name}! how's it been?
""")

print("""principal whatshisnuts: hello everyone! welcome back to school!
""")