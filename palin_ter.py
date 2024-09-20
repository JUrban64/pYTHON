with open("/Users/jachymurban/Downloads/syn2010_word.vyber-ascii.txt", "r", encoding="utf-8") as f:
    data = f.readlines()
vyhov = []
for x in data: 
    x = x.strip()
    if x == x[::-1] and len(x) >= 4:
        vyhov.append(x)
print(data)
count_slov = len(vyhov)
print(count_slov)

with open("/Users/jachymurban/Desktop/palindromy.txt", "w", encoding="utf-8") as f:
    for x in vyhov:
        f.write(x + "\n")



