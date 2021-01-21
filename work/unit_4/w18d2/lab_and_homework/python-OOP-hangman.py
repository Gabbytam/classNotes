class Word():
    def __init__(self, chosen_word):
        self.word = list(chosen_word)
        self.guesses = []
        #cap is the amount of wrong guesses a user is allowed
        self.cap = 6
        self.fill = ['_'] * len(chosen_word)
        self.over = False
    
    def print_word(self):
        print(self.word)
        print(self.fill)
    
    def play_game(self):
        while self.over == False:
            letter = input('Guess a letter: ' )
            print(letter)
            #check if letter is in list 
        
            #while not ValueError, keep checking 
            while True:
                try:
                    index = self.word.index(letter)
                    print('where it at', index)
                    # get the word and replace the letter with -
                    # self.word = self.word.pop(index)
                    self.word.slice(index, index + 1)

                except ValueError:
                    print('letter is not in word')
                    #this is where you would add the guesses
                    #append it to guesses only if its not in the word
                    #also do a check to see if user has already guessed the letter
                    if letter not in self.guesses: 
                        self.guesses.append(letter)
                    break
                else:
                    print('you guessed right!')
                    #this is where you will replace the fill with the letters at the index
                    break

            #this happens after every input 
            print('Letters Guessed: ', self.guesses)
            print('how many guesses', len(self.guesses))
            # check if user is out of guesses
            if self.cap == len(self.guesses):
                self.over = True
        #this code will only run when self.over is True, meaning user is out of guesses
        print('You are out of guesses, your man is HUNG')




python = Word('pythonp')
python.print_word()
python.play_game()

# some variables here to prepare the wordlist, initialize things like
# `remaining_guesses` (start a round with 8), `letters_used`, the `chosen_word` (randomly
# chosen from a list of words you also declare here perhaps?),
#and whatever else you might want to keep track of


# a loop here that will cause game to play and be exited when user either wins or loses
# see below for tips on how to structure this loop

#assigment:
# have a Word class
# it should print the letters of a word to be guessed like _ _ _ _ _ _
# have user guess a letter: if they guess a letter in the word, replace the _ with the letter and print it
# give them praise if they guess a right letter
#if the guessed letter completes the word, print Game over, Winner! (game should stop, no more prompting)
# if user guesses wrong letter, print a message sating wring
# if that guess uses up the remaining guess, print game over, LOSER! (game should stop)
# if the game is not over, after each guess, it should tell the user how mant guesses are remaining and which letters they have already guessed, reprint the word with blanks
