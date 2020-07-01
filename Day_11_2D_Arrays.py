# Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    add = 0

    tarr = []

    for l in range(0, 4):

        for k in range(0, 4):

            for i in range(l, l + 3):

                for j in range(k, k + 3):

                    if i == l + 1 and (j == k or j == k + 2):

                        continue


                    else:

                        add += arr[i][j]

            tarr.append(add)

            add = 0

    print(max(tarr))
