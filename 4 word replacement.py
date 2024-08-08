def replace_word():
    str = "hi guys, this is sentence to replace"
    word_to_replace = input("Enter the word to be replaced: ")
    word_replacement = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word_replacement))

replace_word()