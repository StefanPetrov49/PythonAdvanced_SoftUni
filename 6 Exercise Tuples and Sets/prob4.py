sentence = input()
dictionary = {}
list_sentence = list(sentence)

for el in list_sentence:
    if el not in dictionary:
        dictionary[el] = 0
    dictionary[el] += 1

for letter in sorted(dictionary):
    print(f"{letter}: {dictionary[letter]} time/s")