"""
"A man, a plan, a canal: Panama" # True
"race a car" # false
대소문자 구분 없고 영문자와 숫자만 입력 가능
"""

letters = input()

for letter in letters:
    if (letter.isdigit() or letter.isalpha()) is True: # 숫자이거나 알파벳이면
        continue
    letters = letters.replace(letter,'').lower()

print(True) if letters == letters[::-1] else print(False)