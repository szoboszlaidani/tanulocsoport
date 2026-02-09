with open('gecisszoveg.txt', 'r', encoding="utf-8") as file:
    oText = file.read()

elvalasztok = [",", ".", "!", "?", "\n", ";", ":", "[", "]", "(", ")"]

for x in elvalasztok:
    oText.replace(x, '')

oText = oText.lower() # itt meg egy str

words = oText.split() # ez egy list

# for word in words:
#     print(word)

# print(f"{len(words)}")

# Hany darab A betuvel kezdodo szavak vannak benne

a_word_list = []
for word in words:
    if word[0] == "a":
        a_word_list.append(word)
else:
    print(len(a_word_list))

a_word_db_counter = 0

for word in words:
    if word[0] == "a":
        a_word_db_counter += 1 # a_word_db_counter = a_word_db_counter + 1 
else:
    print(a_word_db_counter)

rasszizmus_counter = 0
rasszizmus_list = []
for word in words: # words = list, word = str
    if word == "rasszizmus":
        rasszizmus_counter += 1
        rasszizmus_list.append(word)
else:
    print(f"1: {len(rasszizmus_list)}, 2: {rasszizmus_counter}")

rasszizmus_list.sort()

with open('tetszolegesfilename.txt', "w", encoding="utf-8") as file_new:
    file_new.write(str(rasszizmus_list))
    print(rasszizmus_list, file=file_new)