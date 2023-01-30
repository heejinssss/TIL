# """
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# # "ball"
# """
from collections import Counter

# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# paragraph = "a, a, a, a, b,b,b,c, c"
paragraph = "abc abc? abcd the jeff!"

# banned = ["hit"]
# banned = ["a"]
banned = ["abc","abcd","jeff"]

for word in paragraph:
    if (word.isalpha() or word == ' '):
        continue
    paragraph = paragraph.replace(word,' ')

words = paragraph.split(' ')


# pwd = "/appl/python/version3/bin/python"
# # change the string to a  list
# PWD = pwd.split("/")                   # will return ['', 'appl', 'python', 'version3', 'bin', 'python']
# Ver =  [itr for itr in PWD if "version" in itr] # Ver is a list ['version3']
# Ver = "".join(Ver)                               # Change list to a string



while True:
    for ban, word in banned, words:
        if ban in words:
            words.replace(words,'')

words = ' '.join(words).split()


print(words)


dict_words = dict(Counter(words))
print(dict_words) # 삭제
max_key = max(dict_words.values())
for key, value in dict_words.items():
    if value == max_key:
        print(str(key))
