# Split Array Largest Sum

def kth_max_sum(arr, window_size):
    arr_size = len(arr)
    if arr_size < window_size:
        print("Invalid operation the window size can't be less than arr size")
        return -1
    window_sum = sum(arr[i] for i in range(window_size))
    max_sum = window_sum
    
    for i in range(arr_size - window_size):
        window_sum = window_sum - arr[i] + arr[i+window_size]
        max_sum = max(max_sum, window_sum)
    return max_sum




k = 2
# arr = [80, -90, 100, -1200, 200]
arr = [80, -50, 90, 100]

print(kth_max_sum(arr, k))




# broth force way
def k_max_sum(arr, k):
    max_sum = float('-inf')
    n = len(arr)
    for i in range(n-k+1):
        current_sum = 0
        for j in range(k):
            current_sum += arr[i+ j]
        max_sum = max(max_sum, current_sum)
    return max_sum
        

print(k_max_sum(arr, k))