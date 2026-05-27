import string
def word_counter(text):
    translation_table=str.maketrans(' ', ' ', string.punctuation)
    text=text.translate(translation_table)
    text=text.split()
    print(len(text))

word_counter("I like my sootcase. I am going to school now! And I eat lunch >:(")
