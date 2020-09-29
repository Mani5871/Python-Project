#!/usr/bin/env python
# coding: utf-8

# In[1]:


def play_again():
    
    play = input("Type yes to play again or type no to quit the game")
    if play == 'yes':
        return True
    return False

def tostring(string):
    
    string1 = ''
    
    for ele in string:
        string1 += ele
    return string1

import random

name = input("Enter your name")
print()
print(f"Hello {name} ! Welcome to this guessing game")

words = ['apple','banana','kite','square','rectangle','laptop','keyboard','mouse',
         'computer','printer','python','java','scanner','numpy','dynamic','king','ear',
         'cricket','football','rugby','tennis','badminton','scale','pen','pencil'
        ]
play =True

while play == True:
    
    ind = random.randint(0, len(words))
    word = words[ind]
    guess = ['_'for i in range(0, len(word))]
    chances = 10
    cnt = 3
    index = random.sample(range(0,len(word)),3)

    for i in index:
        guess[i] = word[i]
    for i in guess:
        print(i, end = ' ')
    
    print()
    print(f"You have to guess a {len(word)} letter word")

    while chances > 0:
        print()
        ch = input("Enter your guessing character")
        flag = 0

        for ind, char in enumerate(word):
            if ch == char:
                flag = 1
                guess[ind] = ch
                cnt += 1

        for i in guess:
            print(i, end = '  ')
        print()

        if word == tostring(guess):
            print("Congratulations you have won the game")
            print()
            print(f"Your score is {chances} out of 10")
            break
            
        if flag == 0:
            chances -= 1

        print()
        print(f"You have {chances} chances remaining")

    if chances == 0:
        print("Better luck next time")
    
    play = play_again()
        
print()
print(f"Have a nice day {name}:)")


# In[ ]:




