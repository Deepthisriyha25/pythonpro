
"""def evenodd(x):
    if x%2 == 0:
        print(f"{x} is a Even Number")
    else:
        print(f)"""

"""for i in range(8):
    if i == 6:
        continue
    print(i)"""

"""def palindrome(str):
    op = ""
    for x in range(len(str)-1,-1,-1):
        op += str[x]
    print(op)
    if(str == op):
        print(f" {str} is palindrome")
    else:
        print(f" {str} is not a palindrome")
str = input("Enter String: ")
palindrome(str)"""

"""tr="FULL_ST_A_CK"
op = ""
for i in range(len(str)):
    if (str[i] =="_"):
        continue
    op += str[i]
print(op)



"""
"""k = ["HELLO", "hi", "PYTHON", "css", "js", "react", "DJANGO"]
for word in k:
   if word == word.upper():
     print(word)
for word in k:
    if word == word.lower():
       print(word)"""

skills = ["python-Easy", "java-difficult", "js-eaSy", "react-easY", "html-eAsy", "git-moDerate"]
for x in skills:
    if x.lower().find("easy") != -1:
        print(x)