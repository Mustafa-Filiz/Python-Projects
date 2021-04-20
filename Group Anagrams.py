# My solution
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
length_words = len(words)

anagrams1 = []
anagrams2 = []
anagrams3 = []

i = 0
for i in range(length_words):
  if "e" in words[i]:
    if "a" in words[i]:
      if "t" in words[i]:
        anagrams1.append(words[i])
  
  elif "n" in words[i]:
    if "a" in words[i]:
      if "t" in words[i]:
        anagrams2.append(words[i])
        
  else :
       anagrams3.append(words[i])
i += 1

print(anagrams1, anagrams2, anagrams3, sep = "\n")

# Answer

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

set_words = []
result = []

for x in words:
  if set(x) not in set_words:
    set_words.append(set(x))

for y in range(len(set_words)):
  result.append([x for x in words if set(x) == set_words[y]])

print(result)