# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
# Your task is to create a Python script that analyzes the records to calculate each of the following:

# As an example, your analysis should look similar to the one below:
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv
import locale

from numpy.lib.function_base import select

locale.setlocale(locale.LC_ALL,'en_US')

# Locate and open CSV file
csvpath = os.path.join("Resources","budget_data.csv")
csvfile = open(csvpath,'r')
budget = csv.reader(csvfile)

#remove heade3rs
csv_header = next(budget)

#create lists
month = []
data = []
months = []
datas = []

#append column info into lists
for row in budget:
    month = str(row[0])
    data = int(row[1])
    
    months.append(month)
    datas.append(data)
    
 # The total number of months included in the dataset
count = len(months)

print(count)

# The net total amount of "Profit/Losses" over the entire period
total = sum(datas)

print(locale.currency(total, grouping = True))

# Identify min and max of "Profit/Losses", calculate average and difference

lowest_amt = min(datas)
highest_amt = max(datas)

# print(lowest_amt)
# print (highest_amt)

difference = highest_amt - lowest_amt
average = total/count

print(locale.currency(difference, grouping = True))
print(locale.currency(average, grouping = True))

# The greatest increase in profits (date and amount) over the entire period
print(locale.currency(highest_amt, grouping = True))
if highest_amt == row[0]:
        highest_date(row)

print(highest_date)

# The greatest decrease in profits (date and amount) over the entire period
print(locale.currency(lowest_amt, grouping = True))
