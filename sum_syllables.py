vowel_values = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}

input_word = input()
total_sum = 0

for letter in input_word:
    if letter.lower() in vowel_values:
        total_sum += vowel_values[letter.lower()]

print(total_sum)