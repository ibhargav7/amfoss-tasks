arr = []
for i in range(100, 1000):
    for j in range(100, 1000):
        a = i * j
        if str(a) == str(a)[::-1] and a not in arr:
            arr.append(a)
arr.sort()            
x=int(input())
for j in range (x):
    n=int(input())
   
    
    b = len(arr)
    for i in range (a):
        if arr[i] >= n:
            
            print(arr[i-1])
            break
