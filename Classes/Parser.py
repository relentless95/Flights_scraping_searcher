from bs4 import BeautifulSoup
from datetime import date


class Parser:
    """
    takes as input the html from the Task class
    """
    def __init__(self, html, year, month, day, start, end, a_li=None):
        # instantiating the class with the above arguments
        if a_li is None:
            self.a_li = []
            self._html = html
            self._start_destination = start
            self._end_destination = end
            self._f_date = date(year, month, day)
            self._sauce = None
            self._all_items = None
            self._price = None
            self._n_stop = None
            self._airline_names = None
            self._stop_cities = None
            self._duration = None
            self._departure_time = None
            self._departure_meridiem = None
            self._arrival_time = None
            self._arrival_meridiem = None
        else:
            self.a_li = []
            self._html = html
            self._start_destination = start
            self._end_destination = end
            self._f_date = date(year, month, day)
            self._sauce = None
            self._all_items = None
            self._price = None
            self._n_stop = None
            self._airline_names = None
            self._stop_cities = None
            self._duration = None
            self._departure_time = None
            self._departure_meridiem = None
            self._arrival_time = None
            self._arrival_meridiem = None

    def sauce_finder(self):
        # to parse the html
        self._sauce = BeautifulSoup(self._html, 'lxml')
        return self._sauce

    def find_item(self):
        # finding the items of interest
        self._all_items = self._sauce.find_all('div', class_='Flights-Results-FlightResultItem')
        return self._all_items

    def items(self):
        # further parsing each of the elements of interest i.e price, number of stops etc.
        for item in self._all_items:
            self._price = item.find('span', class_='price-text').text.strip()
            # print(price)
            self._n_stop = item.find('span', class_='stops-text').text.strip()
            # print(n_stop)
            time_data = item.find_all('div', class_='top')
            self._duration = time_data[2].text.strip()
            self._departure_time = time_data[0].find('span', class_='depart-time').text.strip()
            self._departure_meridiem = time_data[0].find('span', class_='time-meridiem').text.strip()
            self._arrival_time = time_data[0].find('span', class_='arrival-time').text.strip()
            self._arrival_meridiem = time_data[0].find_all('span', class_='time-meridiem')[-1].text.strip()
            flight_info = item.find_all('div', class_='bottom')  # getting the flight info
            self._airline_names = flight_info[0].text.strip()
            # print(airline_names)
            self._stop_cities = flight_info[1].text.strip()
            self.a_li.append([self._start_destination, self._end_destination, self._f_date, self._price,
                              self._n_stop, self._airline_names, self._stop_cities, self._duration,
                              self. _departure_time, self._departure_meridiem, self._arrival_time,
                              self._arrival_meridiem])

        return self.a_li

