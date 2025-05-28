#binary search only works when the array is sort by order


def binary_search(arr, low, high, x):
    while low <= high:
        mid = (low + high) // 2
        if  x == arr[mid]:
            return mid
        elif x > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 2, 5, 10, 20, 22, 25, 27, 28, 29, 30, 31, 50, 100, 200, 1000]
x = 20

result = binary_search(arr, 0, len(arr) - 1, x)

if result == -1:
    print("Element not found")
else:
    print("Element found lenght:", result, "and the number is: ", arr[result])




