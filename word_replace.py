def replace_word():
    str = input("Enter a message you want to display: ")
    word_to_replace = input("Enter word you want to replace : ")
    word_replacement = input("Enter the replacement for the word : ")
    print(str.replace(word_to_replace, word_replacement))

replace_word()