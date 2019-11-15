from load_dictionary import load

palindromes = []

for word in load('words.txt'):
    if word == word[::-1]:
        palindromes.append(word)

            
