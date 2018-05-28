# Christopher Morey - i.am.chris.morey@gmail.com
# Simple Password List Creation Tool 1.0  (S.P.L.C.T.)
# Intended Purpose : Create password lists based on root word & numbers
# This is my learning to program program, and I have some good ideas where I can go with it
# Any creative criticism is appreciated.
# Planned additions: - capitalization of all letter combinations in root word
#                    - have numbers both before and after root word
#                    - substituting 'Leet Speak' chars in root word, EX: 31337h4xx0r
#                    - importing word list files and adding numbers to the beginning & end of words
# NOTE: This is my first program ever written.

import sys

print('Christopher Morey - Simple Password List Creation Tool 1.0')
print('Creates password lists based on root words and numbers')

#name_of_file = input("What is the name of the file: ")
#completeName = name_of_file + ".txt"
#print('Your file will be saved as ' + completeName)
#At the end of this, "completeName" is the name of the file


print('Please input your root word:')
rootWord = input()
rootWord = rootWord.rstrip()
#Takes in "rootWord" and strips any extra spaces at the end


#This is before the word stuff
print('Do you want to add numbers before the word?')
before = input("'Y or N'")

if before == 'y' or before == 'Y':
    print('How high do you want to count before the word?')
    pre = int(input("Enter a number: "))
# creates integer value "pre" of highest number before w


#This is after the word stuff
print('Do you want to add numbers after the word? Y/N')
after = input("'Y or N'")

if after == 'Y' or after == 'y':
    print('How many digits do you want to go to after the word?')
    post = int(input("Enter a number: "))
#creates integer value "post" of highest number after word

if before == 'y' or before == "Y":
    preCount = pre + 1
    for preCount in range(preCount):
        print(str(preCount) + rootWord)
        preCount = preCount - 1

if after == 'Y' or after == 'y':
    postCount = post + 1
    for postCount in range(postCount):
        print(rootWord + str(postCount))
        postCount = postCount - 1





