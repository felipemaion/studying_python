# # https://codefights.com/arcade/intro/level-12/sqZ9qDTFHXBNrQeLC
# # You are given an array of desired filenames in the order of their creation.
# Since two files cannot have equal names, the one which comes later will have an addition
# to its name in a form of (k), where k is the smallest positive integer
# such that the obtained name is not used yet.

# Return an array of names that will be given to the files.

# Example

# For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
# fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].

def fileNaming(names):
    stored_files = []
    for name in names:
        print("Name:", name)
        if name in stored_files:
            i = 0
            new_name = name+str("({})".format(stored_files.count(name)))
            # print("Trying name:", new_name)
            while new_name in stored_files:
                # print("Not ok")
                new_name = name + str("({})".format(stored_files.count(name)+i))
                # print("Trying new name:", new_name)
                i +=1
            stored_files.append(new_name)
        else:
            stored_files.append(name)
    return stored_files

print(fileNaming(["doc", "doc", "image", "doc(1)", "doc"]))
# ['doc', 'doc(1)', 'image', 'doc(1)(1)', 'doc(2)']
names = ["a(1)", "a(6)", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
print(fileNaming(names))
# ["a(1)", "a(6)", "a", "a(2)", "a(3)", "a(4)", "a(5)", "a(7)", "a(8)", "a(9)", "a(10)", "a(11)"]
