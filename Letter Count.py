sentence = input("Enter a sentence : ")
empty_dict = {}
for item in sentence:
    if item not in empty_dict:
        empty_dict[item] = sentence.count(item)

print(empty_dict)