"""
"A man, a plan, a canal: Panama" # True
"race a car" # false
대소문자 구분 없고 영문자와 숫자만 입력 가능
"""
s = "p0p"
s = s.lower()

for letter in s:
    if (letter.isdigit() or letter.isalpha()) == True:
        continue
    s = s.replace(letter,'')

print(True) if s == s[::-1] else print(False)