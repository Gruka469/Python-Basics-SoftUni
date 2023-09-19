lenght = int(input())
width = int(input())
height = int(input())
percent_non_empty = float(input())

total_volume = lenght * width * height
total_volume_in_liters = total_volume / 1000

water_needed = total_volume_in_liters * (100 - percent_non_empty) / 100

print(water_needed)