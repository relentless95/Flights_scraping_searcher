class DataTransformer:

    def transf_price_into_int(self, price):
        # Transform the price value into INT
        self.price = price
        return self.price.str.replace(',', '').str.replace('$', '').astype('int')

    def no_blank_values_df(self, dataframe_to_clean):
        self.dataframe_to_clean = dataframe_to_clean
        # Remove rows containing blank values
        return self.dataframe_to_clean[(self.dataframe_to_clean['start_destination'].notnull()) & (self.dataframe_to_clean['end_destination'].notnull())
                                       & (self.dataframe_to_clean['start_date'].notnull()) & (self.dataframe_to_clean['price'].notnull())
                                       & (self.dataframe_to_clean['num_stops'].notnull()) & (self.dataframe_to_clean['airline_names'].notnull())
                                       & (self.dataframe_to_clean['stop_cities'].notnull()) & (self.dataframe_to_clean['journey_duration'].notnull())
                                       & (self.dataframe_to_clean['dep_time'].notnull()) & (self.dataframe_to_clean['dep_meridiem'].notnull())
                                       & (self.dataframe_to_clean['arrival_time'].notnull()) & (self.dataframe_to_clean['arrival_meridiem'].notnull())]
