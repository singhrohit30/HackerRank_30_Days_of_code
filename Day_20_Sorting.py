# Printing the Number of Swaps taken and also the first and last element of an array sorted using Bubble Sort.

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swaps = 0
for i in range(len(a)):
    for j in range(1, len(a)):
        if a[j - 1] > a[j]:
            swaps += 1
            a[j - 1], a[j] = a[j], a[j - 1]
print(f'Array is sorted in {swaps} swaps.')
print('First Element:', a[0])
print('Last Element:', a[-1])
