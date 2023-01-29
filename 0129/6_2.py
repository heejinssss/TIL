"""
["h","e","l","l","o"]
["o","l","l","e","h"]

["H","a","n","n","a","h"]
["h","a","n","n","a","H"]
"""

def reversing(words = input()):
    new_words = words[0] + (words[-2:-len(words):-1]) + words[len(words)-1]
    return new_words
    
print(reversing())