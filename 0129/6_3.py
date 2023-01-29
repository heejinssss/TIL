"""
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
# "ball"
"""
from collections import Counter

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

words = paragraph.lower()

for ban in banned:
    words = words.replace(ban,'')

for word in words:
    if (word.isalpha() or word == ' '):
        continue
    words = words.replace(word,'')

dict_words = dict(Counter(words.split()))
max_key = max(dict_words.values())
for key, value in dict_words.items():
    if value == max_key:
        print(key)