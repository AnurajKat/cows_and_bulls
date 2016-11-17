from random import randint
import sys, argparse, csv


def take_word_from_file():
    list_words =[]
    with open('word_dictionary.csv', newline='') as csvfile:
        list_of_words = csv.reader(csvfile)
        for line in list_of_words:
            list_words.append(line[randint(0, len(line)) - 1])
    word = list_words[randint(0, len(list_words)-1)]
    return word


def check_bull_and_cow(test_word,word):
    bulls = 0
    cows = 0
    result = False
    if word == test_word:
        return True#result = "4 bulls! You won!"
    else:
        for i in test_word:
           # print(i)
            if i in word:
                #print('it came here')
                if word.find(i) == test_word.find(i):
                 #   print('bull')
                    bulls += 1
                else:
                  #  print('cow')
                    cows += 1
        if cows > 0 or bulls > 0:
            print("bulls :",bulls," and cows :&",cows)
        else:
            print(" Sorry no dommesticated animals which are brutally murdered for food. :(")
        return result


def game_of_cows_and_bulls():
    word=take_word_from_file()
    correct_result = True
    result = False
    print('4 letter word selected from file')
    while True:
        input_word = input('Guess the 4letter word, bitch :')
        result = check_bull_and_cow(input_word,word)
        if result == correct_result:
            print(result)
            break
        else:
            print(result)


def loop_for_game():
    while True:
        print("do you want to play cows and bulls ?")
        decision = int(input('0 for no and 1 for yes. please be gentle :'))
        if decision == 0:
            break
        else:
            game_of_cows_and_bulls()


loop_for_game()