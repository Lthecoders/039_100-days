import os
import random
import time

from replit import audio

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyn = '\033[36m'
white = '\033[0m'

print(white)
list_words = ('''spider mouse python duck donkey lion 
                 tiger elephant monkey horse camel snake fish 
                 ant dear zebra bird pig  chicken bat 
                 butterfly human dinosaur goat ship bear frog 
                 fox shark turtle''').split()

# list_words = ["baboon"]


def print_hangman(lives):
  hangman_art = [
      """
            +---+
            |   |
                |
                |
                |
                |
        =========
        """, """
            +---+
            |   |
            O   |
                |
                |
                |
        =========
        """, """
            +---+
            |   |
            O   |
            |   |
                |
                |
        =========
        """, """
            +---+
            |   |
            O   |
           /|   |
                |
                |
        =========
        """, """
            +---+
            |   |
            O   |
           /|\  |
                |
                |
        =========
        """, """
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
        =========
        """, """
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
        =========
        """
  ]
  print(hangman_art[lives])


intro = (f"""\n                                WELCOME TO THE GAME OF\n
                                  {red}  -- HANGMAN --
                                      =========
                                        +---+
                                        |   |
                                        O   |
                                       /|\  |
                                       / \  |
                                            |
                                      =========

{white}
""")
user_picked = []

print(intro)
print(purple, "\n\nLoading the game....")
print("\nPlease wait", white)
time.sleep(5)
os.system("clear")

userTotal_life = 6
computer = random.choice(list_words)

nikhil = 0
top_logo = "----------------> ------ HANGMAN ------ <-----------------"
print(f"\n{red}{top_logo: ^50} {white}")
gamer_name = input("\n\n\n\n\nEnter your gaming name? 😎 --> ").strip().upper()
print(
    blue,
    "\n\n IMP ---------> The word is releated to animals you have to think which animail is this by entering the letter 😏👍\n",
    white)
while True:

  if userTotal_life == 0:
    print(f"{green}\nYou lost! The correct answer was {computer} {white}")
    sad = (f"""\n              \n
                        {red}  -- {gamer_name} --
                            =========
                              +---+
                              |   |
                              O   |
                             /|\  |
                             / \  |
                                  |
                            =========

        {white}
        """)
    print(sad)
    break
  else:
    print(f"only {userTotal_life} lives are left.")

  userPick_letter = input(
      "\n\n (name a type of animal) Type any letter  ---> ").strip().lower()
  if userPick_letter == "":
    print(red, "\nno white space are allowed\n", white)
    continue
  if userPick_letter.isdigit():
    print(red, "\nNo numbers are allowed\nTry again", white)
    continue

  if userPick_letter in user_picked:
    print(red, "\nYou already picked that letter\n.", white)
    continue

  user_picked.append(userPick_letter)

  if userPick_letter in computer:
    print(green, "\nyou found a letter 🥳\n", white)
  else:
    print(red, "\nincorrect", white)
    userTotal_life -= 1
    print_hangman(nikhil)
    nikhil += 1
    print(yellow, "\n\n\nClearinig the incorrects.....")
    time.sleep(3)
    os.system("clear")
    print("\n\n\nCleard successfully", white)
    time.sleep(2)
    os.system("clear")

    print(f"now only {userTotal_life} lives are remaining 😨")

    continue

  allletter = True
  print()
  for i in computer:
    if i in user_picked:
      print(i, end="")
    else:
      print("_", end="")
      allletter = False
  print()

  if allletter == True:
    print(green, "\n\n🫅 👑  You won with", userTotal_life, "life 🫅 👑\n\n",
          white)
    print(blue,
          "\n An champlion deserves an champion music 😏 here you go....enjoy",
          white)
    campion = audio.play_file('france.mp3')
    break
  else:
    continue
