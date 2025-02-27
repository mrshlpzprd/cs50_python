def main():
    fraction_ok = False
    while fraction_ok == False:
        user_fraction = input("Fraction: ")

        try:
            splitted_user_fraction = user_fraction.split("/")
            if len(splitted_user_fraction) == 2:
                X = splitted_user_fraction[0]
                Y = splitted_user_fraction[1]

                if X.isnumeric() and Y.isnumeric():
                    fraction_ok = fuel_gauge(X, Y)
        except (ValueError, ZeroDivisionError):
            pass

def fuel_gauge(X, Y):
    if int(X) <= int(Y):
        fuel_percentage = round(int(X) / int(Y) * 100)

        if fuel_percentage >= 99:
            print("F")
        elif fuel_percentage <= 1:
            print("E")
        else:
            print(f"{fuel_percentage}%")
        return True
    else:
        return False

main()






