from datetime import date, datetime
from sty import fg, bg
from PyDictionary import PyDictionary
import random
import ast
import sys

print("Wordle Simulator 2022\nDeveloped by Pubudu Wijesinghe\n")

with open('word_list.txt', 'r') as datafile:
    data = datafile.readlines()
    word_list = ast.literal_eval(data[0])
    check_list = ast.literal_eval(data[1])

print("Select the Game Type:\n1. Today's Word\n2. Custom\n3. Random")
type = input("Make your choice: ")

if type == '1':
    day_of_year = datetime.now().timetuple().tm_yday
    idx = 861 + day_of_year
    print(f"\nYou're playing Wordle #{idx}")
    word = word_list[idx]
elif type == '2':
    month = input("Enter the Month: ")
    day = input("Enter the Day: ")
    day_of_year = date(2022,int(month),int(day)).timetuple().tm_yday
    idx = 861 + day_of_year
    print(f"\nYou're playing Wordle #{idx}")
    word = word_list[idx]
elif type == '3': word = random.choice(word_list)
else: 
    print("Invalid Choice!")
    sys.exit()

guess=0
while guess<6:
    word_user = str(input(f"Enter your guess {guess+1}: "))
    ctr = 0
    if word_user in word_list or word_user in check_list:
        for i in range(len(word_user)):
            if word_user[i] == word[i]:
                print(fg.black + bg.green + f"{word_user[i].upper()} " + bg.rs + fg.rs, end='')
                ctr+=1
            elif word_user[i] in word: print(fg.black + bg.yellow + f"{word_user[i].upper()} " + bg.rs + fg.rs, end='')
            else: print(fg.black + bg.grey + f"{word_user[i].upper()} " + bg.rs + fg.rs, end='')
        if ctr == 5:
            print("", end='\n')
            print(random.choice(["Impressive!", "Awesome!", "Great Job!"]))
            break
        print("", end='\n')
    else:
        print("Invalid guess")
        guess -= 1
    guess += 1
dict = PyDictionary()
meaning = dict.meaning(word)
print(f"Answer: {word.upper()}\n{meaning}")