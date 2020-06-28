# Given a string,S , of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters

# as 2 space-separated strings on a single line (see the Sample below for more detail).

for i in range(int(input())):
    s = input()
    print(*["".join(s[::2]), "".join(s[1::2])])
