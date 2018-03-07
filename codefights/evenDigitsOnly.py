# https://codefights.com/arcade/intro/level-6/6cmcmszJQr6GQzRwW
# Check if all digits of the given integer are even.
#
# Example
#
# For n = 248622, the output should be
# evenDigitsOnly(n) = true;
# For n = 642386, the output should be
# evenDigitsOnly(n) = false.

def evenDigitsOnly(n):
    n_s = list(str(n))
    for dig in n_s:
        if int(dig) % 2 != 0:
            return False
    return True


print(evenDigitsOnly(248622))
print(evenDigitsOnly(642386))