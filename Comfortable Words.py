alphabet_left = set("qwertasdfgzxcvb")
alphabet_right = set("yuıophjklnmi")
word1 = set("tester")
word2 = set("polly")
word3 = set("clarusway")

print(bool((word1 - alphabet_left) and (word1 - alphabet_right)))
print(bool((word2 - alphabet_left) and (word2 - alphabet_right)))
print(bool((word3 - alphabet_left) and (word3 - alphabet_right)))
