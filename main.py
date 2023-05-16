import random

#Play/exit inspiration 
#StackOverflow: https://stackoverflow.com/questions/34096822/hangman-assignment-python

play = 1
exit = 2


print("If you would like to play HANGMAN, input 1.")
print("If you would like to EXIT, input 2.")
choice = int(input(""))

def exits():
    print("Goodbye!")
    
while choice == exit:
    exits()
    break

while choice == play:
    word = ['intricate', 'lamb','duck', 'calculator', 'phone', 'electric',
    'water', 'door', 'giraffe', 'coffee', 'tennis', 'soccer', 'football', 'psychology',
    'animals', 'hangan', 'superman', 'shazam', 'telephone', 'avenue', 'tawiwan','japan',
    'canada', 'dungeon', 'imagine', 'simple', 'medium', 'hard', 'easy','jazz', ''
    'sandwhich','batman', 'python', 'chairs','tomatoe', 'turkey']
    
    print("You have 8 attempts at guessing the word. ")
    correct_wrd = random.choice(word)
    print("The word is " + str(len(correct_wrd)) + " letters long.")
    attempts = 8
    correct_ltrs = []
    letters_used = []
# This code shows the underlined spaces, replacing them with letters when the user guesses correctly

    while attempts != 0:
        line = ""
        for i in correct_wrd:
            if i in correct_ltrs:
                line += i + " "
            else: 
                line +="_ "
        print(line)
        print("")
# If the user guesses incorrectly, the amount of attempts go down.           
        letter = input("Input Letter:").lower()
        if letter in letters_used:
            print("That letter has already been used.")
            attempts +=1
        else:
            letters_used.append(letter)
            

        print("Your used letters are: ", (", ").join(letters_used))
        
        correct_ltrs.append(letter)
        if letter in correct_wrd: 
            print("Correct!")
        else:
            attempts = attempts - 1
            print("Incorrect. You have " + str(attempts) +" attempts left.")
        
# This code outputs the end, Win or Lose, and if user would like to play agian.
        if attempts == 0:
            print("You lost! The word was " + correct_wrd.upper() + ".")
#       From codehs Docs
            again = input("Play Again? Y/N ").upper()
            if again == 'Y':
                choice = 1
                
            elif again == 'N':
                choice = 2
                print("Thanks for playing. Goodbye!")
                break
            else:
                print("I'll take that as a no. Goodbye!")
                
        elif set(correct_wrd) <= set(correct_ltrs): 
            print("YOU WIN! The word was " + correct_wrd.upper() +".")
            again = input("Play Again? Y/N ").upper()
            if again == 'Y':
                break
                choice = 1
                
            elif again == 'N':
                choice = 2
                print("Thanks for playing. Goodbye!")
                break
                
            else:
                choice = 2
                print("I'll take that as a no. Goodbye!")
                break
            
#Y/N question inspiration
#Stackoverflow: https://stackoverflow.com/questions/59442258/effecient-way-to-repeat-y-n-question-in-python
