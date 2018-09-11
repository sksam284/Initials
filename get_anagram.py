#Use this function to get anagrams of word from word_list
def get_anagrams(word, word_list):
    li = []
    word=sorted(word)
    for ana in word_list:
        if word == sorted(ana):
            li.append(ana)
    return li
