# Consider a database table, Emails, which has the attributes First Name and Email ID. Given N rows of data simulating
# the Emails table, print an alphabetically-ordered list of people whose email address ends in '@gmail.com' .

import re

if __name__ == '__main__':
    N = int(input())
    names = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
    email = re.findall(r"@gmail.com$", emailID)		# Alternate method
                                                    # if re.search(r'@gmail.com$', emailID):
                                                        # names.append(firstName)
    if len(email) != 0:
        names.append(firstName)

names.sort()
for name in names:
    print(name)
