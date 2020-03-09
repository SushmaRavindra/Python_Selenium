# Anagram
# 'silent' 'listen' 'tea' 'ate'
def is_anagram(word1, word2):
    if word1.lower() == word2.lower():
        return False
    t1 = sorted(word1.lower())
    t2 = sorted(word2.lower())
    if ''.join(t1) == ''.join(t2):
        return True
    else:
        return False


# Remove Duplicates.
def unique_only(iterable):
    unique = set()
    for item in iterable:
        if item not in unique:
            unique.add(item)
    return unique


# words count (Using Dict Comprehension)
def word_count(iterable):
    return {item: iterable.count(item) for item in iterable}


# words count (Using Counter Object)
def word_count(iterable):
   from collections import Counter
   return Counter(iterable)


# words count (Using DefaultDict)
def word_count(iterable):
   from collections import defaultdict
   d = defaultdict(int)
   for item in iterable:
       d[item] +=1
   return d


# tail
def tail(iterable, n):
    return iterable[-n:]


# Reverse the Values in the Dictionary if the type is String.
d = {'a': 'hello', 'b': 10, 'c': 10.3, 'd': 'world'}
for key, value in d.items():
    if isinstance(value, str):
        temp = ''.join(reversed(value))
        d.update({key: temp})



