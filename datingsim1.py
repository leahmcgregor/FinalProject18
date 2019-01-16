import random
import time

class Character:
  def __init__(self, name, grade):
    self.name = name
    self.grade = grade

class Player(Character):
  def __init__(self, name, grade, like):
    Character.__init__(self, name, grade)
    self.like = like

print("DATING SIMULATOR V1.0")

time.sleep(2)

yourname = input("what is the name of your character? ")

you = Player(yourname, 80, 5)

crush = Character("Jordan", 91)

frendo = Character("Jonah", 89)

print("""HOME
""")
time.sleep(2)
print(f"""{you.name} wakes to the unpleasant sound of their alarm clock buzzing. 6:00. it looks like it's time to get up.
""")
value = 0
while value != 1:
  wakeup = input("""OPTIONS:
  > get up
  > snooze
  """)
  if wakeup == "get up":
    value = 1
    print(f"""doing the right thing and being a responsible student, {you.name} manages to drag themself out of their bed. they get ready for school, taking extra care to make sure their bag is properly packed. it would suck to forget those summer assignments on the first day, after all.
    """)
  elif wakeup == "snooze":
   value = 1
   print(f"""{you.name} knew it would be a terrible idea, but they slam the snooze button and drift back to sleep.
   """)
   time.sleep(2)
   print("...")
   time.sleep(2)
   print(f"""6:40. 'shoot!' {you.name} leaps out of their bed in a hurry. they barely have time to get sort of ready, haphazardly tossing their school supplies into their bag as they rush out the door. what a way to start the first day of school.
   """)
  else:
    print("your input is not one of the 2 options listed above. try again.")
time.sleep(2)
print("""BUS
""")
print(f"""on the bus, {you.name} sits next to their best friend, jonah. even though it's only 7:00 in the morning, he seems alert and chipper. it's probably because of the quart of iced coffee he always carries around.
""")
time.sleep(5)
print(f"""jonah: {you.name}, my good sir! how was your summer?
{you.name}: it was pretty good, i did absolutely nothing which was pretty cool. how about you?
jonah: i spent the entire time writing college essays. not my definition of a fun time.
{you.name}: oof. oh wait! you're taking calculus ab and ap mech this year, right?
jonah: yeah, why?
{you.name}: we might have the same class for once!
""")
time.sleep(5)
print("""the duo rustles through their bags and pull out their new schedules.
""")
time.sleep(5)
print(f"""jonah: ... yes! look! both of us have calculus last period on b days!
{you.name}: and we have physics last period on a days! wild!
""")
time.sleep(5)
print(f"""the duo falls into a comfortable silence, and {you.name} pulls out their earbuds and play music as the bus starts to move. roughly thirty minutes later, the bus stops and drops its passengers at school. oh, did i say school? sorry, i meant hell.
""")
time.sleep(5)
print("""SCHOOL
""")
time.sleep(2)
print(f"""as {you.name} walks into school, security guards are passing out new ids and lanyards to the students. after acquiring their id, {you.name} heads to the auditorium.
""")
time.sleep(5)
print("""AUDITORIUM
""")
time.sleep(2)
print(f"""the auditorium is a zoo. friends reunite after the 2 month long summer hibernation, catching up and comparing schedules. it's easy to spot who the freshmen are, because they're the only people not talking to anyone and sitting alone. helen and isaac jump from their seats and greet {you.name} enthusiastically. they wave goodbye to jonah as he leaves to hang out with his other senior buddies.
""")
time.sleep(5)
print(f"""suddenly, just as {you.name} was comparing their schedule with their friends, the principal raises both of his hands in the air.

principal whatshisnuts: hello everyone! good morning and welcome back to school!
""")
time.sleep(5)
print(f"""as the principal drones on with his welcoming speech, someone leans over from the seat behind {you.name}.
""")
time.sleep(2)
print(f"""jordan: hey {you.name}, are we in any classes together?
{you.name}: uh, i'm not sure. can you check?

as {you.name} hands their paper over to jordan, she accidentally brushes their hand. it could have been {you.name}'s imagination, but they could swear that they felt sparks fly. they struggle not to blush as jordan intently examines the papers, eyebrows furrowed in concentration.
""")
time.sleep(10)
print("""...
""")
time.sleep(2)
print(f"""jordan: huh. it looks like we have physics and chemistry together!
{you.name}: oh boi, at least i have someone else to suffer with in there
jordan: true! ... ughhhh i'm not ready for junior year
isaac: is anyone?
jordan: shut up and let me complain, you walnut
""")
time.sleep(10)
print("""~TIME SKIP (+3 hours)~
""")
time.sleep(2)
print("""PHYSICS CLASS
""")
time.sleep(2)
print(f"""so far, {you.name}'s day has been going pretty well. most teachers were just handing out syllabuses and attempting to get to know their new students, nothing crazy. however, this is {you.name}'s first ap class of the day. they doubt that mrs. vector would pull any fast ones on them, but hey, you never know.
""")
time.sleep(10)
print("""mrs. vector: good afternoon class! welcome to ap physics c: mechanics! sit anywhere you like for now!""")

print(f"""{you.mame} locks eyes with jonah and the dynamic duo immediately steals a table next to the wall, high fiving as they lay claim to their new real estate. when jordan enters the classroom, she surprises you by sitting at the table in front of you next to helen. they exchange a complicated secret handshake.
""")
time.sleep(10)
print(f"""after the class finally settles down, mrs. vector launches into her "teaching mode" voice.

mrs.vector: could everyone please place your summer assignments in this folder?
""")
time.sleep(10)
if wakeup == "get up":
  print(f"""{you.name}, being the responsible student that they are, takes the summer assignment that they almost forgot on the kitchen counter out from their binder. wow, it sure is lucky that they got up on time, right? if {you.name} had to rush, they might have forgotten it or something.
  """)
  you.grade += 5
elif wakeup == "snooze":
  print("""crud. as {you.name} totally forgot it on the kitchen counter this morning. they really did it too! if only they hadn't been in such a rush from waking up late, they might have remembered to pack it. when mrs. vector notices that you don't turn in your paper, she shakes her head dissapointingly.

  mrs. vector: make sure to bring it in tomorrow, i'm going to have to take points off for late work though.
  """)
  you.grade -= 5
time.sleep(10)
print(f"""other than that, not much else happens in physics class. the bell rings, and you're off to your next class.

jonah: see you in calculus uwu
{you.name}: yeah, save me a seat!
""")
time.skip(5)