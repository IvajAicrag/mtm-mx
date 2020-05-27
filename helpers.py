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

    #return the indexes of the numbers in the combination
    indexes = get_index(numbers,best_combination)
    return indexes, best_sum
    #Return the numbers of the sequence
    #return best_combination, best_sum

#best_combination, best_sum = best(numbers,target)

#print("\nbest sum{} = {}".format(best_combination, best_sum))

#divide list
def chunker_list(seq, size):
    return (seq[i::size] for i in range(size))

#get indexes from the best combination
def get_index(sequence, combination):

    final = []
    for i in combination:
        count = 0
        for j in sequence:
            if j == i:
                if count in final:
                    count +=1
                    continue
                final.append(count)
                break
            count += 1
    return(final)

#Test
#a = [1,1,3,5,6,7,4]
#r = [1,1,5,6]
#print(get_index(a,r))

#a = [1,2,3,4,5,6]
#r = [6,3,4]
#print(get_index(a,r))

#a = [1,1,1,3,1,5,6,7,2,3]
#r = [2,3,1,7,1]
#print(get_index(a,r))
