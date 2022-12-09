from Flights_scraping_searcher.scraper import scrape
import pandas as pd

while True:
    try:
        year = int(input("Enter the year in digits: "))
        if type(year) == int:
            break
        else:
            raise ValueError
    except ValueError:
        print("Please enter digits")
print(year)


while True:
    try:
        month = int(input("Enter the month in digits: "))
        if type(month) == int:
            break
        else:
            raise ValueError
    except ValueError:
        print("Please enter digits")
print(month)

while True:
    try:
        start_day = int(input("Enter the starting date in digit: "))
        if type(start_day) == int:
            break
        else:
            raise ValueError
    except ValueError:
        print("Please enter digits")
print(start_day)

while True:
    try:
        end_day = int(input("Enter the ending date: "))
        if type(end_day) == int:
            break
        else:
            raise ValueError
    except ValueError:
        print("Please enter digits")
print(end_day)

while True:
    try:
        start_destination = input("Enter the starting destination's airport code: ").upper()
        if type(start_destination) == str:
            break
        else:
            raise ValueError
    except ValueError:
        print("Please enter digits")
print(start_destination)

while True:
    try:
        end_destination = input("Enter the ending destination's airport code: ").upper()
        if type(end_destination) == str:
            break
        else:
            raise ValueError
    except ValueError:
        print("Please enter digits")
print(end_destination)


scraped_results = scrape(year, month, start_day, end_day, start_destination, end_destination)
print(scraped_results)

df = pd.DataFrame(scraped_results, columns=['start_destination', 'end_destination', 'start_date', 'price', 'num_stops',
                                  'airline_names', 'stop_cities', 'journey_duration', 'dep_time', 'dep_meridiem',
                                  'arrival_time', 'arrival_meridiem'])
df.to_csv('{0}.csv'.format("flights_data"), index=False)

print('finished')
