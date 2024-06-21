import datetime

def main():
    fridays = []
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    for year in range(1900, 2100):
        for month in range(1, 13):
            if datetime.datetime(year, month, 13).weekday() == 4:
                fridays.append(datetime.datetime(year, month, 13))
            


    for friday in fridays:
        text = datetime.datetime(friday.year, friday.month, 1).strftime('%Y %B')
        print(text)

if __name__ == "__main__":
    main()
