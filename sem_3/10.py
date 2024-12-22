text = input().lower()
punctuation = ",.!?;:-()[]{}\"'<>"
for char in punctuation:
    text = text.replace(char, "")
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
min_frequency = min(word_count.values())
rare_words = [word for word, count in word_count.items() if count == min_frequency]
print(min(rare_words))
