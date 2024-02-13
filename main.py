def parse_month(month):
    months = {
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    }
    return months.get(month, "")


def parse_date(user_string):
    month, day, year = user_string.split()
    day = day.rstrip(",")
    month_num = parse_month(month)
    return f"{month_num}/{day.zfill(2)}/{year}"


if __name__ == '__main__':
    while True:
        user_input = input()
        if user_input == "-1":
            break
        else:
            x = parse_date(user_input) #I like the letter x
            print(x)