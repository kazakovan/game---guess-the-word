import random

def play_game():
    lives = 8
    known_letters = set()
    final_phrase = 'You are hanged!'
    hidden_word = random.choice(['python', 'java', 'kotlin', 'javascript'])
    hidden_word_set = set(hidden_word)
    input_set = set()
    while lives > 0:
        s = ''
        for i in hidden_word:
            if i in hidden_word_set:
                s += '-'
            else:
                s += i
        print(s)
        entered_letter = input('Input a letter:')
        if len(entered_letter) != 1 or entered_letter == ' ':
            print('You should input a single letter')
        elif entered_letter in input_set:
            print('You already typed this letter')
        elif entered_letter in hidden_word_set:
            hidden_word_set.remove(entered_letter)
        elif entered_letter not in 'qwertyuiopasdfghjklzxcvbnm':
            print('It is not an ASCII lowercase letter')
        else:
            print('No such letter in the word')
            lives -= 1
        if hidden_word_set == set():
            final_phrase = '''You guessed the word!
    You survived!'''
            break
        if lives == 0:
            break
        print()
        input_set.add(entered_letter)
    print(final_phrase)
print('H A N G M A N\n')
while True:
    play_or_exit = input('Type "play" to play the game, "exit" to quit:')
    if play_or_exit == 'play':
        play_game()
        break
    if play_or_exit == 'exit':
        break    
