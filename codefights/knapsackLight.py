# https://codefights.com/arcade/intro/level-9/r9azLYp2BDZPyzaG2
# You found two items in a treasure chest!
# The first item weighs weight1 and is worth value1,
# and the second item weighs weight2 and is worth value2.
# What is the total maximum value of the items you can take with you,
# assuming that your max weight capacity is maxW and you can't come back for the items later?

# Note that there are only two items and you can't bring more than one item of each type,
# i.e. you can't take two first items or two second items.

# Example

# For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4 and maxW = 8, the output should be
# knapsackLight(value1, weight1, value2, weight2, maxW) = 10.

# You can only carry the first item.

# For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4 and maxW = 9, the output should be
# knapsackLight(value1, weight1, value2, weight2, maxW) = 16.

# You're strong enough to take both of the items with you.

# For value1 = 5, weight1 = 3, value2 = 7, weight2 = 4 and maxW = 6, the output should be
# knapsackLight(value1, weight1, value2, weight2, maxW) = 7.

# You can't take both items, but you can take any of them.

def knapsackLight(value1, weight1, value2, weight2, maxW):
    item1 = [value1,weight1]
    item2 = [value2,weight2]
    weights = [weight1,weight2]
    values = [value1, value2]
    items = [item1,item2]
    # I can take all them?:
    if maxW >= sum(weights):
        return sum(values)
    else:
        # I cannot take any of them:
        if weights[0] > maxW and weights[1] > maxW:
            return 0
        # Find the most valuable and see if I can take it, else take the other.
        return max(items)[0] if max(items)[1] <= maxW else min(items)[0]

print(knapsackLight(value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, maxW = 8))#10
print(knapsackLight(value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, maxW = 9))#16
print(knapsackLight(value1 = 5, weight1 = 3, value2 = 7, weight2 = 4, maxW = 6))#7
print(knapsackLight(value1 = 5, weight1 = 3, value2 = 7, weight2 = 4, maxW = 1))#0
print(knapsackLight(value1 = 15, weight1 = 2, value2 = 20, weight2 = 3, maxW = 2)) #15
print(knapsackLight(value1 = 2, weight1 = 5, value2 = 3, weight2 = 4, maxW = 5)) #3