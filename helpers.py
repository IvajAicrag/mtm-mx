import math
import itertools

#numbers = [7,4,3,2,3,4,1,1,3,6,]
#target = 9
#print("target:{}\nnumbers:{}".format(target,numbers))


def best(numbers, target):

    best_combination = ((None,))
    best_result = math.inf
    best_sum = 0


    # generate all combinations of the numbers
    # including combinations with different lengths


    for L in range(0, len(numbers)+1):
        for combination in itertools.combinations(numbers, L):
            sum = 0
            for number in combination:
                sum += number
            result = target - sum
            if result < 0:
                continue
            if abs(result) < abs(best_result):
                best_result = result
                best_combination = combination
                best_sum = sum
                #print("\nnew best\n{}\nsum:{} off by:{}".format(best_combination, best_sum, best_result))
    return best_combination, best_sum

#best_combination, best_sum = best(numbers,target)

#print("\nbest sum{} = {}".format(best_combination, best_sum))
