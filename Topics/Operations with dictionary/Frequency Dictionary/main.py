text = input().lower()
words = text.split()
freq_word = {}
for word in words:
    freq_word.setdefault(word, 0)
    freq_word[word] += 1
for word in freq_word:
    print(f'{word} {freq_word[word]}')
