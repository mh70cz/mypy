"""
Bite 134. Two Sums 

https://codechalleng.es/bites/134
"""

     
            
def two_sums_mh(numbers, target):
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """
    candidates = []
    srtnums = sorted(numbers)
    len_num = len(srtnums)
    for i in range(len_num):
        if srtnums[i] > target:
            break
        for j in range(i, len_num):
            if srtnums[i] == srtnums[j]:
                continue
            if (srtnums[i] + srtnums[j]) > target:
                break
            if srtnums[i] + srtnums[j] == target:
                candidates.append((srtnums[i],srtnums[j]))
    if candidates == []:
        return None
    candidates.sort(key= lambda x: x[0])
    idx1 = numbers.index(candidates[0][0])
    idx2 = numbers.index(candidates[0][1])

    return (idx1, idx2)


def two_sums(numbers, target):
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """
    nums = sorted(numbers)
    i = 0
    j = len(numbers) - 1
    while i < j:
        total = nums[i] + nums[j]
        if total < target:
            i += 1
        elif total > target:
            j -= 1
        else:
            index1 = numbers.index(nums[i])
            index2 = numbers.index(nums[j])
            return index1, index2
    return None

