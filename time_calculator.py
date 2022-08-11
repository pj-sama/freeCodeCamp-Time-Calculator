from numpy import full


def add_time(start, duration):
    start_split = start.split(" ")  # splits time component from AM/PM
    full_start_time = start_split[0].split(":")
    start_hour = int(full_start_time[0])
    start_minutes = int(full_start_time[1])

    am_pm = start_split[1].strip()

    duration_split = duration.split(":")  # split duration into components
    duration_hour = int(duration_split[0])
    duration_minute = int(duration_split[1])
    final_minute = start_minutes+duration_minute

    if final_minute >= 60:
        duration_hour = duration_hour + 1
        final_minute = final_minute - 60

    final_hour = start_hour + duration_hour

    days_passed = 0
    print("\n")
    print(final_hour)
    print("\n")
    while final_hour >= 12:
        final_hour = final_hour - 12
        if am_pm == "AM":
            am_pm = "PM"
        elif am_pm == "PM":
            am_pm = "AM"
            days_passed = days_passed + 1

    if final_hour == 0:
        final_hour = 12 #because 12 hour time is weird
    if days_passed == 0:
        new_time = f"{final_hour}:{format(final_minute, '02')} {am_pm}"
    elif days_passed == 1:
        new_time = f"{final_hour}:{format(final_minute, '02')} {am_pm} (next day)"
    else:
       new_time = f"{final_hour}:{format(final_minute, '02')} {am_pm} ({days_passed} days later)"

    return new_time


print(add_time("11:59 PM", "24:05"))
