import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')


display = [];
length = len(chosen_word)
for _ in range(length):
  display += "_";
print(display);

guess = input("Guess a letter: ").lower()


for position in range(length):
   letter = chosen_word[position]
   if letter == guess:
     display[position] = letter
  


print(display)