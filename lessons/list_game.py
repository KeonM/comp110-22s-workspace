"""Examples of using lists in a simple game"""


from random import randint
import rlcompleter
 
rolls: list[int] = list() # empty list

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

print(rolls)

# remove item from a list by its index ("pop")
rolls.pop(len(rolls) - 1)
print(rolls)

# Sum values of our rolls
i: int = 0
sum: int = 0 
while i < len(rolls):
    sum += rolls[i]
    i += 1

print(f"total score: {sum}")

# list literal
word = ['the', 'quick', 'fox']
word[0] = "THE"
word.append('!!!')
print(word)

# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)

# #acces indi item
# print(rolls[0])
# print(rolls[1])

# #Access the length of the list
# print(len(rolls))

# # Acess last item of a list
# print(rolls[len(rolls) -  1])