# GPU_COST = 250
# CPU_COST = GPU_COST * 0.35
# RAM_COST = GPU_COST * 0.1


# budget = float(input())
# gpu_quantity = int(input())
# cpu_quantity = int(input())
# ram_quantity = int(input())


# gpu_total = gpu_quantity * GPU_COST
# cpu_total = cpu_quantity * CPU_COST
# ram_total = ram_quantity * RAM_COST

# total_price = gpu_total + cpu_total + ram_total

# if gpu_quantity > cpu_quantity:
#     total_price *= 0.85

# if budget >= total_price:
#     remaining_budget = budget - total_price
#     print(f"You have {remaining_budget:.2f} leva left!")

# else:
#     need_amount = total_price - budget
#     print(f"Not enough money! You need {need_amount:.2f} leva more!")


budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

video_cards_price = video_cards * 250
processors_price = processors * (video_cards_price * 0.35)
ram_price = ram_memory * (video_cards_price * 0.1)

total_price = video_cards_price + processors_price + ram_price

if video_cards > processors:
    total_price -= total_price * 0.15

if budget >= total_price:
    left_budget = budget - total_price
    print(f"You have {left_budget:.2f} leva left!")
else:
    needed_amount = total_price - budget
    print(f"Not enough money! You need {needed_amount:.2f} leva more!")