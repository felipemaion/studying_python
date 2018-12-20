# https://codefights.com/arcade/intro/level-9/xHvruDnQCx7mYom3T
# Each day a plant is growing by upSpeed meters.
# Each night that plant's height decreases by downSpeed meters due to the lack of sun heat.
# Initially, plant is 0 meters tall. We plant the seed at the beginning of a day.
#  We want to know when the height of the plant will reach a certain level.

# Example

# For upSpeed = 100, downSpeed = 10 and desiredHeight = 910, the output should be
# growingPlant(upSpeed, downSpeed, desiredHeight) = 10.
def growingPlant(upSpeed, downSpeed, desiredHeight):
    height = 0
    days = 0
    while not height >= desiredHeight:
        height += upSpeed
        days += 1
        if height >= desiredHeight:
            break
        height -= downSpeed
    return days

print(growingPlant(100,10,910))
print(growingPlant(10,9,4))

# Input:
# upSpeed: 10
# downSpeed: 9
# desiredHeight: 4
# Output:
# 4
# Expected Output:
# 1
# Console Output:
# Empty