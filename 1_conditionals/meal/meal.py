# Prompt user for the time
def main():
    time = input("What time is it? ")

    if time.endswith("a.m.") or time.endswith("p.m."):
        time = time_format(time)

    time = convert(time)

# Conditional statements
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        print(" ")

# Convert 24 hr format to hours as float
def convert(time):
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60

# Convert 12 hr format to 24 hr format
def time_format(time):
    time = time.split(" ")
    hours, minutes = map(int, time[0].split(":"))
    if time[1] == "a.m." and hours == 12:
        hours = 0
    elif time[1] == "p.m." and hours != 12:
        hours += 12
    return str(hours) + ":" + str(minutes)

# Allows check50 to test my convert function separately
if __name__ == "__main__":
    main()


