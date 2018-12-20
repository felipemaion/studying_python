# https://codefights.com/arcade/intro/level-12/ywMyCTspqGXPWRZx5
# Check if the given string is a correct time representation of the 24-hour clock.
#
# Example
#
# For time = "13:58", the output should be
# validTime(time) = true;
# For time = "25:51", the output should be
# validTime(time) = false;
# For time = "02:76", the output should be
# validTime(time) = false.

def validTime(time):
    groups = time.split(":")
    if len(groups) > 2:
        return False
    if 0 <= int(groups[0]) <= 23:
        if 0 <= int(groups[1]) <= 59:
            return True
    return False


print(validTime("13:58"))
print(validTime("13:78"))
print(validTime("24:18"))