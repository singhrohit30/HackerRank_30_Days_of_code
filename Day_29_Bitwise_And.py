# Given set S= {1,2,3,...N}. Find two integers, A and B (where A<B ), from set S such that the value of A&B is the maximum
# possible and also less than a given integer,K . In this case, & represents the bitwise AND operator.

import math


def getAnswer(n, k):
    power = int(math.log(n, 2)) - 1
    floor = 2 ** power

    maxNum = 0
    for i in range(floor + 1, n + 1):
        for j in range(1, i):
            test = i & j
            if maxNum < test < k:
                maxNum = test
        if maxNum == k - 1:
            break
    return maxNum


if __name__ == '__main__':
    t = int(input())

    for a in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        print(getAnswer(n, k))

# A naive approach works for few test cases

'''
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        s = ()
        for values in range(1, n + 1):
            s.add(values)
        s = list(s)
        value_set = []
        for i in range(len(s)):
            for j in range(1, len(s)):
                and_op = s[i] & s[j]
                value_set.append(and_op)
        value_set.sort()
        value_set.reverse()
        for vals in value_set:
            if vals < k:
                print(vals)
                break'''
