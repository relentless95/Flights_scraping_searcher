## Flights_scraping_searcher
![webscraping image](/images/Web-Scraping-Using-Selenium-and-Python.jpg "web-scraping")


This repo contains the full code divided into three parts: 'step_one.py', 'step_two.py', 'step_three.py'.
Each of them can be used separately.
Please, read the 'requirements' file to know, what packages, classes and files you need for each step.

#### Important!!! All files should be located in the same folder.
We recommend you to download the whole folder instead of separate files.

### Step One: 
* Web Scraping 
  1. To use the webscraper please refer to specify the airport code. 
  Click here to find the appropriate [airport code](https://www.nationsonline.org/oneworld/IATA_Codes/airport_code_list.html)
  2. Enter the appropriate parameters and run the script.
  3. Note that you cannot scrape data 2 years in advance. i.e if we are in 2022 you can't scarape data for 2024 because
  the website doesn't provide the data.

### Step Two: 
* Data transformation (from strings to integers, cleaning blank values.
* Simple descriptive analysis (pandas): 
  1. Top three cheapest airlines, 
  1. Average price per number of stops, 
  1. Average price per departure time on am/pm.

### Step Three:
* Search filter to find flights by:
  1. Numbers of stops,
  1. Departure on am/pm,
  1. Price.
* Visualisation with plots (pandas, mathplotlib,seaborn):
  1. The average flight price per date,
  1. Number of flights per airline,
  1. Airline vs averagePrice
