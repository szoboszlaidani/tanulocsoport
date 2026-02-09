with open("órai/forras.txt","r", encoding="UTF-8") as file:
    text=file.read()

sep=[",",".",";",":","(,",")","[","]","!","?","\n"]
for c in sep:
    text=text.replace(c," ")

text=text.lower()
words=text.split()
print(len(words))
print(f"{words.count(input("írj be egy szót | "))} - szor szerepel")
print(words.sort())
print(words.sort(reverse=True))

szereplobetu=input("írj egy betűt")
count=0
for w in words:
    if szereplobetu[0] in w: count+=1
print(f"{count}-szor szerepel")

alen=0
for w in words:
    alen+=len(w)
print(f"össz {alen} karakter hosszú")