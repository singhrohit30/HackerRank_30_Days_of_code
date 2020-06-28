# Given an integer,N , print its first 10 multiples. Each multiple n * i (where ) should be printed on a new line
# in the form: n x i = result.


if __name__ == '__main__':
    n = int(input())
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
