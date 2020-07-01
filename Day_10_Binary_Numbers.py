# Given a base-10 integer,n , convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of
# consecutive 1's in n's binary representation.


if __name__ == '__main__':
    n = int(input())
    rmd = []

    while n > 0:
        rm = n % 2
        n = n // 2
        rmd.append(rm)

    count, result = 0, 0

    for i in range(0, len(rmd)):

        if rmd[i] == 0:

            count = 0

        else:

            count += 1

            result = max(result, count)

    print(result)
