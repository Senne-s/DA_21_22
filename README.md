# DA_21_22
Databases Advanced year 2021-2022 - Senne Schaerlaeken 2IMS

### Concept
This is a real-time webscraper that collects data of bitcoin transactions while running. After it is manually shut down you can write the highest transaction of every minute to a text file.
The website being scraped in real-time is: https://www.blockchain.com/btc/unconfirmed-transactions

### Usage
You use the scraper as follows:
1) Execute the code with the imports, we need these libraries.
2) Execute the "Scrape" function and let it run for a few minutes.
3) Manually stop the script.
4) Execute the rest of the code. You can ignore any warning signs since the code just warns you about the manual interruption.
5) You will now find a text file called "transactions.txt". This file contains the highest transactions per minute.
