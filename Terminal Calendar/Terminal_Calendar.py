# Enter how many days in the month
days_in_month = int(input("Enter number of days in the month: "))

if days_in_month < 28 or days_in_month > 31:
    print("Invalid number of days. Please enter a value between 28 and 31.")
    exit()

# Enter the starting day of the week (1=Monday, 7=Sunday)
starting_day = int(input("Enter starting day of the week (1=Mon, 7=Sun): "))

# Print the calendar header
print("Mon Tue Wed Thu Fri Sat Sun")

# Print leading spaces for the first week
for _ in range(starting_day - 1):
    print("    ", end="")

# Print the days of the month
for day in range(1, days_in_month + 1):
    print(f"{day:2} ", end="")
    if (day + starting_day - 1) % 7 == 0:
        print()  # New line after Sunday    