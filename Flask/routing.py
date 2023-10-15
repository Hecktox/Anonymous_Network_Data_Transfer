import random

def trim_list(strings, min_length=4):
    if len(strings) <= min_length:
        return strings
    else:
        trimmed_length = random.randint(min_length, len(strings))
        trimmed_list = random.sample(strings, trimmed_length)
        return trimmed_list

def scramble_list(strings):
    random.shuffle(strings)
    return strings

# Example usage:
original_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew"]
trimmed_list = trim_list(original_list)
scrambled_list = scramble_list(trimmed_list)

print("Original List:", original_list)
print("Trimmed List:", trimmed_list)
print("Scrambled List:", scrambled_list)
