#ask for user input
days_in_month=int(input("How many days are in the month?"))
start_day = int(input("What day of the week does the month start on? (0=Sun, 1=Mon, ..., 6=Sat) "))

#print the header
print("Su Mo Tu We Th Fr Sa")

#initial space
for space in range(start_day):
    print("   ", end="")
current_day = start_day

#loop through the days of the month
for day in range(1, days_in_month + 1):
    print(f"{day:2} ", end="")
    current_day += 1
    if current_day == 7:
        print()  # New line at the end of the week
        current_day = 0
if current_day != 0:
    print()  # Final new line if the last week is not complete

    