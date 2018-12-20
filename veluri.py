files = {"Input.txt": "Randy", "Code.py": "Stan", "Output.txt": "Randy"}

owners = []
dict_owners = {}

# Get the owners:
for values in files.values():
    owners.append(values)
# Remove the duplicates:
owners = list(set(owners))

# Create a dict with the owners:
for owner in owners:
    dict_owners[owner] = []

# Append each file to the owner dictionary
for key,values in files.items():
    dict_owners[values].append(key)

print(dict_owners)
