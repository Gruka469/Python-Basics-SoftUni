from math import floor

current_record = float(input())
meters_swimmed = float(input())
sec_for_meter = float(input())

sum_meters_per_sec = meters_swimmed * sec_for_meter

delay = floor(meters_swimmed / 15) * 12.5

total_time = sum_meters_per_sec + delay

if current_record > total_time:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

else:
    print(f"No, he failed! He was {total_time - current_record:.2f} seconds slower.")
