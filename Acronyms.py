stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
org = "The organization for health, safety, and education"
acro = []

for word in org.split():
    if word in stopwords:
        pass
    else:
        acro.append(word[0].capitalize())
print("".join(acro))