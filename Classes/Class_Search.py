class Search:

    def __init__(self, number_of_stops, departure_am_pm, maximum_price, clear_data_frame):
        self.num_stops = number_of_stops
        self.dep_am_pm = departure_am_pm
        self.max_price = maximum_price
        self.clear_data_frame = clear_data_frame

    def __str__(self):
        return f"\nSearcher One selected following filters: {self.num_stops}, departure on {self.dep_am_pm}, price below {self.max_price} "

    def select_num_stops(self, clear_data_frame):
        df_num_stops = clear_data_frame[(clear_data_frame['num_stops'] == self.num_stops)]
        return df_num_stops

    def select_dep_am_pm(self, clear_data_frame):
        df_dep_am_pm = clear_data_frame[(clear_data_frame['dep_meridiem'] == self.dep_am_pm)]
        return df_dep_am_pm

    def select_max_price(self, clear_data_frame):
        df_max_price = clear_data_frame[(clear_data_frame['price'] < self.max_price)]
        return df_max_price
