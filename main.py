import random

ans = True

while ans:
  question = input("Ask the 8 ball a question: Press 'NO' to quit: ")

  answers = random.randint(1,6)

  if question == "NO":
    break

  elif answers == 1:
      print ("It is certain")

  elif answers == 2:
      print ("Yes")

  elif answers == 3:
      print ("No way!")

  elif answers == 4:
      print ("Ask again later")

  elif answers == "no":
      print ("I'm sorry? I didn't understand, do you want to keep playing? If no, please type NO")

print ("Thanks for playing! See you next time!")

