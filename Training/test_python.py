from collections import defaultdict
sentence = 'hello world hello world welcome to python'

words = sentence.split()
# Normal Dic
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

print(word_count)

# Using defaultdict
dd = defaultdict(int)
for word in words:
    dd[word] += 1
