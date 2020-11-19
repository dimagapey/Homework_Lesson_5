from datetime import date

def day_check(month, day):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return 0 < day <= days_in_month[month-1]

def month_check(month):
    return 0 < month <= 12

def year_check(year):
    return 1 <= len(year) <= 4

def main():
    date = str(input("Введите дату в формате dd/mm/yyyy: "))
    try:
        day,month,year = date.split("/")
        month_validity = month_check(int(month))
        day_validity = day_check(int(month),int(day))
        year_validity = year_check(year)
        if month_validity and day_validity and year_validity:
            print("Дата {0} корректная.".format(date))
        else:
            print("Дата {0} некорректная.".format(date))
    except ValueError:
        print('Некорректный ввод. Введите дату в формате dd/mm/yyyy.')
    except IndexError:
        print('Некорректная дата.')

if __name__ == "__main__":
    main()