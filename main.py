spaceIndices = []
WordBank = []
spam = "As the stock of Tesla goes up, the cost continues to rise with it. This is very intimidating to other electric car companies."

print(spam)
newSpam = spam.strip()
print(newSpam)

print(newSpam.find(" "));

print(newSpam.rfind(" "));

letters = newSpam
i = 0
for let in letters:
  print(str(i) + " - " + let)
  if(let == (" ")):
    spaceIndices.append(i)
  i = i+1

print(spaceIndices)

for let in letters:
  print(str(i))