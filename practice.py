def unique_word():
    chokas =set()
    fin = open("Book1.txt",'r')
    wrd = fin.read()
    fiss = open("Book2.txt",'r')
    lo = fiss.read()
    mega = open("20k.txt",'r')
    ka = mega.read()
    ans =(wrd + lo + ka)
    jng = ans.split()
    for data in jng:
        chokas.add(data)
    print(list(chokas))
unique_word()

def count_the_article():
    a=0
    fin = open("Book1.txt",'r')
    wrd = fin.read()
    fiss = open("Book2.txt",'r')
    lo = fiss.read()
    mega = open("20k.txt",'r')
    ka = mega.read()
    ans =(wrd + lo + ka)
    jng = ans.split()
    for data in jng:
        if data in ["a", "the", "at", "run", "to","and","are","or","for","an","this"]:
            a+=1
    return a

print(count_the_article())

def sorted_words():
    fin = open("Book1.txt",'r')
    wrd = fin.read()
    fiss = open("Book2.txt",'r')
    lo = fiss.read()
    mega = open("20k.txt",'r')
    ka = mega.read()
    ans =(wrd + lo + ka)
    jng = ans.split()
    jng.sort(key=len)
    print(jng)

sorted_words()

def character_word_count():
    a={}
    fin = open("Book1.txt",'r')
    wrd = fin.read()
    fiss = open("Book2.txt",'r')
    lo = fiss.read()
    mega = open("20k.txt",'r')
    ka = mega.read()
    ans =(wrd + lo + ka)
    jng = ans.split()
    for data in jng:
        if data not in a:
            a[data] = 1
        else:
            a[data]+=1
    print(a)
character_word_count()

def start_with_vow():
    a=0
    fin = open("Book1.txt",'r')
    wrd = fin.read()
    fiss = open("Book2.txt",'r')
    lo = fiss.read()
    mega = open("20k.txt",'r')
    ka = mega.read()
    ans =(wrd + lo + ka)
    jng = ans.split()
    for data in jng:
        if data[0] == "a" or "e" or "i" or "u":
            a+=1
    print(a)

start_with_vow()