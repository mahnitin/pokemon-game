import random
def to_str(word):
  blank=''
  return blank.join(word)
def pokemon():
  pokemon_random=random.choice(['balbasaur','pikachu','raichu','magikarp','nidoking','persian','ninetail','magnemite','weezing','koffing','ekans','scyther','magmar','kabuto','snorlax','zapdos','squirtle','chikorita','slowking','butterfree','charmander','charlizard','psyduck','pidgeot','sandlash','sandshrew','jigglypuff','venomoth','tentacruel','lapras','geodude','golem','poliwhirl'])
  word=pokemon_random.upper()
  main=[]
  valid_input=('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  turn =10
  
  wrong_guess=" "
  for x in range (0,len(word)):
    main.append("_ ") 
  while turn != 0:  
    print("                         "+to_str(main)) 
    print(f"\n**Wrong guess remaining: {turn}.\nWrong guesses:({wrong_guess})** ")
    guess=input("Enter ur guess: ")
    guess=guess.upper()
    if guess == "":
      print("please give an input")
    if guess in valid_input and guess!="":
      if guess in word:
        occurance=word.count(guess)
        place=word.index(guess)
        main[place]=word[place]
        if occurance >1:
          while occurance-1>0:
            place=word.index(guess,place+1)
            main[place]=word[place]
            occurance-=1
        if to_str(main) == word:
          print("                         "+to_str(main))
          print( f"\nCongratulation {name.title()}. You caught this beauty.")
          print("You are a good trainer")
          break
        else:
          print("\n***Correct guess!!!!Keep going***\n")  
      else :
        turn =turn-1
        print("")
        print("     !!!!Wrong!!!!    ")
        print(f"You have **{turn}** turn left")
        wrong_guess=wrong_guess+ guess+" "
        print("")
    else:
      print("please enter a valid alphabet")    
  if turn == 0:
    print("!!!!!!OOPS!!!!!!")
    print( f'The correct answer was : {word}')
    print("It escaped out of the pokeball")




print("***Welcome to the game***.\n*You will need to guess the name of pokemon *")
name=input('Please type in your name: ')
print(f'Great.Lets begin! Good luck {name.title()}\n')
print("Gotta catch 'em all")
pokemon()
print("Thank you for playing.")
print("For any suggestion please mail at nitinmhw@gmail.com")
while True:
	continue