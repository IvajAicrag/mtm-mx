# Python 3 program to find subarray having
# maximum sum less than or equal to sum

# To find subarray with maximum sum
# less than or equal to sum
def findMaxSubarraySum(arr, n, sum):

    # To store current sum and
    # max sum of subarrays
    curr_sum = arr[0]
    max_sum = 0
    start = 0;

    # To find max_sum less than sum
    for i in range(1, n):

        # Update max_sum if it becomes
        # greater than curr_sum
        if (curr_sum <= sum):
            max_sum = max(max_sum, curr_sum)

        # If curr_sum becomes greater than sum
        # subtract starting elements of array
        while (curr_sum + arr[i] > sum and start < i):
            curr_sum -= arr[start]
            start += 1

        # Add elements to curr_sum
        curr_sum += arr[i]

    # Adding an extra check for last subarray
    if (curr_sum <= sum):
        max_sum = max(max_sum, curr_sum)

    return max_sum

# Driver Code
if __name__ == '__main__':
    arr = [6, 8, 9]
    n = len(arr)
    sum = 20

    print(findMaxSubarraySum(arr, n, sum))

# This code is contributed by
# Surendra_Gangwar 
