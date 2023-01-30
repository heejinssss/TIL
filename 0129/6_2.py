"""
["h","e","l","l","o"]
["o","l","l","e","h"]

["H","a","n","n","a","h"]
["h","a","n","n","a","H"]
"""
s = ["h","e","l","l","o"]

def reverseString(s):
    new_s = list(reversed(s))
    return new_s
    
print(reverseString(s))