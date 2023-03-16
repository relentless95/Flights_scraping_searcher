## Flights_scraping_searcher
![webscraping image](/images/Web-Scraping-Using-Selenium-and-Python.jpg "web-scraping")


This repo contains the full code divided into three parts: 'step_one.py', 'step_two.py', 'step_three.py'.
Each of them can be used separately.
Please, read the 'requirements' file to know, what packages, classes and files you need for each step.

#### Important!!! All files should be located in the same folder.
We recommend you to download the whole folder instead of separate files. Don't change names of folders and files.

### Step One: 
* Only for Windows OS. For Mac OS or Linux OS start from the 'step_two.py' file. 
* Web Scraping (creates 'flights_data.csv' file for further steps).
  1. To use the webscraper please refer to specify the airport code. 
  Click here to find the appropriate [airport code](https://www.nationsonline.org/oneworld/IATA_Codes/airport_code_list.html)
  2. Enter the appropriate parameters and run the script.
  3. Note that you cannot scrape data 2 years in advance. i.e if we are in 2022 you can't scarape data for 2024 because
  the website doesn't provide the data.

### Step Two: 
* If you skip the Step One, use 'flights_data.csv' file that is included to the current folder.
* Data transformation:
  1. From strings to integers, 
  2. Cleaning blank values,
  3. Creates additional 'clean_data.csv' and 'step_two_logfile.log' files.
* Simple descriptive analysis (pandas): 
  1. Top three cheapest airlines, 
  1. Average price per number of stops, 
  1. Average price per departure time on am/pm.

### Step Three:
* Search filter to find flights by:
  1. Numbers of stops,
  2. Departure on am/pm,
  3. Price.
  4. Creates additional 'searcher_one.csv' and 'step_three_logfile.log' files.
* Visualisation with plots (pandas, matplotlib,seaborn):
  1. The average flight price per date,
  1. Numbers of flights per airline,
  1. The average flight price per airline
