from datetime import date, time, datetime

today = date.today()

t_now = datetime.time(datetime.now())

print(t_now)

def main():
    today = datetime.now()
    
    wd = datetime.weekday(today)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    print('today is day number %d' % wd)

    print('And today is: ', days[wd])

if __name__ == '__main__':
    main()