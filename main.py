import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list);
print(chosen_word)
guess = input("guess a letter").lower()

if guess in chosen_word:
    print("yes")
else: 
    print("false")