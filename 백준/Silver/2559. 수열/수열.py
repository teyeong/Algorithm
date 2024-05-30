def max_temperature(arr, N, K):
    temp_sum = sum(arr[:K])
    max_sum = temp_sum
    for i in range(N - K):
        temp_sum = temp_sum - arr[i] + arr[i + K]
        if max_sum < temp_sum:
            max_sum = temp_sum
    return max_sum

N, K = map(int, input().split())
arr = list(map(int, input().split()))

print(max_temperature(arr, N, K))