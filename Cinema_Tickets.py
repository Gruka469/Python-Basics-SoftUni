total_tickets = 0
students_total = 0
standart_total = 0
kids_total = 0

command = input()  # Command for "Finish" or "current_movie_name"

while command != "Finish":
    current_movie_name = command
    total_seats = int(input())
    available_seats = total_seats

    students_count = 0
    standart_count = 0
    kids_count = 0

    while available_seats > 0:
        current_ticket_type = input()

        if current_ticket_type == "End":
            break

        available_seats -= 1
        total_tickets += 1

        if current_ticket_type == "student":
            students_count += 1
        elif current_ticket_type == "standard":
            standart_count += 1
        elif current_ticket_type == "kid":
            kids_count += 1

    percent_full = (total_seats - available_seats) / total_seats * 100
    print(f"{current_movie_name} - {percent_full:.2f}% full.")

    students_total += students_count
    standart_total += standart_count
    kids_total += kids_count

    command = input()

percent_students = (students_total / total_tickets) * 100 if total_tickets > 0 else 0
percent_standart = (standart_total / total_tickets) * 100 if total_tickets > 0 else 0
percent_kids = (kids_total / total_tickets) * 100 if total_tickets > 0 else 0

print(f"Total tickets: {total_tickets}")
print(f"{percent_students:.2f}% student tickets.")
print(f"{percent_standart:.2f}% standard tickets.")
print(f"{percent_kids:.2f}% kids tickets.")
