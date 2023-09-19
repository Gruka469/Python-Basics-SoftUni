musala_count = 0
monblan_count = 0
kilimanjaro_count = 0
K2_count = 0
everest_count = 0


group_climbers = int(input())
for _ in range(group_climbers):
    current_climbers = int(input())
    if current_climbers < 6:
        musala_count += current_climbers
    elif current_climbers < 13:
        monblan_count += current_climbers
    elif current_climbers < 26:
        kilimanjaro_count += current_climbers
    elif current_climbers < 41:
        K2_count += current_climbers
    elif current_climbers >= 41:
        everest_count += current_climbers


total_climbers = musala_count + monblan_count + kilimanjaro_count + K2_count + everest_count

musala_percent = musala_count / total_climbers * 100
monblan_percent = monblan_count / total_climbers * 100
kilimanjaro_percent = kilimanjaro_count / total_climbers * 100
K2_percent = K2_count / total_climbers * 100
everest_percent = everest_count / total_climbers * 100

print(f"{musala_percent :.2f}%")
print(f"{monblan_percent :.2f}%")
print(f"{kilimanjaro_percent :.2f}%")
print(f"{K2_percent :.2f}%")
print(f"{everest_percent :.2f}%")