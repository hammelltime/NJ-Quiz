import sys

# 1ST GAME OPTION
def easy_game():
  
  easy_quiz = ["Many NJ residents love going to the beach in the summer, but they don't call it the 'beach'. They call it the ___.", 
  "We  also have a large Italian-American population.  If you ever pass through the 'Burg', an area of Trenton, you must try a special kind of pizza called a tomato ___, which is more focused on the tomatos and less on the cheese.",  
  "After your meal, head on over to the Yankees minor league baseball team, the Trenton ___.  It's a beautiful park where every seat is close to the field.", 
  "Actually, New Jersey isn't filled of highways.  There are very scenic portions, which is why it's known as the ___ State.",  
  "But up north in the section that is more metropolitan, we still have our only team of a major sport.  They are the New Jersey ___."]
  blank = ["___"]
  easy_answers = ["shore", "pie", "Thunder", "Garden", "Devils"]
  
  # THE QUIZ...
  
  index = 0
  
  print ""
  print easy_quiz[index]
  print ""

  guesses = 3
  while int(guesses) > 0:
    user_input = raw_input("Type in your answer: ")
    if user_input == easy_answers[index]:
      print ""
      print "Oh, a wise guy!"
      print ""
      easy_quiz[index] = play_game(easy_quiz[index],blank, user_input)
      print easy_quiz[index]
      index += 1
      if index == 5:
				break
    else:
			guesses -= 1
			print ""
			print "Wrong, dingbat! You still have " + str(guesses) + " guesses left."
			print ""
    print easy_quiz[index]
  if guesses > 0:
		print "Congratulations on not being a stunad!  You finished the quiz!"
  else:
		print "You don't have any guesses left.  Please accept my condolences."

  # Allows user to take a different quiz/retake the quiz
  print " "
  new_quiz = raw_input("If you want to play another quiz you can type in the name (easy way, medium way, or hard way). If you want to quit hit enter.")
  if new_quiz == "easy way":
		easy_game()
  elif new_quiz == "medium way":
		medium_game()
  elif new_quiz == "hard way":
		hard_game()
  else:
		sys.exit()


# 2ND GAME OPTION
def medium_game():
  
  medium_quiz = ["New Jersey is home to many celebrities.  Some of them were da best!  Way back when there was ol' blue eyes, ___.",
  "More recently was the Boss, known for his shows at the Stony Pony, ___.",  "But we also got actuhs.  There is the short, balding nut who played George on Seinfeld, ___.",
  "And also da short Italian guy who epitimizes our state with his short temper.  ___ played roles in mafia movies, but also the lawyer in My Cousin Vinny.",
  "Lastly, I don't want to leave out the famous women from Jersey.  The lovely ___ was in the popular film The Princess Diaries."]
  
  blank = ["___"]
  
  medium_answers = ["Frank Sinatra", "Bruce Springstein", "Jason Alexander", "Joe Pesci", "Anne Hathaway"]
  
  index = 0
	
	  # THE QUIZ...
	
  print ""
  print medium_quiz[index]
  print ""  
	
  guesses = 3
  while int(guesses) > 0 :
    #print ""
		user_input = raw_input("Type in your answer: ")
		if user_input == medium_answers[index]:
		  print ""
		  print "Oh, a wise guy!"
		  print ""
		  medium_quiz[index] = play_game(medium_quiz[index],blank, user_input)
		  print medium_quiz[index]
		  index += 1
		  if index == 5:
				break
		else:
			guesses -= 1
			print ""
			print "Wrong, dingbat! You still have " + str(guesses) + " guesses left."
			print ""
		print medium_quiz[index]
  if guesses > 0:
		print "Congratulations on not being a stunad!  You finished the quiz!"
  else:
		print "You don't have any guesses left.  Please accept my condolences."

  # Allows user to take a different quiz/retake the quiz
  print " "
  new_quiz = raw_input("If you want to play another quiz you can type in the name (easy way, medium way, or hard way). If you want to quit hit enter.")
  if new_quiz == "easy way":
		easy_game()
  elif new_quiz == "medium way":
		medium_quiz()
  elif new_quiz == "hard way":
		hard_quiz()
  else:
		sys.exit()


# 1ST GAME OPTION
def hard_game():
  
  hard_quiz = ["The light ___ was invented by Thomas Edison in his Menlo Park lab.",
  "The Statue of ___ is located in the waters of Jersey City.",
  "The first ___ game was played in Hoboken in 1845.",
  "New Jersey is often referred to as the ___ capital of the world.", 
  "The longest ___ in the world is located in Atlantic City."]
  
  blank = ["___"]
  
  hard_answers = ["bulb", "Liberty", "baseball", "diner", "boardwalk"]
  
  # THE QUIZ...
  
  index = 0
  
  print ""
  print hard_quiz[index]
  print ""

  guesses = 3
  while int(guesses) > 0:
    user_input = raw_input("Type in your answer: ")
    if user_input == hard_answers[index]:
      print ""
      print "Oh, a wise guy!"
      print ""
      hard_quiz[index] = play_game(hard_quiz[index],blank, user_input)
      print hard_quiz[index]
      index += 1
      if index == 5:
				break
    else:
			guesses -= 1
			print ""
			print "Wrong, dingbat! You still have " + str(guesses) + " guesses left."
			print ""
    print hard_quiz[index]
  if guesses > 0:
		print "Congratulations on not being a stunad!  You finished the quiz!"
  else:
		print "You don't have any guesses left.  Please accept my condolences."

  # Allows user to take a different quiz/retake the quiz
  print " "
  new_quiz = raw_input("If you want to play another quiz you can type in the name (easy way, medium way, or hard way). If you want to quit hit enter.")
  if new_quiz == "easy way":
		easy_game()
  elif new_quiz == "medium way":
		medium_game()
  elif new_quiz == "hard way":
		hard_game()
  else:
		sys.exit()
	
# determines if the word is a blank
def check_answer(word, blank):
    for element in blank:
      if element in word:
        return element
      return None


def play_game(quiz_question, blank, user_input):
    replaced = []
    quiz_list = quiz_question.split()

    for word in quiz_list:
        replacement = check_answer(word, blank)
        if replacement != None:
          word = word.replace(replacement, user_input)
          replaced.append(word)
        else:
          replaced.append(word)
    replaced = " ".join(replaced)
    return replaced


welcomeMessage = """Hey yo! Welcome to the Jersey Quiz! I hope yous guys have half uh brain to answer these questions correctly. Now we can do this the easy way, or the hard way... or the medium way."""

#Actual start of the program
print welcomeMessage
print ""
choice = raw_input("Which will it be?")
correctChoice = True
#As long as the user hasn't typed in a correct categorie, the program will keep asking.
while correctChoice:
	if (choice == "easy way" or choice == "medium way" or choice =="hard way"):
		break
	print "Very creative, but that's not an option."
	choice = raw_input("Would you like the 'easy way', 'medium way', or 'hard way'?")

#Once a correct choise has been made, the program will start one of the three possible quizzes.  This piece of code selects the right function.
if choice == "easy way":
	easy_game()
elif choice == "medium way":
	medium_game()
else:
	hard_game()

