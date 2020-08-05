# calculate fine for a library if the book is returned after due date

import datetime

r_day, r_month, r_year = map(int, input().split())
e_day, e_month, e_year = map(int, input().split())

ret_date = datetime.date(r_year, r_month, r_day)
exp_ret_date = datetime.date(e_year, e_month, e_day)
# print(ret_date)
# print(exp_ret_date)
# print(ret_date - exp_ret_date)
if ret_date > exp_ret_date:
    if r_year <= e_year:

        if r_month > e_month:
            fine = 500 * (r_month - e_month)
            print(fine)
        elif r_day > e_day and r_month == e_month:
            fine = 15 * (r_day - e_day)
            print(fine)

    else:
        fine = 10000
        print(fine)
else:
    fine = 0
    print(fine)
