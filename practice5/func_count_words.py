def count_words(sentence):
    s_list = sentence.split(' ')
    return len(s_list)

print("단어 수:"+ str(count_words("This is sample test sentence")))