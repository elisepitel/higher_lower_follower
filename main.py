from game_data import daten
from art import vs 
import random
from replit import clear

USER_SCORE = 0
USERRESPONSE = True


def sentenceToPrint(data):
  """Print sentence for comparison:"""
  data_name = data['name']
  data_description = data['description']
  data_country = data['country']
  #data_follower_count = data['follower_count']
  return f"{data_name}, a {data_description.lower()} from {data_country}"
  #add : has {data_follower_count} tausend of followers and uncomment data_follower_count. to return output value to test code

#Evaluate user answer &increment User Score: 
def isUserRight(A, B, answer):
  """Take the user guess, follower counts, increment score & returns if user is right """

  global USER_SCORE
  global USERRESPONSE
  
  if answer == "a" and A['follower_count'] > B['follower_count']:
    clear()
    USER_SCORE += 1
    print(f"You're right! Current score: {USER_SCORE}")
  elif answer == "b" and B['follower_count'] > A['follower_count']:
    clear()
    USER_SCORE += 1
    print(f"You're right! Current score: {USER_SCORE}")
  else: 
    print(f"Sorry, that's wrong. Final score: {USER_SCORE}")
    replay = input("Would you like to replay? Type 'y' or 'n': ").lower()
    if replay == 'y':
      clear()
      USER_SCORE = 0
      play()
    else:
      clear()
      print("Have a nice day! 🧚‍")
    USERRESPONSE = False
    
#Run Game:
def play(): 
  compareA = random.choice(daten)

  while USERRESPONSE:
    compareB = random.choice(daten)

    #change B if 2 same propositions: 
    while compareA == compareB: 
      compareB = random.choice(daten)

    sentenceA = sentenceToPrint(compareA)
    sentenceB = sentenceToPrint(compareB)

    ##Display two propositions
    print(f"Compare A: {sentenceA}")
    print(vs)
    print(f"Against B: {sentenceB}")

    #Quest
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    isUserRight(compareA, compareB, user_answer)

    #Pass B value within A
    compareA = compareB


#####Start
print("Welcome to the Higher Lower Game! 🧚‍")
play()
