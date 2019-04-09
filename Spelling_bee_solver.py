# Author: Vincent Emond
# Solver for the spelling bee game found on the NYT Crosswords website
# Full rules and game can be found there. Rules are as follows.
# ----------------RULES---------------------------------
# Words must contain at least 4 Letters
# Words must include the center (special) letter
# Words may not be proper nouns or hyphenated
# Letters can be used more than once
#-------------------------------------------------------


# clean and reduce word list to words with > 3 characters
f = open("words.txt","r")
words = f.read().strip().split("\n")
words = [word.lower() for word in words if len(word) > 3]
f.close()

#initialize alphabet
alph = 'abcdefghijklmnopqrstuvwxyz'
alph = list(alph)

# Enter the special letter
while True:
    special_letter = str(input("Enter the special letter: ").lower())
    if len(special_letter)>1:
        print("Input only one special letter")
    elif special_letter not in alph:
        print("Enter a letter from the alphabet")
    else:
        break

# Enter the other letters
while True:
    other_letters = list(str(input("Enter the 6 other letters: ")).replace(' ',''))
    if len(other_letters)>6:
        print("Only 6 letters!")
    elif special_letter in set(other_letters):
        print("Can't use same letter")
    elif set(other_letters).isdisjoint(set(alph)) is True:
        print("Letters you fool!")
    else:
        break

# remove entered letters from alphabet
if special_letter in alph:
    alph.remove(special_letter)

for i in other_letters:
    if i in list(alph):
        alph.remove(i)

#sort words
othwords = []
for w in words:
    if not any(letter in w for letter in alph):
        othwords.append(w)
spcwords = [w for w in othwords if special_letter in w]


print("The solution for the spelling bee with special letter:")
print(list(special_letter))
print("And other letters:")
print(other_letters)
print("Are as follows: ")
print(spcwords)
print("Kind of...This scrabble dictionary has some crazy words in it. It found {} solutions" .format(len(spcwords)))
