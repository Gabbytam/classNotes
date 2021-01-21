class Word():
    def __init__(self, chosen_word):
        self.word = list(chosen_word)
        self.guesses = []
        #cap is the amount of wrong guesses a user is allowed
        self.cap = 8
        self.fill = ['_'] * len(chosen_word)
        self.over = False
    
    def play_game(self):
        #game will run code in while statement until self.over is True --> game over
        while self.over == False:
            print(' '.join(self.fill))
            letter = input('Guess a letter: ' )
            #check if letter is in list 
            if letter in self.word: 
                #while statement is used to do a check for multiple letter occurances 
                while letter in self.word:
                    # get the index of the letter so it can be replaced in the word and also the fill
                    index = self.word.index(letter)
                    # get the word and replace the letter with * so it doesnt keep finding the same index location
                    self.word[index] = '*'
                    # fill the blank with the letter 
                    self.fill[index] = letter
            # else statement runs if the letter is not in the word
            else: 
                print('letter is not in word')
                #this is where you would add the guesses if its not in the word and if they havent guessed it already
                # checks also if the letter isnt in the correctly guessed 
                if letter not in self.guesses and letter not in self.fill: 
                    self.guesses.append(letter)

            #this code will run after every input 
            #do a check if the word is filled
            if '_' in self.fill:
                print('Letters Guessed: ', self.guesses)
                print('Guesses remaining: ', self.cap - len(self.guesses))
            else:
                print(' '.join(self.fill))
                print('Game over! Winner!')
                self.over = True
            # check if user is out of guesses, if they are, change status of 'game' over to True
            if self.cap == len(self.guesses):
                self.over = True
            print('')
        #this code will only run when self.over (game over) is True
        # and another check to see if the fill has not been filled 
        if '_' in self.fill:
            print('You are out of guesses, your man is HUNG')



# python = Word('python')
# python.play_game()

poppy = Word('poppy')
poppy.play_game()



#assigment:
# have a Word class 
# it should print the letters of a word to be guessed like _ _ _ _ _ _
# have user guess a letter: if they guess a letter in the word, replace the _ with the letter and print it
# give them praise if they guess a right letter
#if the guessed letter completes the word, print Game over, Winner! (game should stop, no more prompting)
# if user guesses wrong letter, print a message saying wrong
# if that guess uses up the remaining guess, print game over, LOSER! (game should stop)
# if the game is not over, after each guess, it should tell the user how mant guesses are remaining and which letters they have already guessed, reprint the word with blanks

# CODE WITHOUT COMMENTS
# class Word():
#     def __init__(self, chosen_word):
#         self.word = list(chosen_word)
#         self.guesses = []
#         self.cap = 8
#         self.fill = ['_'] * len(chosen_word)
#         self.over = False
    
#     def play_game(self):
#         while self.over == False:
#             print(' '.join(self.fill))
#             letter = input('Guess a letter: ' )
#             if letter in self.word: 
#                 while letter in self.word:
#                     index = self.word.index(letter)
#                     self.word[index] = '*'
#                     self.fill[index] = letter
#             else: 
#                 print('letter is not in word')
#                 if letter not in self.guesses and letter not in self.fill: 
#                     self.guesses.append(letter)

#             if '_' in self.fill:
#                 print('Letters Guessed: ', self.guesses)
#                 print('Guesses remaining: ', self.cap - len(self.guesses))
#             else:
#                 print(' '.join(self.fill))
#                 print('Game over! Winner!')
#                 self.over = True
#             if self.cap == len(self.guesses):
#                 self.over = True
#             print('')
#         if '_' in self.fill:
#             print('You are out of guesses, your man is HUNG')