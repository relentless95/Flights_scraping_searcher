if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    import logging
    logging.basicConfig(filename='step_three_logfile.log', filemode='w', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO)

    # Let's create a simple search engine to find the personalised flight
    # with the particular preferences (Number of stops, departure am/pm, price)

    # Open a csv file with clean data
    from Classes import FileManager
    data_file = FileManager.FileManager('clean_data.csv')
    df = data_file.open_data()
    logging.info('%s Initial csv is opened')

    # Filter dataframe according the user's preferences: number of stops, departure on am or pm, price
    while True:
        try:
            number_of_stops = input("\nChoose 1 stop, 2 stops or 3 stops: ")
            if number_of_stops in ['1 stop', '2 stops', '3 stops']:
                break
            else:
                raise NameError
        except Exception as e:
            print('Please, write "1 stop", "2 stops" or "3 stops"')
            logging.error("Exception occurred", exc_info=True)

    while True:
        try:
            departure_am_pm = input("\nChoose the departure time am or pm: ")
            if departure_am_pm in ['am', 'pm']:
                break
            else:
                raise NameError
        except Exception as e:
            print('Please, write "am" or "pm"')
            logging.error("Exception occurred", exc_info=True)

    while True:
        try:
            maximum_price = int(input("\nEnter max flight price: "))
            if type(maximum_price) == int:
                break
            else:
                raise TypeError
        except TypeError as e:
            print('Please, write a whole number ')
            logging.error("Exception occurred", exc_info=True)

    # Create a class Searcher One
    from Classes import Search
    searcher_one = Search.Search(number_of_stops, departure_am_pm, maximum_price, clear_data_frame=df)
    print(searcher_one)
    logging.info('%s Searcher one class is created', searcher_one)

    # Search process filter by filter: num stops, departure  time: am/pm, max price
    try:
        filter_num_stops = searcher_one.select_num_stops(clear_data_frame=df)
        filter_num_stops_am_pm = searcher_one.select_dep_am_pm(clear_data_frame=filter_num_stops)
        filter_num_stops_am_pm_price = searcher_one.select_max_price(clear_data_frame=filter_num_stops_am_pm)

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)

    # Save info in a csv file with filtered info:
    filtered_data_file = FileManager.FileManager()
    filtered_data_file.save_clean_data(my_clean_data=filter_num_stops_am_pm_price, name_of_saved_file='searcher_one.csv')

    # Open the created csv file
    data_file = FileManager.FileManager('searcher_one.csv')
    df2 = data_file.open_data()

    # Let's create some plots
    from Classes import DataDescriptor
    describe_df2 = DataDescriptor.DataDescriptor(df=df2)

    # Create a plot that shows the average flight price per date
    describe_df2.plot_average_price_per_date()

    # Count of flights v/s Airline
    describe_df2.plot_flights_per_airline()

    # Airline vs AveragePrice
    describe_df2.plot_average_price_per_airline()
