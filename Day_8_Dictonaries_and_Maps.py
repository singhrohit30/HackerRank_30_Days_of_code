# Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
# You will then be given an unknown number of names to query your phone book for. For each Name queried, print the associated entry
# from your phone book on a new line in the form name=phoneNumber; if an entry for Name is not found, print Not found instead.

rn = int(input())
phone_book = {}
for _ in range(rn):
    name, number = map(str, input().split())
    phone_book[name] = number
try:
    while True:
        query = input().lower()
        if query == '':
            break
        else:
            res = phone_book.get(query)
            if res is None:
                print('Not found')
            else:
                print(query + "=" + res)
except EOFError:
    pass
