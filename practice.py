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
