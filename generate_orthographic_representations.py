import pandas as pd

orth_info = pd.read_csv("orth_words.csv")
letters = pd.read_csv("letter_vectors.csv")

for orth in orth_info.loc[:,'orth']: # index through the orthographic word forms themselves
    orth_index = orth_info.index[orth_info.orth == orth][0] # get the row index of each orthographic word form
    orth_centered = orth_info.loc[orth_index, 'orth_centered'] # get the centered vesio of that orthographic word form

    rep = []
    for letter in orth_centered:
        letter_rep = letters.loc[:,letter]
        letter_rep = letter_rep.tolist()
        for unit_value in letter_rep:
            rep.append(unit_value)
    print(orth, rep, len(rep))
