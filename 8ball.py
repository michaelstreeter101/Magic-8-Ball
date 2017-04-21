# Original author: Mathias Ettinger
# See: https://codereview.stackexchange.com/questions/118174/magic-8-ball-code
# Original creation date: Jan 29 2016
#
from random import choice
from time import sleep

ANSWERS = ("It is certain",
"It is decidedly so",
"Without a doubt",
"Yes definitely",
"You may rely on it",
"As I see it yes",
"Most likely",
"Outlook good",
"Yes",
"Signs point to yes",
"Reply hazy try again",
"Ask again later",
"Better not tell you now",
"Cannot predict now",
"Concentrate and ask again",
"Don't count on it",
"My reply is no",
"My sources say no",
"Outlook not so good",
"Very doubtful")

while input("Ask the mighty 8-Ball a question\n> "):
  for i in range(1,4):
    print("Shaking{}".format("."*i))
    sleep(.7)
  print(choice(ANSWERS))
