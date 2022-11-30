import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
word = input("Type a word: ").upper()
nato_ver = [nato_dict[_] for _ in word]
print(nato_ver)

