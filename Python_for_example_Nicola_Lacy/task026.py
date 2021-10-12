word = input("Please enter a word to convert it to 'Pig Latin':  ")
word = word.lower()
if word[0:1] == 'e' or word[0:1] == 'y' or word[0:1] == 'u' or word[0:1] == 'i' or word[0:1] == 'o' or word[0:1] == 'a':
    new_word = word + 'way'
    print(new_word)
else:
    new_word = word[1:] + word[0:1] + 'ay'
    print(new_word)

