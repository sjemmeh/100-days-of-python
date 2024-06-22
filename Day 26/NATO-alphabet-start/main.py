import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')
# Keyword Method with iterrows()

#TODO 1. Create a dictionary in this format:
nato = {row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name_normal = input("Enter a word to convert to nato alphabet: ").upper()
name_nato = [nato[letter] for letter in name_normal]

print(name_nato)