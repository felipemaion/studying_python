# Tô querendo escrever um script que verifica e
# Imprime caracteres subsequentes em uma string...
# Ex: s= 'shjabcdjhio'


import string

def find_sequence_string(strng):
    strng = strng.lower()
    all_alphabet = list(string.ascii_lowercase)
    groups = []
    current_seq = ''
    prev_char = 'z' # Greatest
    for char in strng:
        if all_alphabet.index(prev_char)+1 == all_alphabet.index(char):
            current_seq += char
            prev_char = char
        else:
            groups.append(current_seq)
            prev_char = char
            current_seq = char
    groups.append(current_seq)
    groups = [group for group in groups if len(group) > 1]
    return groups

print(find_sequence_string( "tarasabcduikjuvwxabop"))
# ['abcd', 'uvwx', 'ab', 'op']
print(find_sequence_string( "shjabcdjhio"))
# ['abcd', 'hi']

