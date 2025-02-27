def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    fuel_status = gauge(percentage)
    print(fuel_status)

def convert(fraction):
    try:
        splitted_fraction = fraction.split("/")
        if len(splitted_fraction) == 2:
            X = splitted_fraction[0]
            Y = splitted_fraction[1]
            if X.isnumeric() and Y.isnumeric():
                percentage = round(int(X) / int(Y) * 100)
                print(percentage)
                return percentage
        raise ValueError
    except (ValueError, ZeroDivisionError):
        raise

def gauge(percentage):
    Z = percentage
    if Z <= 1:
        return "E"
    elif Z >= 99:
        return "F"
    else:
        return f"{Z}%"

if __name__ == "__main__":
    main()
