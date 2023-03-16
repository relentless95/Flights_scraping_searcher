from Flights_scraping_searcher.scraper import scrape
import pandas as pd


year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
start_day = int(input("Enter the starting date: "))
end_day = int(input("Enter the ending date: "))
start_destination = input("Enter the airport code: ")
end_destination = input("Enter the ending destination: ")


scraped_results = scrape(year, month, start_day, end_day, start_destination, end_destination)
print(scraped_results)

df = pd.DataFrame(scraped_results, columns=['start_destination', 'end_destination', 'start_date', 'price', 'num_stops',
                                  'airline_names', 'stop_cities', 'journey_duration', 'dep_time', 'dep_meridiem',
                                  'arrival_time', 'arrival_meridiem'])
df.to_csv('{0}.csv'.format("flights_data"), index=False)

print('finished')
