import re

my_string = "dcaabbbaaccd"

def remove_middle_group(my_string):
    groups = [item[0] for item in re.findall(r"((.)\2*)", my_string)]
    middle = groups[int(len(groups)/2)]
    groups.remove(middle)
    return "".join(groups)

while len(my_string) > 2:
    my_string = remove_middle_group(my_string)
