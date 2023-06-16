def strcount(s): # решение за О()
    mydct = {}
    for sym in s:
        mydct[sym] = mydct.get(sym, 0) + 1

    for key in mydct:
        print(key, mydct.get(key))


strcount('aabcde')
