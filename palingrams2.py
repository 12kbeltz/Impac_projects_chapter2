from load_dictionary import load

word_list = load('words.txt')

def find_palingrams():
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end - i] and rev_word[end-i:] in words:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end - i:] and rev_word[:end-i] in words:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list
            
palingrams = find_palingrams()

palingrams_sorted = sorted(palingrams)

#print("\nNumber of Paligrams = {}\n".format(len(palingrams_sorted)))

#for first, second in palingrams_sorted:
#    print("{} {}".format(first,second))

    
