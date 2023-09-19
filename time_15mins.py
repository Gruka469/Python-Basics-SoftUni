hour = int(input())
min = int(input())

new_minute = (min + 15) % 60
new_hour = (hour + (min + 15) // 60) % 24

print(f"{new_hour}:{new_minute:02d}")