# check whether a number is prime or not

import math
test_case = int(input())
for _ in range(test_case):
    num = int(input())
    if num == 1:
        print('Not prime')
    else:
        sq = int(math.sqrt(num))
        p = all((num % numbers != 0) for numbers in range(2, sq+1))
        if p:
            print("Prime")
        else:
            print("Not prime")
