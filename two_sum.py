some_string = input()
sum_of_points = 0
for symbol in some_string:
    if symbol == "a":
        sum_of_points += 1
    elif symbol == "e":
        sum_of_points += 2
    elif symbol == "i":
        sum_of_points += 3
    elif symbol == "o":
        sum_of_points += 4
    elif symbol == "u":
        sum_of_points += 5
    
print(sum_of_points)
