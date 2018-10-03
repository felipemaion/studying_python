my_list = ["abc", "bac", "bca"]

my_list.sort(key=lambda x: x[1])
print(my_list)

def mySort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i][1]>alist[i+1][1]: # Here is where you are sorting on the second char.
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

my_list = ["abcasdas", "bacasdasd", "bcaasdsad","asdsadeq","asdasdasdfreq"]
print(mySort(my_list))