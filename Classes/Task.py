import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import date
import random


class Task(webdriver.Chrome):
    """
    This subclass inherits form the class webdriver.Chrome
    """
    def __init__(self,
                 driver_path=r"./Flights_scraping_searcher"):
        # instantiate the class
        self._driver_path = driver_path
        os.environ['PATH'] += self._driver_path
        super(Task, self).__init__()
        self.set_window_position(-10000, 0)  # to put the window in the background
        self.implicitly_wait(30)
        self._f_date = None

    def page_url(self, year, month, day, start, end):
        # to get the page url
        self._f_date = date(year, month, day)
        # print(self.f_date)
        self.get(f'https://www.kayak.com/flights/{start}-{end}/{self._f_date}?sort=bestflight_a')
        print(f'https://www.kayak.com/flights/{start}-{end}/{self._f_date}?sort=bestflight_a')

    def more_results(self):
        # click to get more results
        time.sleep(random.randint(5, 10))
        try:
            button = self.find_element(By.CSS_SELECTOR, "a[class='moreButton']")
            button.click()
            print("loading more results")
            button.click()
            print("loading more results")
            button.click()
            print("loading more results")
            button.click()
            print("loading more results")
            button.click()
            print("loading more results")
            # button.click()
            # print("sixth click worked")
        except:
            print("couldn't load more results")

    def get_html(self):
        # to download the html from the page
        return self.page_source

    def quit_chrome(self):
        # to quit the driver
        print('quiting')
        self.quit()
