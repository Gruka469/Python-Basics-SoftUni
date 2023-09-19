actor = str(input())
starting_points = float(input())
judges_count = int(input())

total_point = starting_points

for _ in range(judges_count):
    judge_name = input()
    judge_points = float(input())
    total_point += len(judge_name) * judge_points / 2
    if total_point > 1250.5:
        break

if total_point > 1250.5:
    print(f'Congratulations, {actor} got a nominee for leading role with {total_point :.1f}!')
else:
    print(f'Sorry, {actor} you need {1250.5 - total_point :.1f} more!')