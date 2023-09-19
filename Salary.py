count_open_tabs = int(input())
salary = int(input())

for tabs_open in range(count_open_tabs):
    tabs_open = input()
    if tabs_open == "Facebook":
        salary -= 150
    elif tabs_open == "Instagram":
        salary -= 100
    elif tabs_open == "Reddit":
        salary -= 50
    if salary <= 0:
        break


if salary > 0:
    print(salary)
else: 
    print("You have lost your salary.")




# MY SOLUTION

# count_open_tabs = int(input())
# salary = int(input())

# for tabs_open in range(count_open_tabs):
#     tabs_open = input()
#     if tabs_open == "Facebook":
#         salary -= 150
#     elif tabs_open == "Instagram":
#         salary -= 100
#     elif tabs_open == "Reddit":
#         salary -= 50
#     else:
#         pass

# if salary <= 0:
#     print("You have lost your salary.")
# else:
#     print(salary)