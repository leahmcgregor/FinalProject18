import random
import time

class Character:
  def __init__(self, name, grade):
    self.name = name.lower()
    self.grade = grade

class Player(Character):
  def __init__(self, name, grade, like):
    Character.__init__(self, name, grade)
    self.like = like

  def stats(self):
    print(f"""{self.name.upper()}'s CURRENT STATS
    GRADE AVG: {self.grade}
    LIKEABILITY: {self.like}
    """)

print("DATING SIMULATOR V1.0")

time.sleep(2)
print(f"""instructions: hello! you are about to play DATING SIMULATOR V1.0! the goal of this game is to win the heart of your character's love interest as they simultaneously struggle to survive their junior year of high school!

every choice you make in this game (aside from your character's name) will affect at least one of your 2 stats: your grade average and how much your crush likes you. your likeability score must be at least 10 in order to successfully ask out your crush, and your grade average must be at least 90 to earn high honor roll.

good luck obtaining the grain!
""")
time.sleep(10)
print("""disclaimer: any resemblance of any of these characters to actual ucvts students is entirely coincidential.
""")
time.sleep(2)

yourname = input("what is the name of your character? ")

you = Player(yourname, 80, 5)

crush = Character("Jordan", 91)

frendo = Character("Jonah", 89)

Player.stats(you)
print("""September 6, 2018

HOME
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
time.sleep(10)
print("""BUS
""")
time.sleep(2)
print(f"""on the bus, {you.name} sits next to their best friend, jonah. even though it's only 7:00 in the morning, he seems alert and chipper. it's probably because of the quart of iced coffee he always carries around.
""")
time.sleep(10)
print(f"""jonah: {you.name}, my good sir! how was your summer?
{you.name}: it was pretty good, i did absolutely nothing which was pretty cool. how about you?
jonah: i spent the entire time writing college essays. not my definition of a fun time.
{you.name}: oof. oh wait! you're taking calculus ab and ap mech this year, right?
jonah: yeah, why?
{you.name}: we might have the same class for once!
""")
time.sleep(10)
print("""the duo rustles through their bags and pull out their new schedules.
""")
time.sleep(5)
print(f"""jonah: ... yes! look! both of us have calculus last period on b days!
{you.name}: and we have physics last period on a days! wild!
""")
time.sleep(5)
print(f"""the duo falls into a comfortable silence, and {you.name} pulls out their earbuds and play music as the bus starts to move. roughly thirty minutes later, the bus stops and drops its passengers at school. oh, did i say school? sorry, i meant hell.
""")
time.sleep(10)
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
time.sleep(10)
print(f"""suddenly, just as {you.name} was comparing their schedule with their friends, the principal raises both of his hands in the air.

principal whatshisnuts: hello everyone! good morning and welcome back to school!
""")
time.sleep(10)
print(f"""as the principal drones on with his welcoming speech, someone leans over from the seat behind {you.name}.
""")
time.sleep(5)
print(f"""jordan: hey {you.name}, are we in any classes together?
{you.name}: uh, i'm not sure. can you check?

as {you.name} hands their paper over to jordan, she accidentally brushes their hand. it could have been {you.name}'s imagination, but they could swear that they felt sparks fly. they struggle not to blush as jordan intently examines the papers, eyebrows furrowed in concentration.
""")
time.sleep(10)
print("""...
""")
time.sleep(2)
print(f"""jordan: huh. it looks like we have physics and programming together!
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
print("""mrs. vector: good afternoon class! welcome to ap physics c: mechanics! sit anywhere you like for now!
""")
time.sleep(5)
print(f"""{you.name} locks eyes with jonah and the dynamic duo immediately steals a table next to the wall, high fiving as they lay claim to their new real estate. when jordan enters the classroom, she sits at the table in front of you next to helen. they exchange a complicated secret handshake that involves italian hands and finger circles.
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
frendo.grade += 5
crush.grade += 1
time.sleep(10)
Player.stats(you)
time.sleep(5)
print(f"""other than that, not much else happens in physics class. the bell rings, and you're off to your next class.
""")
time.sleep(5)
print(f"""jonah: see you in calculus uwu
{you.name}: yeah, save me a seat!
""")
time.sleep(5)
print("""~TIME SKIP (+1 hour)~
""")
time.sleep(2)
print(f"""INTRODUCTION TO PROGRAMMING CLASS
""")
time.sleep(2)
print(f"""{you.name} arrives to your second-to-last class of the day earlier than most, with only one other student present so far. normally they'd start this class around noon, but because of the 1st day schedule, it starts at 2:00. the classroom radiates a cozy vibe, with random computer parts and 3d printed models scattered around. {you.name} sits up front, knowing full well that they'd need to pay attention because they have absolutely no previous programming experience.
""")
time.sleep(10)
print(f"""the room buzzes with chatter as more students trickle in. jordan strides in, bag slung over one shoulder and takes the seat next to you. she dumps the bag with a *thud* and groans, collapsing into her seat.
""")
time.sleep(10)
greet = input("""OPTIONS:
> offer high five
> ask how she is
> say nothing
""")
if greet == "offer high five":
  print(f"""{you.name} wordlessly offers a high five to jordan as a sign of solidarity. she goes for it, but it's pretty half-hearted. jordan takes out a new textbook from her bag and uses it as a pillow. it doesn't look very comfortable, but it's kind of cute seeing her grumpy tired.
  """)
  you.like +=1
elif greet == "ask how she is":
  print(f"""{you.name}: hey, you look pretty tired. are you good?
  jordan: yeah, i'm fine. i just only got like 3 hours of sleep last night because i procrastinated on the chemistry summer assignment.
  {you.name}: dang, did you do that all in one night?
  jordan: oh jeez no, i'm not that insane. i started it 2 days ago, but it took longer than i expected.
  {you.name}: oh good, at least you didn't try and rush it. try to get some sleep tonight, though. you look like you really need it.
  """)
  time.sleep(10)
  print(f"""jordan gives {you.name} a lopsided smile and winks. well, if you could call it winking. it was more of a really weird, twitchy blink. oddly enough, {you.name} found it pretty adorable.

  jordan: sure, maybe after i'm 66 and retired.
  """)
  you.like += 2
elif greet == "say nothing":
  print(f"""jordan glances at {you.name}, but they say nothing and scroll through their phone. she turns back to her backpack and quietly gets ready for class while barely suppressing a tired yawn.
  """)
  you.like -= 2
else:
  print("""sorry, what you entered in was not one of the listed options. please re-enter your action.
  """)
time.sleep(10)
Player.stats(you)
time.sleep(5)
print(f"""after about 5 minutes, mrs. coding starts class. like most of the other teaches, she passes out a syllabus. overall, it isn't very eventful.
""")
time.sleep(5)
print("""CALCULUS
""")
time.sleep(2)
print(f"""calculus, the last class of the day goes the same way, but {you.name} does get to sit next to jonah there. the teacher, mr. rolle, is shockingly energetic even after meeting basically 80 students in 1 day. it's almost like he radiates pure sunshine energy.
""")
time.sleep(10)
print(f"""2:50. the bell rings, and the hallways flood with students fleeing class. you hop on the bus and frown when {you.name} sees a couple of freshman sitting in jonah and their's usual bus seat. ugh. it looks like they'll have to find somewhere else to sit for the bus ride. {you.name} grabs a 2 seater (which are actually 1 seaters, there's no way 2 grown adults can fit on those without basically cuddling) reluctantly. as jonah gets on the bus, he raises his eyebrows at {you.name} when he sees them there. you subtly nod towards the freshmen. he seems to get it and huffs in annoyance.
""")
time.sleep(15)
print("""~TIME SKIP (+30 minutes)~
""")
time.sleep(2)
print("""HOME
""")
time.sleep(2)
print(f"""ah, home sweet home. {you.name} dumps their bag on the floor and flops onto the couch with a satisfied sigh.
""")