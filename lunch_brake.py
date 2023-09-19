# series_name = str(input())
# ep_time = int(input())
# break_time = int(input())

# lunch_time = break_time * 0.125
# rest_time = break_time * 0.25

# remaining_time = break_time - lunch_time - rest_time

# if remaining_time >= ep_time:
#     print(f"You have enough time to watch {series_name} and left with {remaining_time} minutes free time.")

# elif remaining_time < ep_time:
#     time_needed = break_time - lunch_time - rest_time
#     print(f"You don't have enough time to watch {series_name}, you need {time_needed} more minutes.")

import math

serial_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
rest_time = break_duration / 4
remaining_time = break_duration - lunch_time - rest_time

if remaining_time >= episode_duration:
    leftover_time = math.ceil(remaining_time - episode_duration)
    print(f"You have enough time to watch {serial_name} and left with {leftover_time} minutes free time.")
else:
    needed_time = math.ceil(episode_duration - remaining_time)
    print(f"You don't have enough time to watch {serial_name}, you need {needed_time} more minutes.")