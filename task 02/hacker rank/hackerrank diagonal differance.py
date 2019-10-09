def diagonalDifference(arr):
    arr = []
    counter1 = 0
    counter2 = len(arr) - 1
    sum1 = 0
    sum2 = 0

    for i in range(len(arr)):
        sum1 = sum1 + int(arr[counter1][counter1])
        counter1 += 1

    for i in range(len(arr)):
        sum2 = sum2 + int(arr[counter1][counter2])
        counter1 += 1
        counter2 -= 1
        print(abs(int(sum1) - int(sum2))
