text = input("Enter your phrase: \n")
long_words = []

for word in text.split():
    if len(word) > 10:
        long_words.append(word)

if long_words:
    print("Long words found: \n")
    for word in long_words:
        print(word)
else:
    print("No long words found.")