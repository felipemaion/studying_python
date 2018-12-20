# https://codefights.com/arcade/intro/level-3/3o6QFqgYSontKsyk4
# You have a string s that consists of English letters, punctuation marks,
#  whitespace characters, and brackets. It is guaranteed that the parentheses in s form a regular bracket sequence.
#
# Your task is to reverse the strings contained in each pair of matching parentheses, starting from the innermost pair.
# The results string should not contain any parentheses.
#
# Example
#
# For string s = "a(bc)de", the output should be
# reverseParentheses(s) = "acbde"
#
def reverseParentheses(s):
    new_s = ""
    inside = False
    buffer = []
    buffer_count = -1
    for chr in s:
        if inside and chr != "(" and chr != ")": #
            buffer[buffer_count] += chr
        else:
            if chr != "(" and chr != ")":
                new_s += chr
        if chr == "(":
            inside = True
            buffer.append("")
            buffer_count += 1
        if chr == ")":
            if buffer_count < 1:
                new_s += buffer[buffer_count][::-1]
                inside = False
            else:
                buffer[buffer_count - 1] += buffer[buffer_count][::-1]
            print("\tBuffer[",buffer_count,"]:", buffer[buffer_count])
            buffer[buffer_count] = ""
            buffer_count -= 1
    return new_s



# Tests:
s = "a(bcdefghijkl(m(no))p)q"
print(s)
print(reverseParentheses(s)) #
print("apmonlkjihgfedcbq")


s = "Code(Cha(lle)nge)"
print(s)
print(reverseParentheses(s))
print("CodeegnlleahC")