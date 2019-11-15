from load_dictionary import load

palindromes = []

word='kayak'

def palindromes_recur(word, beg, end):
    if word[beg] == word[end] and (beg + 1) < (len(word) // 2):
        palindromes_recur(word, beg + 1, end -1)
    if word[beg] == word[end] and (beg + 1) == (len(word) // 2):
        palindromes.append(word)



for word in load('words.txt'):
    palindromes_recur(word, 0, len(word)-1)

