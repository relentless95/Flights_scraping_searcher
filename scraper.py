from Classes.Parser import Parser
from Classes.Task import Task
import time
import random


def scrape(year: "int", month: "int", start_day: "int", end_day: "int", start_destination: "str",
           end_destination: "str"):
    end_day = end_day + 1
    b_li = []
    for i in range(1, end_day):
        print(f"scraping page: {start_day}")
        webpage = Task()
        webpage.page_url(year, month, start_day, start_destination, end_destination)
        webpage.more_results()
        h = webpage.get_html()
        webpage.quit_chrome()
        tags = Parser(h, year, month, start_day, start_destination, end_destination)
        tags.sauce_finder()
        tags.find_item()
        b_li.extend(tags.items())
        start_day += 1
        time.sleep(random.randint(10, 30))
    return b_li

