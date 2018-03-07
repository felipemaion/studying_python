# https://codefights.com/arcade/intro/level-6/6Wv4WsrsMJ8Y2Fwno
# Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.
#
# Check if the given string is a correct variable name.
#
# Example
#
# For name = &quot;var_1__Int&quot;, the output should be
# variableName(name) = true;
# For name = &quot;qq-q&quot;, the output should be
# variableName(name) = false;
# For name = &quot;2w2&quot;, the output should be
# variableName(name) = false.
import re
def variableName(name):
    ## Regex would solve it... but it is ugly...
    return bool(re.match("^[^\d\W]\w*\Z", name))
    ## So I may use:
def variableName1(name):
    if name.isidentifier():
        return True
    return False

import string
def variableName2(name):
    ## but this is not as 'readable' as this:
    #
    valid = string.ascii_letters + "_"
    full_valid = valid  + string.digits
    if name[0] not in valid:
        return False
    for chr in name:
        if chr not in full_valid:
            return False
    return True
    #
    #
    #   # PICK A SOLUTION....

print(variableName("a-a"))
print(variableName1("a-a"))
print(variableName2("a-a"))
print(variableName("teste_"))
print(variableName1("teste_"))
print(variableName2("teste_"))
print(variableName("1teste_"))
print(variableName1("1teste_"))
print(variableName2("1teste_"))
