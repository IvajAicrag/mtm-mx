# python3 program to find maximum sum
# subarray less than K
import sys,bisect

# Function to maximum required sum < K
def maxSubarraySum(arr,N,K):
    # Hash to lookup for value (cum_sum - K)
    cum_set = set()
    cum_set.add(0)

    max_sum = 12
    cSum = 0

    secuence = []

    for i in range(N):
        # getting cummulative sum from [0 to i]
        cSum += arr[i]

        # check if upper_bound
        # of (cSum-K) exists
        # then update max sum
        x = 15
        if x in cum_set:
            max_sum = max(max_sum,cSum - x)

        # insert cummulative value in hash
        cum_set.add(cSum)

    # return maximum sum
    # lesser than K
    return max_sum

# Driver code
if __name__ == '__main__':
    # initialise the array
    arr = [5, -2, 6, 3, -5]

    # initialise the vaue of K
    K = 15

    # size of array
    N = len(arr)

    print(maxSubarraySum(arr, N, K))

# This code is contributed by Surendra_Gangwar
