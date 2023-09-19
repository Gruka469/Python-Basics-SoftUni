import math

W_POINTS = 2000
F_POINTS = 1200
SF_POINTS = 720

tournaments_count = int(input())
starting_points = int(input())
tota_point = 0
total_wins = 0

for _ in range(tournaments_count):
    tournament_result = input()

    if tournament_result == "W":
        tota_point += W_POINTS
        total_wins += 1
    elif tournament_result == "F":
        tota_point += F_POINTS
    elif tournament_result == "SF":
        tota_point += SF_POINTS

total_points = starting_points + tota_point
average_points = math.floor(tota_point / tournaments_count)
percent_finals = total_wins / tournaments_count * 100

print(f"Final points: {total_points}")
print(f"Average points: {int(average_points)}")  # Закръгляме към най-близкото цяло надолу
print(f"{percent_finals:.2f}%")