import matplotlib.pyplot as plt
import seaborn as sns


class DataDescriptor:
    def __init__(self, df):
        self.df = df

    def data_head(self):
        return print('\n', self.df.head())

    def data_info(self):
        return print('\n', self.df.info())

    def rows_number(self):
        return print('\nNumber of Rows: ' + str(len(self.df)))

    def top_cheapest_airlines(self):
        # Display  three airlines with the lowest price.
        #  We group the rows in df by airline and find the average price for each airline.
        avg_price_airline = self.df.groupby('airline_names')['price'].mean().nsmallest(3)
        return print(f"\nTop 3 cheapest flights by airlines: {avg_price_airline}")

    def average_price_number_stop(self):
        # Calculate the average price per num stops.
        avg_price_num_stops = self.df.groupby('num_stops')['price'].mean().nsmallest()
        return print(f"\nThe average price per number of stops: {avg_price_num_stops}")

    def average_price_am_pm(self):
        # Calculate the average price per am/pm.
        avg_price_am_pm = self.df.groupby('dep_meridiem')['price'].mean().nsmallest()
        return print(f"\nThe average price per departure on am/pm: {avg_price_am_pm}")

    def plot_average_price_per_date(self):
        # Create a plot that shows the average flight price per date
        df_date = self.df.groupby('start_date')['price'].mean()
        plt.figure(figsize=(16, 8))
        plt.xlabel('Date')
        plt.ylabel('price ($)')
        plt.title('Price of Flight Vs Date')
        plt.plot(df_date)
        plt.xticks(rotation=85)
        return plt.show()

    def plot_flights_per_airline(self):
        # Count of flights v/s Airline
        plt.figure(figsize=(15, 10))
        plt.title('Count of flights with different Airlines')
        ax = sns.countplot(x='airline_names', data=self.df)
        plt.xlabel('Airline')
        plt.ylabel('Count of flights')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(int(p.get_height()), (p.get_x()+0.25, p.get_height()+1), va='bottom', color='black')
        return plt.show()

    def plot_average_price_per_airline(self):
        # Airline vs AveragePrice
        dvsp1 = sns.barplot(x='airline_names', y='price', ci=None, data=self.df)
        dvsp1.set_title('Airline V/S Price')
        dvsp1.set_ylabel('Price (€)')
        dvsp1.set_xticklabels(dvsp1.get_xticklabels(), rotation=80)
        return plt.show()
