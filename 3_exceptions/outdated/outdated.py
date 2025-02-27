# Months list
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Prompt user for date and output YYYY-MM-DD
def main():
    while True:
        try:
            date = input('Date: ').strip()

# Print for MM-DD-YYYY
            m_d_y = mm_dd_yyyy(date) or mth_dd_yyyy(date)
            if m_d_y:
                print(f"{m_d_y['yyyy']}-{m_d_y['mm']:02}-{m_d_y['dd']:02}")
                break
        except:
            pass

# MM-DD-YYYY
def mm_dd_yyyy(date):
    s_d = date.split("/")
    if len(s_d) == 3:
        date_ok = {"mm": int(s_d[0]), "dd": int(s_d[1]), "yyyy": int(s_d[2])}
        for index, val in enumerate(s_d):
            if val.isnumeric():
                if index == 0 and (int(val) < 1 or int(val) > 12):
                    return False
                if index == 1 and (int(val) < 1 or int(val) > 31):
                    return False
                if index == 2 and len(val) != 4:
                    return False
            else:
                return False
    else:
        return False
    return date_ok

# month day, year
def mth_dd_yyyy(date):

        s_d_comma = date.split(",")
        if len(s_d_comma) == 2:
            yyyy = s_d_comma[1].lstrip()
            s_d_m_d = s_d_comma[0].split(" ")
            s_d = [s_d_m_d[0], s_d_m_d[1], yyyy]
            mm = s_d[0]
            dd = s_d[1]

            if mm in months:
                mm_i = months.index(mm) + 1
                date_ok = {'mm': int(mm_i), 'dd': int(dd), 'yyyy': int(yyyy)}

                if len(yyyy) != 4:
                    return False
                if int(dd) < 1 or int(dd) > 31:
                    return False
            else:
                return False
            return date_ok
        else:
            return False

main()
