# Python Reflection: Disassembling the secret
# There is a string of 32 alphanumeric characters hidden inside a dynamically 
# generated function, which will then be passed into your function.

# Your task is to recover this string and return it.

def find_the_secret(f):
#     for met in dir(f.__code__):
#         print(met, getattr(f.__code__,met))
    return f.__code__.co_consts[1]

