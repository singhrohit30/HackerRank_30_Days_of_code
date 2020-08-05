# Read a string, S, and print its integer value; if S cannot be converted to an integer, print Bad String

S = input().strip()
try:
    new = int(S)
    print(new)
except Exception as e:
    print("Bad String")