from sys import stdin

arr = [tuple(map(int, stdin.readline().rstrip().split())) for _ in range(3)]

if arr[0][0] == arr[1][0] == arr[2][0] or arr[0][1] == arr[1][1] == arr[2][1]:
    print("WHERE IS MY CHICKEN?")
else:
    if arr[1][0]-arr[0][0] == 0:
        print("WHERE IS MY CHICKEN?") if arr[1][1] == arr[1][0]*(arr[2][1]-arr[0][1]/arr[2][0]-arr[0][0]) else print("WINNER WINNER CHICKEN DINNER!")  
    else:
        print("WHERE IS MY CHICKEN?") if arr[2][1] == arr[2][0]*(arr[1][1]-arr[0][1])/(arr[1][0]-arr[0][0]) else print("WINNER WINNER CHICKEN DINNER!")
