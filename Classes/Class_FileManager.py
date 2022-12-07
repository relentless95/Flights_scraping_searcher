import pandas as pd
import os
import platform


class FileManager:
    def __init__(self, name_of_file_with_data='flight_prices_september.csv'):
        self.name_of_file_with_data = name_of_file_with_data

    def open_data(self):
        # Open a csv file with data
        return pd.read_csv(self.name_of_file_with_data)

    def save_clean_data(self, my_clean_data, name_of_saved_file='clean_data.csv', __folder_path=os.getcwd()):
        self.my_clean_data = my_clean_data
        self.name_of_saved_file = name_of_saved_file
        self.__folder_path = __folder_path

        # Save filtered_data in a csv file
        # If MAC or Linux, then folder path uses "/" if Windows then "\\"(backslash) in Python
        user_platform = platform.system()
        if user_platform == 'Linux':
            folder_path_with_file_name = str(self.__folder_path + "/" + self.name_of_saved_file)
        elif user_platform == 'Darwin':
            folder_path_with_file_name = str(self.__folder_path + "/" + self.name_of_saved_file)
        else:
            folder_path_with_file_name = str(self.__folder_path + "\\" + self.name_of_saved_file)
        print(f'\nA file with data saved here: {self.__folder_path}. It is called {self.name_of_saved_file}')
        return self.my_clean_data.to_csv(rf"{folder_path_with_file_name}")
