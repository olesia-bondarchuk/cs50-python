from datetime import date
from num2words import num2words

def main():
    user_date = input("Date of birth(YYYY-MM-DD): ")
    minutes = difference_between_two_dates_in_minutes(user_date)
    result = number_to_words(minutes)
    print(f'{result}')

def difference_between_two_dates_in_minutes(start_date):
    today = date.today()
    before_year, before_month, before_day = start_date.split('-')
    before = date(int(before_year), int(before_month), int(before_day))
    difference = today - before

    return difference.total_seconds() / 60

def number_to_words(number):
    word = num2words(number)

    return word.replace('-','')

if __name__ == "__main__":
    main()
