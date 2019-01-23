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
    print(f"""{self.name.upper()}'S CURRENT STATS
    GRADE AVG: {self.grade}
    LIKEABILITY: {self.like}
    """)
  def win(self):
    if self.like >= 10 and self.grade >= 90:
      print(f"""congratulations! you have won the game! {self.name} is currently dating jordan and is a high honor roll student with a grade average of {self.grade}.
      """)
    elif self.like >= 10 and self.grade < 90:
      print(f"""congratulations! you have won the primary objective of the game! {you.name} currently dating jordan. however, they did not acheive honor roll. smh, how will they go to college now?
      """)
    elif self.like < 10 and self.grade >= 90:
      print(f"""sorry, you did not win the game. {you.name} did not end up dating jordan. but hey, at least they have good grades, right?
        """)
    elif self.like < 10 and self.grade < 90:
      print(f"""wow, you took a mega L on this game. {you.name} did not end up dating jordan or earn honor roll.
      """)
    print("""anywho, thanks for playing my game! i hope you enjoyed playing this as much as i hated coding it.
    """)
    input("""TYPE ANYTHING TO CONTINUE
    """)
    print("""... oh yeah! one last thing!
    """)
    time.sleep(5)
    print("👌")


calcadvantage = 0
physadvantage = 0
#these are points that will raise the grade of the character whenever they take a test/quiz. they are earned by studying for a specific subject. these stats are purposely hidden from the player.

print("""DATING SIMULATOR V1.0
""")
time.sleep(2)
print(f"""instructions: hello! you are about to play DATING SIMULATOR V1.0! the goal of this game is to win the heart of your character's love interest as they simultaneously struggle to survive their junior year of high school!

every choice you make in this game (aside from your character's name) will affect at least one of your 2 stats: your grade average and how much your crush likes you. your likeability score must be at least 10 in order to successfully ask out your crush, and your grade average must be at least 90 to earn high honor roll.

good luck obtaining the grain!
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print("""disclaimer: any resemblance of any of these characters to actual ucvts students is entirely coincidental.
""")
input("""TYPE ANYTHING TO CONTINUE
""")

yourname = input("what is the name of your character? ")

you = Player(yourname, 80, 5)

Player.stats(you)
print("""September 6, 2018

HOME
""")
time.sleep(2)
print(f"""{you.name} wakes to the unpleasant sound of their alarm clock buzzing. 6:00. it looks like it's time to get up.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
value = 0
while value != 1:
  wakeup = input("""OPTIONS:
  > get up
  > snooze
  """)
  if wakeup == "get up":
    value = 1
    print(f"""doing the right thing and being a responsible student, {you.name} manages to drag themself out of their bed. they get ready for school, taking extra care to make sure their bag is properly packed. they spot their physics summer packet and tuck it neatly into their binder. good catch! it would suck to forget those summer assignments on the first day, after all.
    """)#you remember your physics summer assignment
  elif wakeup == "snooze":
   value = 1
   print(f"""{you.name} knew it would be a terrible idea, but they slam the snooze button and drift back to sleep.
   """)
   time.sleep(2)
   print("""...
   """)
   time.sleep(2)
   print(f"""6:40. 'shoot!' {you.name} leaps out of their bed in a hurry. they barely have time to get sort of ready, haphazardly tossing their school supplies into their bag as they rush out the door. what a way to start the first day of school.
   """)#you forget your physics summer assignment
  else:
    print("your input is not one of the 2 options listed above. try again.")
input("""TYPE ANYTHING TO CONTINUE
""")
print("""BUS
""")
time.sleep(2)
print(f"""on the bus, {you.name} sits next to their best friend, jonah. even though it's only 7:00 in the morning, he seems alert and chipper. it's probably because of the quart of iced coffee he always carries around.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""jonah: {you.name}, my good sir! how was your summer?
{you.name}: it was pretty good, i did absolutely nothing, which was pretty cool. how about you?
jonah: i spent the entire time writing college essays. not my definition of a fun time.
{you.name}: oof. oh wait! you're taking calculus ab and ap mech this year, right?
jonah: yeah, why?
{you.name}: we might have the same class for once!
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print("""the duo rustles through their bags and pulls out their new schedules.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""jonah: ... yes! look! both of us have calculus last period on b days!
{you.name}: and we have physics last period on a days! wild!
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""their initial chatter settles into a comfortable silence, and {you.name} pulls out their earbuds and begins to play music as the bus starts to move. roughly thirty minutes later, the bus stops and drops its passengers at school. oh, did i say school? sorry, i meant hell.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print("""SCHOOL
""")
time.sleep(2)
print(f"""as {you.name} walks into school, security guards are passing out new ids and lanyards to the students. after acquiring their id, {you.name} heads to the auditorium.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print("""AUDITORIUM
""")
time.sleep(2)
print(f"""the auditorium is a zoo. friends reunite after the 2 month long summer hibernation, catching up and comparing schedules. it's easy to spot who the freshmen are, because they're the only people not talking to anyone and sitting alone. helen and isaac jump from their seats and greet {you.name} enthusiastically. they wave goodbye to jonah as he leaves to hang out with his other senior buddies.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""suddenly, just as {you.name} starts comparing their schedule with their friends, the principal raises both of his hands in the air.

principal whatshisnuts: hello everyone! good morning and welcome back to school!
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""as the principal drones on with his welcoming speech, someone leans over from the seat behind {you.name}.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""jordan: hey {you.name}, are we in any classes together?
{you.name}: uh, i'm not sure. can you check?
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""as {you.name} hands their paper over to jordan, she accidentally brushes their hand. it could have been {you.name}'s imagination, but they could swear that they felt sparks fly. they struggle not to blush as jordan intently examines the papers, eyebrows furrowed in concentration.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print("""...
""")
time.sleep(2)
print(f"""jordan: huh. it looks like we have physics and programming together!
{you.name}: oh boi, at least i have someone else to suffer with in there
jordan: true! ... ughhhh i'm not ready for junior year
isaac: is anyone?
jordan: shut up and let me complain, you walnut
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print("""~TIME SKIP (+3 hours)~
""")
time.sleep(2)
print("""PHYSICS CLASS
""")
time.sleep(2)
print(f"""so far, {you.name}'s day has been going pretty well. most teachers were just handing out syllabuses and attempting to get to know their new students, nothing crazy. however, this is {you.name}'s first ap class of the day. they doubt that mrs. vector would pull any fast ones on them, but hey, you never know.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print("""mrs. vector: good afternoon class! welcome to ap physics c: mechanics! sit anywhere you like for now!
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""{you.name} locks eyes with jonah and the dynamic duo immediately steals a table next to the wall, high fiving as they lay claim to their new real estate. when jordan enters the classroom, she sits at the table in front of {you.name} next to helen. they exchange a complicated secret handshake that involves italian hands and finger circles.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""after the class finally settles down, mrs. vector launches into her "teaching mode" voice.

mrs.vector: could everyone please place your summer assignments in this folder?
""")
input("""TYPE ANYTHING TO CONTINUE
""")
if wakeup == "get up":
  print(f"""{you.name}, being the responsible student that they are, takes the summer assignment that they almost forgot on the kitchen counter out from their binder. wow, it sure is lucky that they got up on time, right? if {you.name} had to rush, they might have forgotten it or something.
  """)
  you.grade += 5
elif wakeup == "snooze":
  print("""crud. as {you.name} totally forgot it on the kitchen counter this morning. they really did it too! if only they hadn't been in such a rush from waking up late, they might have remembered to pack it. when mrs. vector notices that you don't turn in your paper, she shakes her head dissapointingly.

  mrs. vector: make sure to bring it in tomorrow, i'm going to have to take points off for late work though.
  """)
  you.grade -= 5
input("""TYPE ANYTHING TO CONTINUE
""")
Player.stats(you)
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""other than that, not much else happens in physics class. the bell rings, and {you.name} goes off to their next class.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""jonah: see you in calculus uwu
{you.name}: yeah, save me a seat!
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print("""~TIME SKIP (+1 hour)~
""")
time.sleep(2)
print(f"""INTRODUCTION TO PROGRAMMING CLASS
""")
time.sleep(2)
print(f"""{you.name} arrives to their second-to-last class of the day earlier than most, with only one other student present so far. normally they'd start this class around noon, but because of the 1st day schedule, it starts at 2:00. the classroom radiates a cozy vibe, with random computer parts and 3d printed models scattered around. {you.name} sits up front, knowing full well that they'd need to pay attention because they have absolutely no previous programming experience.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""the room buzzes with chatter as more students trickle in. jordan strides in, bag slung over one shoulder and takes the seat next to {you.name}. she dumps the bag with a *thud* and groans, collapsing into her seat.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
greet = input("""OPTIONS:
> offer high five
> ask how she is
> say nothing
""")
value = 0
while value != 1:
  if greet == "offer high five":
    value = 1
    print(f"""{you.name} wordlessly offers a high five to jordan as a sign of solidarity. she goes for it, but it's pretty half-hearted. jordan takes out a new textbook from her bag and uses it as a pillow. it doesn't look very comfortable, but it's kind of cute seeing her grumpy tired.
    """)
    you.like +=1
  elif greet == "ask how she is":
    value = 1
    print(f"""{you.name}: hey, you look pretty tired. are you good?
    jordan: yeah, i'm fine. i just only got like 3 hours of sleep last night because i procrastinated on the chemistry summer assignment.
    {you.name}: dang, did you do that all in one night?
    jordan: oh jeez no, i'm not that insane. i started it 2 days ago, but it took longer than i expected.
    {you.name}: oh good, at least you didn't try and rush it. try to get some sleep tonight, though. you look like you really need it.
    """)
    input("""TYPE ANYTHING TO CONTINUE
    """)
    print(f"""jordan gives {you.name} a lopsided smile and winks. well, if you could call it winking. it was more of a really weird, twitchy blink. oddly enough, {you.name} found it pretty adorable.

    jordan: sure, maybe after i'm 66 and retired.
    """)
    you.like += 2
  elif greet == "say nothing":
    value = 1
    print(f"""jordan glances at {you.name}, but they say nothing and scroll through their phone. she turns back to her backpack and quietly gets ready for class while barely suppressing a tired yawn.
    """)
    you.like -= 2
  else:
    print("""sorry, what you entered in was not one of the listed options. please re-enter your action.
    """)
input("""TYPE ANYTHING TO CONTINUE
""")
Player.stats(you)
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""after about 5 minutes, mrs. coding starts class. like most of the other teaches, she passes out a syllabus. overall, it isn't very eventful.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print("""CALCULUS
""")
time.sleep(2)
print(f"""calculus, the last class of the day, goes the same way, but {you.name} does get to sit next to jonah there. the teacher, mr. rolle, is shockingly energetic even after meeting basically 80 students in 1 day. it's almost like he radiates pure sunshine energy.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""2:50. the bell rings, and the hallways flood with students fleeing class. {you.name} hops on the bus and frowns when they see a couple of freshman sitting in jonah and their usual bus seat. ugh. it looks like they'll have to find somewhere else to sit for the bus ride. {you.name} grabs a 2 seater (which are actually 1 seaters, there's no way 2 grown adults can fit on those without basically cuddling) reluctantly. as jonah gets on the bus, he raises his eyebrows at {you.name} when he sees them there. {you.name} subtly nod towards the freshmen. he seems to get it and huffs in annoyance.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print("""~TIME SKIP (+30 minutes)~
""")
time.sleep(2)
print("""HOME
""")
time.sleep(2)
print(f"""ah, home sweet home. {you.name} dumps their bag on the floor and flops onto the couch with a satisfied sigh.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print("""...
""")
time.sleep(2)
print(f"""after doing nothing for a few minutes, {you.name} peels themself from the couch into an upright position. they pick up their bag from where they dropped it and bring it to their room. there isn't any homework for them that they can do yet, they need their dad to come home from work to sign all of the syllabi. what should they do?
""")
input("""TYPE ANYTHING TO CONTINUE
""")
day1time = input("""OPTIONS:
> binge youtube
> study from new textbooks
> practice guitar
> make memes
""")
value = 0
while value != 1:
  if day1time == "binge youtube":
    value = 1
    print(f"""{you.name} opens youtube on their phone and dares to turn on autoplay. the journey eventually leads them far from where they started, from a video of someone attempting to paint a bob ross painting while blindfolded to a diy long furby video.
    """)
    #unlocks conversation with jordan later
  elif day1time == "study from new textbooks":
    value = 1
    print(f"""feeling productive, {you.name} decides to get a head start on calculus and opens the textbook. they already know a little bit of calculus due to the summer crash course they went through to prepare for ap physics, but spending a few hours reading and practicing problems now could only help.
    """)
    calcadvantage += 1
  elif day1time == "practice guitar":
    value = 1
    print(f"""{you.name} takes full advantage of this free time to grab their 6-stringer. they really intended to concentrate and hone their skills, but after only half an hour of actual practice they gave up and just played africa by toto over and over again.
    """)
    #unlocks conversation with jordan later
  elif day1time == "make memes":
    value = 1
    print(f"""{you.name} lets out an evil cackle as they open up photoshop. 2 hours later, and they have an arsenal of fresh, spicy memes, straight from the oven. {you.name} sends an image of a t posing thanos to jonah, who keysmashes in reply.
    """)
    #unlocks text conversation with jordan later if you get her number
  else:
    print("""what you typed in was not one of the available options. try again?
  """)
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""around 6:30, {you.name} hears a car pull into the driveway. it looks like dad's home. they open the door for him so he doesn't have to take out his keys, and he pulls them into a bear hug.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""dad: hey dingus, how was your first day back?
{you.name}: how do you think?
dad: ah, so it went exceptionally well then, i take it. did they load you with homework already?
{you.name}: nah, it's all just papers you need to sign.
dad: alright, i'll do that after i make dinner. care to help me?
{you.name}: absolutely not.
dad: that wasn't an actual question, wash your hands and join me in the kitchen.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""after father and child work together to try to make a halfway decent home cooked meal, he proceeds to sign all of the syllabi the teachers sent home.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""around 10:00, {you.name} heads to bed. it's been a long day and they could use some shut-eye. eventually, {you.name} manages to drift to sleep.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print("""September 16, 2018
""")
time.sleep(2)
print("""AUDITORIUM
""")
time.sleep(2)
print(f"""{you.name} enters the auditorium at 7:45. they don't spot isaac or helen anywhere, but jordan is sitting alone. she smiles and waves {you.name} over.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
if day1time == "make memes":
  print(f"""jordan: hey {you.name}! jonah sent me this while we were working on the physics lab the other day!
  {you.name}: huh, he sent you my meme?
  jordan: your meme? wait you made this?
  {you.name}: yeah, i made it a few weeks ago.
  jordan: oh, that's cool! for real though, it was pretty funny.
  {you.name}: haha thanks, but it was a little trash.
  """)
  you.like += 1
elif day1time == "binge youtube":
  print(f"""jordan: yo, did you see that video where joana ceddia followed a bob ross tutorial while blindfolded?
  {you.name}: yeah, it was pretty insane. she did surprisingly well, too. it actually vaguely resembled the original.
  jordan: well, it still looked like a 5 year old did it.
  {you.name}: i mean yeah, but like a talented 5 year old did it.
  """)
  you.like += 1
elif day1time == "practice guitar":
  print(f"""jordan: hey, isaac told me you play guitar! that's pretty cool.
  {you.name}: oh, yeah! i don't get that much time to practice nowadays because of school, but i try to kind of stay on top of it.
  jordan: i actually play the bass and drums, maybe we should play together sometime!
  {you.name}: oh, that would be lit!
  """)
  you.like +=1
else:
  print(f"""{you.name} sits next to her, but before they get a chance to talk, it's already 7:50. helen runs up to jordan and the pair leave towards their first class.
  """)
input("""TYPE ANYTHING TO CONTINUE
""")
Player.stats(you)
input("""TYPE ANYTHING TO CONTINUE
""")
print("""~TIME SKIP (+5 hours)~
""")
time.sleep(2)
print("""PHYSICS CLASS
""")
time.sleep(2)
print(f"""one more class until {you.name} can go home. they drop off their phone in the box at the front of the class and sit down quietly. mrs. vector wastes no time in passing out a thick packet of kinematics problems. jonah hits his head repeatedly on the desk when he reads the first problem.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""jonah: i didn't even start yet and i'm already confused.
{you.name}: this problem actually isn't that bad. all you have to do is substitute velocity with this equation and use...
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""as {you.name} and jonah steadily work through the problems, helen turns around in her seat and taps {you.name} on the shoulder.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print("""helen: hey, do you know how to do #3?
jordan: we were working on it together, but neither of us can get the right answer.
""")
value = 0
while value !=1:
  helping = input("""OPTIONS:
  > yeah, do you need help?
  > no, sorry
  """)
  if helping == "yeah, do you need help?":
    value = 1
    print(f""" jordan and helen sigh in relief.
    """)
    input("""TYPE ANYTHING TO CONTINUE
    """)
    print(f"""jordan shows {you.name} her work so far. it's a neat collumn of numbers, variables, and equations. reading it through, they see something stick out.
    """)
    input("""TYPE ANYTHING TO CONTINUE
    """)
    print(f"""{you.name}: oh, yeah. i see what you did wrong. you mixed up the formula a little bit. delta v is final minus initial, not initial minus final. also you should use this value for time, not the whole interval.
    jordan: oh, now i see it. thanks!
    helen: wow, we're really out here stealing your brain cells. thanks for the help!
    {you.name}: it's not stealing if there are no brain cells for you to take.
    """)
    physadvantage += 1
    you.like += 2
  elif helping == "no, sorry":
    value = 1
    print("""helen: nah, it's good, i guess we'll all perish together.
    """)
  else:
    print("""it looks like you didn't type in any of the above options. try again?
    """)
input("""TYPE ANYTHING TO CONTINUE
""")
Player.stats(you)
input("""TYPE ANYTHING TO CONTINUE
""")
print("""it's 2:47. everyone is packing up their bags and preparing to leave.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print("""mrs. vector: alright, everyone! don't forget to study for the test next class!
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print("""HOME
""")
time.sleep(2)
print(f"""when {you.name} gets home, they take out their homework and get started. they don't finish it until 8:00. this gives {you.name} only about 2 hours of free time before they need to get ready for bed. how do they spend it?
""")
value = 0
while value != 1:
  day2time = input("""OPTIONS:
  > study for physics
  > procrastinate
  """)
  if day2time == "study for physics":
    value = 1
    physadvantage += 1
    print(f"""{you.name} decides to reopen their physics textbook and work through a few extra problems. by 10:00, their brain feels a little melted, but they understand the material better.
    """)
  elif day2time == "procrastinate":
    print(f"""{you.name} probably could have used this time to prepare for that physics test, but honestly? they're just too tired to bother. instead, they go to bed early and fall asleep instantly.
    """)
input("""TYPE ANYTHING TO CONTINUE
""")
print("""September 18, 2018

PHYSICS CLASS
""")
time.sleep(2)
if physadvantage == 2:
  print(f"""as {you.name} walks into the classroom, they feel confident. they move through the problems at a steady pace and have ample time to check their work.
  """)
  you.grade +=3
elif physadvantage == 1:
  print(f"""{you.name} is only slightly nervous as they walk into physics. they struggle a bit with the last open-ended problems, but overall they think they did a decent job.
  """)
  you.grade += 2
else:
  print(f"""{you.name} feels a little jittery walking into the classroom. they're not as prepared as they should be, and their performance show it. they had to guess on 2 problems, but it could have been much worse.
  """)
  you.grade -= 2
input("""TYPE ANYTHING TO CONTINUE
""")
Player.stats(you)
input("""TYPE ANYTHING TO CONTINUE
""")
print("""HOME
""")
time.sleep(2)
print(f"""as {you.name} works on some calculus homework due tomorrow, their dad knocks on their bedroom door.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print("""dad: hey, i was just wondering if you needed help with any of your calculus. you know, i was really good at it back when i was your age.
""")
value = 0
while value != 1:
  dadhelp = input("""OPTIONS:
  > sure
  > no thanks
  """)
  if dadhelp == "sure":
    value = 1
    print(f"""{you.name}'s dad smiles ear to ear as he pulls over a chair next to your desk.
    """)
    input("""TYPE ANYTHING TO CONTINUE
    """)
    print("""dad: okay, so what unit are you working on right now?
    """)
    input("""TYPE ANYTHING TO CONTINUE
    """)
    print(f"""not only does {you.name} get to finish their homework faster, they get to spend a nice evening with their dad. it's a win-win.
    """)
    calcadvantage += 1
  elif dadhelp == "no thanks":
    value = 1
    print("""dad: oh, okay! if you ever need me or have any questions, feel free to ask me!
    """)
    input("""TYPE ANYTHING TO CONTINUE
    """)
    print(f"""{you.name} feels bad turning down their dad's offer for free help, but really, they can do this on their own. it takes a while, but they eventually finish it.
    """)
  else:
    print("""what you entered was not one of the above options. please enter another option.
      """)
input("""TYPE ANYTHING TO CONTINUE
""")
print("""October 21, 2018)
""")
time.sleep(2)
print("""PROGRAMMING CLASS
""")
time.sleep(2)
print(f"""while waiting for class to start, isaac and jordan are avidly discussing whether or not hot dogs are sandwiches. mrs. coding is judging them in the background. isaac turns to {you.name} in desperation.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""isaac: {you.name}, you're a relatively sane human being. tell me, do you think a hot dog is a sandwich?
""")
value = 0
while value != 1:
  hotdog = input("""OPTIONS:
  > yes
  > no
  """)
  if hotdog == "yes":
    value = 1
    print(f"""jordan raises her hands triumphantly and isaac gives {you.name} a death glare.
    """)
    input("""TYPE ANYTHING TO CONTINUE
    """)
    print(f"""jordan: hah, i told you i was right! even {you.name} agrees with me!
    isaac: all of you are dead to me, i'm leaving.
    """)
    you.like += 1
  elif hotdog == "no":
    value = 1
    print("""jordan gasps dramatically in betrayal while isaac grins smugly.
    """)
    input("""TYPE ANYTHING TO CONTINUE
    """)
    print(f"""jordan: {you.name}! how could you?
    {you.name}: what? it's true!
    isaac: i knew i could count on you to not be stupid! jordan, take notes.
    """)
  else:
    print("""your answer is not one of the above options. please re-enter your response.
    """)
input("""TYPE ANYTHING TO CONTINUE
""")
Player.stats(you)
input("""TYPE ANYTHING TO CONTINUE
""")
print("""CALCULUS CLASS
""")
time.sleep(2)
print(f"""when entering the classroom, {you.name} feels an inexplicable sense of dread. shrugging it off, they sit down and take out their notebook and homework as usual. when they see mr. rolle erase the do now before anyone could start it, they connect the dots. oh no.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print("""mr. rolle: alright everyone! put away your notes. it's time for a pop quiz! i'm sure you'll all do fine, it's only 2 problems. remember, don't stress too much, it's not as hard as it looks.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
print(f"""{you.name} stresses anyways.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
if calcadvantage >= 2:
  print(f"""huh. it actually isn't that bad. {you.name} completes the quiz in 5 minutes, gives it a quick twice-over, and turns it in.
  """)
  you.grade += 2
elif calcadvantage == 1:
  print(f"""the calculus part of the problem is relatively easy, but the simplifying and algebra is kind of tricky. when {you.name} is satisfied with their work, they turn it in.
  """)
  you.grade += 1
else:
  print(f"""the numbers seem to swim around the page as {you.name} works. they do your best to show their work, but they don't think they did it right.
  """)
  you.grade -= 1
input("""TYPE ANYTHING TO CONTINUE
""")
Player.stats(you)
input("""TYPE ANYTHING TO CONTINUE
""")

print("""November 12, 2018
""")
time.sleep(2)
print("""SCHOOL HALLWAYS
""")
print(f"""{you.name} and jonah are taking laps around the school during lunch. as they walk by the chemistry room, {you.name} sees jordan performing a titration lab.
""")
input("""TYPE ANYTHING TO CONTINUE
""")
if you.like >= 10:
  print(f"""jordan spots {you.name} through the window and waves excitedly. they give a 2-finger salute back. in response, she t-poses and asserts her dominance.
  """)
  input("""TYPE ANYTHING TO CONTINUE
  """)
  print(f"""jonah: you know she likes you, right?
  {you.name}: asdfghjkdwqeqtwfyguhiwdef what
  jonah: yeah, she told me that she's been crushing on you for like a month now.
  jonah: ...
  jonah: did you not realize that?
  {you.name}: well duh i didn't realize that! i would have asked her out by now if i did! i've liked her since september!
  jonah: wow, you really are useless huh
  """)
  input("""TYPE ANYTHING TO CONTINUE
  """)
  print(f"""{you.name} glares at jonah.
  """)
  time.sleep(2)
  print(f"""{you.name}: honestly? i can't even argue that.
  jonah: well, what are you waiting for now? i'll ditch you now so you can ask her out after co finishes.
  {you.name}: thanks fam, you are the ultimate wingman. what would i do without you?
  jonah: die, probably
  """)
  input("""TYPE ANYTHING TO CONTINUE
  """)
  print(f"""jonah peaces out and {you.name} waits anxiously for period 5 to end. when it does, jordan is one of the last to walk out of the room. she seems pleasantly surprised to see them leaning against the wall, waiting for her.
  """)
  input("""TYPE ANYTHING TO CONTINUE
  """)
  print(f"""jordan: hey, were you waiting there for me?
  {you.name}: yeah, but only for like 10 minutes, it's fine
  """)
  input("""TYPE ANYTHING TO CONTINUE
  """)
  print("""a hint of a blush appears on jordan's face.
  """)
  input("""TYPE ANYTHING TO CONTINUE
  """)
  print(f"""jordan: you know you didn't have to do that.
  {you.name}: nah, i wanted to.
  """)
  input("""TYPE ANYTHING TO CONTINUE
  """)
  print(f"""jordan almost trips over a pencil after they say that. okay, she's definitely blushing. that's probably a good sign. right?
  """)
  input("""TYPE ANYTHING TO CONTINUE
  """)
  print(f"""{you.name}: anyways, i was wondering if you wanted to hang out with me after school this friday. preferably doing literally anything but schoolwork. like, maybe dinner? a movie? both? heck, i don't know. this is my terrible attempt of asking you out.
  """)
  input("""TYPE ANYTHING TO CONTINUE
  """)
  print("""...
  """)
  time.sleep(5)
  if day1time == "practice guitar":
    print(f"""jordan: i think that would be nice. oh! we could also get around to jamming together like we said we would do!
    {you.name}: dang, that's such a better first date idea. why didn't i think of that?

    jordan just sticks her tongue out at them. what a toddler.
    """)
  else:
   print(f"""jordan: i think i'd like that. a lot, actually.
   {you.name}: wait really?
   jordan: yeah. you're cute, funny, and a genuinely good person. why wouldn't i like to go on a date with you?
   """)
   input("""TYPE ANYTHING TO CONTINUE
    """)
   print(f"""now it's {you.name}'s turn to be a blushing stuttering mess. jordan laughs and pats them on the head.

   jordan: you good there?
   {you.name}: n o
    """)
  input("""TYPE ANYTHING TO CONTINUE
  """)
  print(f"""jordan gently taps {you.name}'s inner wrist with two fingers as a subtle offer to hold her hand. they accept gladly and walk around the school chatting about anything and nothing, hands intertwined and slightly leaning into each other.
  """)
else:
 print(f"""{you.name} and jonah walk past the chemistry room and round the corner.
  """)
 input("""TYPE ANYTHING TO CONTINUE
 """)
 print(f"""{you.name}: you know, i've had a thing for her since the beginning of this year.
 jonah: who? jordan?
 {you.name}: yeah.
 jonah: oh, oof. what do you plan on doing about it?
 {you.name}: i think i'm going to try to forget about it. i don't think it's going to go anywhere. besides, she already makes a great friend. i think it would be best to just leave it this way.
 jonah: okay... you know i've got you if you need to talk about your feelings or anything, right?
 {you.name}: yeah, i know. i'm actually good though.
 """)
 input("""TYPE ANYTHING TO CONTINUE
 """)
 print(f"""{you.name} and jonah continue to walk around the hallway, laughing and joking as they always did. sure, giving up on a crush sucked, but it wasn't the end of the world.
 """)
Player.win(you)