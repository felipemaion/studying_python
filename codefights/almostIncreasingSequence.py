# https://codefights.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG
#
#  Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.
#
# Example
#
# For sequence = [1, 3, 2, 1], the output should be
# almostIncreasingSequence(sequence) = false;
#
# There is no one element in this array that can be removed in order to get a strictly increasing sequence.
#
# For sequence = [1, 3, 2], the output should be
# almostIncreasingSequence(sequence) = true.
#
# You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] array.integer sequence
#
# Guaranteed constraints:
# 2 ≤ sequence.length ≤ 105,
# -105 ≤ sequence[i] ≤ 105.
#
# [output] boolean
#
# Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.
#




def almostIncreasingSequence(sequence):
    # for i in range(len(sequence)):
    #     cp = sequence.copy()
    #     del cp[i]
    #     if cp == sorted(list(set(cp))):
    #         return True
    # return False
    # # NOT OK DUE TO TIME LAPSED.
    #
    # ordered = sorted(sequence)
    # for i in range(len(sequence)):
    #     cp_or = ordered.copy()
    #     cp = sequence.copy()
    #     item = cp.pop(i)
    #     cp_or.remove(item)
    #     cp_or = [x for x in cp_or if cp_or.count(x) < 2]
    #     if cp == cp_or:
    #         return True
    # return False
    #     # NOT OK DUE TO TIME LAPSED.
    def get_not_increasing(sequence):
        for index in range(len(sequence) - 1):
            if sequence[index] >= sequence[index + 1]:
                # print(index)
                return index
        return -1

    bad_item_index = get_not_increasing(sequence)
    # print(bad_item_index, " ", sequence[bad_item_index])
    # Check if it is already in sequence.
    if bad_item_index == -1:
        return True

    # Check if it is in sequence without the bad item.

    new_seq = sequence[bad_item_index - 1:bad_item_index] + sequence[bad_item_index + 1:]
    # print(new_seq)
    if get_not_increasing(new_seq) == -1:
        return True

    # Check if the sequence is ok without the next item.
    # May be the bad item is the following one.
    new_seq = sequence[bad_item_index:bad_item_index + 1] + sequence[bad_item_index + 2:]
    # print(new_seq)
    if get_not_increasing(new_seq) == -1:
        return True

    return False


# print(almostIncreasingSequence([1, 3, 2, 1]))
print(almostIncreasingSequence([10, 1, 2, 3, 4, 5, 6, 1]))