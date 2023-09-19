import math

card_price = int(input())
adapter_price = int(input())
power_consumption = float(input())
daily_profit = float(input())

total_card_price = card_price * 13
total_adapter_price = adapter_price * 13
total_cost = total_card_price + total_adapter_price + 1000

daily_income = 13 * (daily_profit - power_consumption)
return_days = math.ceil(total_cost / daily_income)

print(total_cost)
print(return_days)
